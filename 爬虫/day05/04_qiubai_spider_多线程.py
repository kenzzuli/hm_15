from lxml import etree
import requests
import json
from queue import Queue
from threading import Thread
import time


class QiubaiSpider:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
        self.url_template = "https://www.qiushibaike.com/text/page/{}/"
        self.url_queue = Queue()  # url队列
        self.html_queue = Queue()  # 响应队列
        self.content_queue = Queue()  # 数据队列

    def enqueue_urls(self):  # 将所有待请求的url放入队列
        for i in range(1, 14):
            self.url_queue.put(self.url_template.format(i))

    def parse_url(self):  # 发送请求获取响应，将响应放入队列中
        while True:  # 这是一个死循环，让一个线程不停的做这个事
            url = self.url_queue.get()  # 仅仅get，队列长度不减
            print(url)
            self.html_queue.put(requests.get(url, headers=self.headers).content)
            # 先将当前队列的内容put下一环节的队列中，再让当前队列task_done，这种耦合能确保所有数据都被处理
            # 如果没有这种耦合，可能会出现这种情况：
            # 当前队列有一条数据，下一队列中没有数据，当前队列get后立刻task_done，此时当前队列就空了，
            # 而这条数据还在处理，未传到下一队列中，下一队列也是空，
            # 这时数据并没有全部处理完，但两个队列都空了，q.join会解堵塞，主线程执行结束，所有守护线程结束，整个程序结束。
            self.url_queue.task_done()  # 先get，再task_done，这样队列长度才减一

    def get_content_list(self):  # 获取数据
        while True:  # 死循环
            content_list = list()
            html_str = self.html_queue.get()  # 从响应队列中获取html_str
            html = etree.HTML(html_str)
            # 获取结果分组
            div_list = html.xpath("//div[contains(@class, 'article block untagged mb15 typs')]")
            for div in div_list:
                item = dict()
                # 作者信息
                author = dict()
                author_name = div.xpath("./div[@class='author clearfix']//h2/text()")
                author_img = div.xpath("./div[@class='author clearfix']//img/@src")
                author_gender = div.xpath(".//div[contains(@class, 'articleGender')]/@class")
                author_age = div.xpath(".//div[contains(@class, 'articleGender')]/text()")
                author["author_name"] = author_name[0].strip() if author_name else None
                author["author_img"] = "https:" + author_img[0].split("?imageView")[0] if author_img else None
                author["author_gender"] = author_gender[0].split()[-1][:-4] if author_gender else None
                author["author_age"] = author_age[0] if author_age else None
                item["author"] = author
                # 笑话
                content = div.xpath(".//div[@class='content']/span/text()")
                item["content"] = "\n".join(content).strip() if content else None
                # 当前点赞数和评论数
                status = dict()
                vote_number = div.xpath("./div[@class='stats']/span[@class='stats-vote']/i/text()")
                comment_number = div.xpath(
                    "./div[@class='stats']/span[@class='stats-comments']//i[@class='number']/text()")
                status["vote_number"] = vote_number[0] if vote_number else None
                status["comment_number"] = comment_number[0] if comment_number else None
                item['status'] = status
                # 最佳评论者、最佳评论、最佳评论点赞数
                comment = dict()
                best_commenter = div.xpath("./a[@class='indexGodCmt']//span[@class='cmt-name']/text()")
                best_comment = div.xpath("./a[@class='indexGodCmt']//div[@class='main-text']/text()")
                best_comment_like_number = div.xpath(
                    "./a[@class='indexGodCmt']//div[@class='main-text']/div[@class='likenum']/text()")
                comment["best_commenter"] = best_commenter[0].strip()[:-1] if best_commenter else None
                comment["best_comment"] = best_comment[0].strip() if best_comment else None
                comment["best_comment_like_number"] = "".join(
                    best_comment_like_number).strip() if best_comment_like_number else None
                item["comment"] = comment
                content_list.append(item)

            self.content_queue.put(content_list)  # 将数据放入数据队列
            self.html_queue.task_done()  # 让响应队列长度减一

    def save_content_list(self):  # 保存数据
        while True:  # 死循环
            content_list = self.content_queue.get()  # 从数据序列获取数据
            with open("./tmp/qiubai.txt", mode="a", encoding="utf8") as f:
                f.write(json.dumps(content_list, ensure_ascii=False, indent=2))
                f.write("\n")
            print("保存成功")
            self.content_queue.task_done()  # 让数据序列长度减一

    def run(self):  # 实现主要逻辑
        thread_list = list()  # 保存所有线程
        # 1.将所有待请求的url放入队列
        thread_list.append(Thread(target=self.enqueue_urls))
        # 2.发送请求获取响应
        for i in range(20):  # 这里可能较慢，多分配几个线程
            thread_list.append(Thread(target=self.parse_url))
        # 3.提取数据
        for i in range(20):  # 这里可能较慢，多分配几个线程
            thread_list.append(Thread(target=self.get_content_list))
        # 4.保存数据
        thread_list.append(Thread(target=self.save_content_list))

        # 启动所有线程
        # 进程启动后会默认产生一个主线程，默认情况下主线程创建的子线程都不是守护线程（setDaemon(False)）。
        # 因此主线程结束后，子线程会继续执行，进程会等待所有子线程执行完毕后才结束

        # 如果不设置子线程为守护线程，主线程结束后，子线程仍会执行，进程会等待所有子线程执行结束后才结束，
        # 数据确实能全部爬取，但这里子线程全是死循环，根本无法结束，进程也就无法结束。
        for t in thread_list:
            t.setDaemon(True)  # 将子线程设置为守护线程，该线程不重要，主线程结束，子线程就结束
            t.start()

        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()  # 让主线程阻塞，直到队列中的任务完成 如果上面代码任何环节少了一个task_done，主线程就会卡死在这

        # 当主线程执行到这里时，全部队列中的任务都已经完成，但子线程仍在死循环中
        # 由于设置了子线程为守护进程，主线程结束，子线程就结束，死循环就停了
        print("主线程结束")


if __name__ == '__main__':
    start_time = time.time()
    qiubai_spider = QiubaiSpider()
    qiubai_spider.run()
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
    # 0.43483591079711914
