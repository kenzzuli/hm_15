from selenium import webdriver
import time
import json


class DouyuSpider:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def get_content_list(self):  # 提取数据和下一页按钮
        content_list = list()
        lis = self.driver.find_elements_by_xpath(
            "//section[@class='layout-Module js-ListContent']//ul[@class='layout-Cover-list']/li")
        for li in lis:
            item_dict = dict()
            url = li.find_elements_by_xpath("./div/a")
            img = li.find_elements_by_xpath(".//div[@class='DyListCover-imgWrap']/div/img")
            cate = li.find_elements_by_xpath(".//div[@class='DyListCover-info']/span[@class='DyListCover-zone']")
            title = li.find_elements_by_xpath(".//div[@class='DyListCover-info']/h3[@class='DyListCover-intro']")
            num = li.find_elements_by_xpath(".//div[@class='DyListCover-info']/span[@class='DyListCover-hot']")
            anchor = li.find_elements_by_xpath(".//h2[@class='DyListCover-user']/div[@class='DyListCover-userName']")
            desc = li.find_elements_by_xpath(".//span[@class='HeaderCell-label-wrap is-od']")

            item_dict["url"] = url[0].get_attribute("href") if url else None
            item_dict["img"] = img[0].get_attribute("src") if img else None
            item_dict["cate"] = cate[0].text if cate else None
            item_dict["title"] = title[0].text if title else None
            item_dict["num"] = num[0].text if num else None
            item_dict["anchor"] = anchor[0].text if anchor else None
            item_dict["desc"] = desc[0].text if desc else None
            content_list.append(item_dict)

        # 有时候会找不到这个元素而报错，是因为页面没有完全加载出来，最好每次获取页面后都要等几秒✅
        next_page_button = self.driver.find_element_by_xpath("//li[@title='下一页']")
        return content_list, next_page_button

    def save_content_list(self, content_list):  # 保存数据
        with open("./douyu.txt", mode="a", encoding="utf8") as f:
            f.write(json.dumps(content_list, ensure_ascii=False, indent=2))
        print("保存成功")

    def run(self):  # 实现主要逻辑
        # 1.请求起始url
        self.driver.get(self.start_url)
        time.sleep(3)
        while True:
            # 2.提取数据，和下一页按钮
            content_list, next_page_button = self.get_content_list()
            # 3.保存数据
            self.save_content_list(content_list)
            # 4.点击翻页
            # 4.1 判断下一页按钮是否可以点击，如果不可以则退出循环，如果可以则点击
            if next_page_button.get_attribute("aria-disabled") == "true":
                break
            else:
                next_page_button.click()
                time.sleep(5)
        # 5.循环2-4
        # 6.退出driver
        self.driver.quit()


if __name__ == '__main__':
    douyu_spider = DouyuSpider()
    douyu_spider.run()
