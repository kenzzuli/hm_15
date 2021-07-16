import requests
from lxml import etree
import json
import time
import os
from parse_url import parse_url as parse

SLEEP_TIME = 60


class OxfordSpider:
    def __init__(self, wordlist_path):
        self.url_template = "https://www.lexico.com/definition/{}"
        self.wordlist_path = wordlist_path
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
        self.txt_dir = "./txt"
        self.html_dir = "./html"
        if not os.path.exists(self.txt_dir):
            os.mkdir(self.txt_dir)
        if not os.path.exists(self.html_dir):
            os.mkdir(self.html_dir)

    def parse_url(self, url, word):  # 发送请求，获取响应
        print(url)
        content = parse(url)
        # r = requests.get(url, headers=self.headers)
        if content:
            self.save_page_source(content, word)
        return content

    def save_page_source(self, content, word):
        file_name = "{}.html".format(word)
        file_path = os.path.join(self.html_dir, file_name)
        with open(file_path, mode="wb") as f:
            f.write(content)
        print("[{}]源网页保存成功".format(word))

    def get_word_dict(self, html_str, word):  # 提取数据
        # {"word_dict": "like"
        #  "meanings": [{meaning1}, {meaning2}, {meaning3}]
        # }
        try:
            word_dict = dict()
            main_meaning_list = list()
            html = etree.HTML(html_str)
            entry = html.xpath("//div[@class='entryWrapper']/*")
            # main_meaning_num = len(html.xpath("//div[@class='entryHead primary_homograph']"))
            new_meaning = True
            for item in entry:
                # print(item, item.tag, item.attrib['class'])
                if item.attrib["class"] == "breadcrumbs layout" and item.tag == "div":
                    # path = item.xpath("./div[@class='breadcrumbs layout']//text()")
                    continue
                if item.attrib["class"] == "entryHead primary_homograph" and item.tag == "div":
                    if new_meaning:
                        meaning = dict()
                        meaning['gramb_list'] = list()
                        meaning['usage_list'] = list()
                        meaning['etymology_list'] = list()
                        new_meaning = False
                    else:
                        main_meaning_list.append(meaning)
                        meaning = dict()
                        meaning['gramb_list'] = list()
                        meaning['usage_list'] = list()
                        meaning['etymology_list'] = list()
                        new_meaning = True
                if item.attrib["class"] == "gramb" and item.tag == "section":
                    meaning['gramb_list'].append(self.extract_gramb_section(item))
                if item.attrib["class"] == "etymology etym usage" and item.tag == "section":
                    meaning['usage_list'].append(self.extract_etymology_etym_usage_section(item))
                if item.attrib["class"] == "etymology etym" and item.tag == "section":
                    meaning['etymology_list'].append(self.extract_etymology_etym_section(item))

            main_meaning_list.append(meaning)
            word_dict["word_dict"] = word
            word_dict["main_meaning_list"] = main_meaning_list
            return word_dict
        except Exception as e:
            self.log_exception(e, word)

    def extract_etymology_etym_section(self, item):
        temp_dict = dict()
        etym_type = item.xpath(".//h3//text()")
        etym_type = etym_type[0].strip().lower()
        temp_dict['etym_type'] = etym_type
        if etym_type == "phrases":
            temp_dict['etym_content'] = self.extract_etym_phrases(item)
        elif etym_type == "origin":
            temp_dict['etym_content'] = self.extract_etym_origin(item)
        elif etym_type == "phrasal verbs":
            temp_dict['etym_content'] = self.extract_etym_phrases(item)
        else:
            raise NotImplementedError

        return temp_dict

    def extract_etym_phrases(self, item):
        ret_list = list()
        semb_gramb_ul = item.xpath(".//div[@class='senseInnerWrapper']//ul[@class='semb gramb']/*")
        new_meaning = True
        for element in semb_gramb_ul:
            if element.tag == "br":
                continue
            if element.tag == "strong" and element.attrib["class"] == "phrase":
                phrase = element.xpath(".//text()")
                if new_meaning:
                    meaning = dict()
                    meaning["phrase"] = phrase
                    new_meaning = False
                else:
                    ret_list.append(meaning)
                    meaning = dict()
                    meaning["phrase"] = phrase
                    new_meaning = True

            if element.tag == "span" and element.attrib["class"] == "sense-registers":
                sense_register = element.xpath(".//text()")
                meaning["sense_register"] = sense_register
            if element.tag == "ul" and element.attrib["class"] == "semb":
                phrase_info = self.extract_semb_ul(element)
                meaning["phrase_info"] = phrase_info
            if element.tag == "span" and element.attrib["class"] == "sense-regions spanish_label":
                sense_region = element.xpath(".//text()")
                meaning["sense_region"] = sense_region

        return ret_list

    def extract_semb_ul(self, item):
        temp_dict = dict()
        # 短语编号
        iteration = item.xpath(".//span[@class='iteration']/text()")
        sense_registers = item.xpath(".//span[@class='sense-registers']/text()")
        explanation = item.xpath(".//p//span[@class='ind one-click-content']//text()")
        sub_senses_lis = item.xpath(".//ol[@class='subSenses']")
        sub_senses = self.extract_sub_senses_lis_phrase(sub_senses_lis)

        temp_dict["iteration"] = iteration
        temp_dict["sense_register"] = sense_registers
        temp_dict["explanation"] = explanation
        temp_dict["sub_senses"] = sub_senses
        return temp_dict

    def extract_sub_senses_lis_phrase(self, item):
        ret_list = list()
        temp_dict = dict()
        for sub_sense_li in item:
            sub_sense_iteration = sub_sense_li.xpath(".//span[@class='subsenseIteration']//text()")
            sub_sense = sub_sense_li.xpath(".//span[@class='form-groups']/strong/text()")
            explanation = sub_sense_li.xpath(".//span[@class='ind one-click-content']//text()")
            examples = sub_sense_li.xpath(".//div[@class='examples']//ul[@class='english-ex']/li/em/text()")
            temp_dict['sub_sense_iteration'] = sub_sense_iteration
            temp_dict['sub_sense'] = sub_sense
            temp_dict['explanation'] = explanation
            temp_dict['examples'] = examples
            ret_list.append(temp_dict)
        return ret_list

    def extract_etym_origin(self, item):
        origin = item.xpath(".//div[@class='senseInnerWrapper']//text()")
        # origin = "".join(origin)
        return origin

    def extract_etymology_etym_usage_section(self, item):
        return item.xpath(".//div[@class='senseInnerWrapper']//text()")

    def extract_gramb_section(self, item):
        gramb = dict()
        meaning_list = list()
        pos = item.xpath(".//span[@class='pos']/text()")
        meanings = item.xpath(".//ul[@class='semb']/li")
        for meaning in meanings:
            meaning_list.append(self.extract_li(meaning))
        gramb['pos'] = pos
        gramb['meaning_list'] = meaning_list
        return gramb

    def extract_li(self, item):
        li = dict()
        meaning_num = item.xpath(".//p/span[@class='iteration']/text()")
        meaning = item.xpath(".//p/span[@class='ind one-click-content']/text()")
        example = item.xpath(".//div[@class='exg']/div[@class='ex']//span/text()")
        example = [i.strip()[1:-1] for i in example]
        examples_div = item.xpath(".//div[@class='trg']/div[@class='examples']")
        examples = self.extract_examples_div(examples_div)
        examples = [i.strip()[1:-1] for i in examples]
        synonyms = item.xpath(".//div[@class='trg']/div[@class='synonyms']/div[@class='exg']/div//text()")
        sub_senses_ol = item.xpath(".//div[@class='trg']/ol[@class='subSenses']")
        sub_senses = self.extract_sub_senses_ol(sub_senses_ol)
        li['meaning_num'] = meaning_num
        li['meaning'] = meaning
        li['example'] = example
        li['examples'] = examples
        li['synonyms'] = synonyms
        li['sub_senses'] = sub_senses
        return li

    def extract_sub_senses_ol(self, item):
        ret_list = list()
        if isinstance(item, list):
            if item:
                item = item[0]
            else:
                return None
        sub_sense_lis = item.xpath("./li[@class='subSense']")
        for sub_sense_li in sub_sense_lis:
            ret_list.append(self.extract_sub_senses_li(sub_sense_li))
        return ret_list

    def extract_sub_senses_li(self, item):
        sub_senses = dict()
        # 子义编号
        sub_sense_iteration = item.xpath(".//span[@class='subsenseIteration']/text()")
        # 子义
        sub_sense = item.xpath(".//span[@class='ind one-click-content']/text()")
        # 子义例句
        sub_sense_example = item.xpath(".//div[@class='exg']/div/em/span/text()")
        sub_sense_example = [i.strip()[1:-1] for i in sub_sense_example]
        # 子义更多例句
        sub_sense_examples = item.xpath(".//div[@class='examples']/div[@class='exg']/ul/li/em/text()")
        sub_sense_examples = [i.strip()[1:-1] for i in sub_sense_examples]
        # 子义近义词
        sub_sense_synonyms = item.xpath(".//div[@class='synonyms']/div[@class='exg']/div//text()")
        sub_senses['sub_sense_iteration'] = sub_sense_iteration
        sub_senses['sub_sense'] = sub_sense
        sub_senses['sub_sense_example'] = sub_sense_example
        sub_senses['sub_sense_examples'] = sub_sense_examples
        sub_senses['sub_sense_synonyms'] = sub_sense_synonyms
        return sub_senses

    def extract_examples_div(self, item):
        example_list = list()
        for i in item:
            example_list += i.xpath(".//div[@class='exg']/ul/li/em/text()")
        return example_list

    def save_word_dict(self, word_dict, word):
        file_name = "{}.txt".format(word)
        file_path = os.path.join(self.txt_dir, file_name)
        with open(file_path, mode="w", encoding="utf8") as f:
            f.write(json.dumps(word_dict, ensure_ascii=False, indent=2))
            f.write("\n")
        # print(word_dict)
        print("[{}]保存成功".format(word))
        print("-" * 50)

    def get_wordlist(self):
        with open(self.wordlist_path, mode="r", encoding="utf8") as f:
            return [i.strip().lower() for i in f.readlines() if i.strip()]

    def log_exception(self, e, word):
        with open("./error.log", mode="a", encoding="utf8") as f:
            f.write(word + "\t" + str(e) + "\n")

    def already_download(self, word):
        file_name = "{}.txt".format(word)
        file_list = os.listdir(self.txt_dir)
        if file_name in file_list:
            return True
        else:
            return False

    def run(self):
        # 1.获取url
        wordlist = self.get_wordlist()
        for word in wordlist:
            try:
                print("当前单词为:{}".format(word))
                if self.already_download(word):
                    print("[{}]已经下载过了，无需重复下载".format(word))
                    continue
                url = self.url_template.format(word)
                # 2.发送请求获取响应
                html_str = self.parse_url(url, word)
                # 3.提取数据
                if not html_str:  # 如果响应为空，直接跳过
                    time.sleep(SLEEP_TIME)
                    continue
                word_dict = self.get_word_dict(html_str, word)
                # 4.保存数据
                if not word_dict:  # 如果提取的数据为空，直接跳过
                    time.sleep(SLEEP_TIME)
                    continue
                self.save_word_dict(word_dict, word)
                # 休息后再请求
                time.sleep(SLEEP_TIME)
            except Exception as e:
                self.log_exception(e, word)
                time.sleep(SLEEP_TIME)
                continue


if __name__ == '__main__':
    wordlist_path = "./10k.txt"
    oxford_spider = OxfordSpider(wordlist_path)
    oxford_spider.run()
