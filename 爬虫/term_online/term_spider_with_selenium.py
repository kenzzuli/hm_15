from selenium import webdriver
import json
import os
import time
import pandas as pd

SLEEP_TIME = 60  # 每请求一次页面休息多长时间
PAGES = 20  # 请求一个术语的前多少页


class TermSpider:
    def __init__(self, term_list):
        self.term_list = term_list
        self.start_url = "https://www.termonline.cn/search?k={}"
        self.driver = webdriver.Chrome()
        self.base_dir = "./tmp"
        self.keys = ['Abbreviation', 'Also known as', 'Chinese', 'Commonly known as', 'Definition', 'English', 'Fields',
                     'Fields1', 'Full name', 'Once called', 'Source', 'Year_of_publication']
        self.template_dict = {i: None for i in self.keys}
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)

    def get_content_list(self, lis):
        try:
            content_list = list()

            for li in lis:
                # 初始化字典
                item_dict = self.template_dict.copy()
                chinese = li.find_elements_by_xpath(".//div[@class='cell']//span[@class='acts spz']")
                chinese = chinese[0].text if chinese else None
                english = li.find_elements_by_xpath(".//div[@class='cell']//span[@class='spz']")
                english = english[0].text if english else None
                _, _, fields1, year_of_pub = li.find_elements_by_xpath(".//div[@class='cell']")
                fields1 = fields1.text if fields1 else None
                year_of_pub = year_of_pub.text if year_of_pub else None
                ps = li.find_elements_by_xpath(".//div[@class='resulinfors']/p")
                ps_ret_dict = self.extract_ps(ps)

                item_dict["Chinese"] = chinese
                item_dict["English"] = english
                item_dict["Fields1"] = fields1
                item_dict["Year_of_publication"] = year_of_pub
                for key, value in ps_ret_dict.items():
                    item_dict[key] = value
                content_list.append(item_dict)

            return content_list
        except Exception as e:
            self.log_exception(e)

    def save_content_list(self, content_list, term, page_num):
        file_name = "{}.txt".format(term)
        with open(os.path.join(self.base_dir, file_name), mode="a", encoding="utf8") as f:
            f.write(json.dumps(content_list, ensure_ascii=False, indent=2))
        print("[{}]第{}页json格式保存成功".format(term, page_num))

        excel_name = "{}.xlsx".format(term)
        # 写入表格
        self.write_to_excel(content_list, os.path.join(self.base_dir, excel_name))
        print("[{}]第{}页excel格式保存成功".format(term, page_num))
        print("-" * 50)

    def write_to_excel(self, content_list, path):
        original_df = None
        if os.path.exists(path):
            original_df = pd.DataFrame(pd.read_excel(path, index_col=[0]))
            os.remove(path)
        new_df = pd.DataFrame(content_list)
        ret = original_df.append(new_df) if original_df is not None else new_df
        unique = ret.drop_duplicates().reset_index(drop=True)
        unique.to_excel(path)
        print("excel去重后有{}条数据".format(unique.shape[0]))

    def extract_ps(self, ps):
        temp_dict = dict()
        for p in ps:
            key = p.find_element_by_xpath(".//span[@class='title']").text.replace("：", "")
            value_list = p.find_elements_by_xpath(".//span[@class='spz']")
            value = "".join([i.text for i in value_list])
            if not value:
                value = p.text.split("：")[1]
            temp_dict[key] = value
        return temp_dict

    def log_exception(self, e):
        with open("./error.log", mode="a", encoding="utf8") as f:
            f.write(str(e) + "\n")

    def run(self):
        # 遍历术语表中的每个术语
        for term in self.term_list:
            # 访问起始页
            self.driver.get(self.start_url.format(term))
            time.sleep(SLEEP_TIME)
            page_num = 1
            while True:
                try:
                    # 获取页面内容
                    lis = self.driver.find_elements_by_xpath("//div[@class='resulistm']/ul/li")
                    print("[{}]第{}页包含{}数据".format(term, page_num, len(lis)))
                    # 提取数据
                    content_list = self.get_content_list(lis)
                    # 保存数据
                    self.save_content_list(content_list, term, page_num)
                    # 点击翻页
                    next_page_button = self.driver.find_element_by_xpath("//button[@class='btn-next']")
                    disabled = next_page_button.get_attribute("disabled")
                    # 如果disabled属性不为空，说明没有下一页了
                    if disabled:
                        break
                    else:
                        next_page_button.click()
                        time.sleep(SLEEP_TIME)
                    page_num += 1
                    if page_num > PAGES:
                        break
                except Exception as e:
                    self.log_exception(e)
                    break
            print("[{}]爬取结束".format(term))
            print("*" * 50)
        print("全部爬取结束")
        self.driver.quit()


if __name__ == '__main__':
    term_list = ["菌", "素", "毒", "霉素", "菌素", "病毒", "细胞", "剂", "液", "唑胺", "培养基", "药", "脂", "醇", "生物", "膜", "病"]
    term_spider = TermSpider(term_list)
    term_spider.run()
