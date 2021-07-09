import requests
import sys
import json
import execjs


class TranslateSpider:
    def __init__(self, source_text):
        self.url_detect = "https://fanyi.baidu.com/langdetect"
        self.url_translate = "https://fanyi.baidu.com/basetrans"
        self.header = {
            "cookie": "BIDUPSID=4605EF59F8ADD4DDC07A417C10B9F3C0; PSTM=1578983328; BAIDUID=4109A7FBACC39A30E12409E85FF9E29B:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; DOUBLE_LANG_SWITCH=0; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; delPer=0; H_PS_PSSID=1429_21095_18559_26350_30498; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1579266775,1579314208,1579402140; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1579402168; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1579314657,1579402168; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1579402168; __yjsv5_shitong=1.0_7_6397b4f578d5cdd3e38a743c63141afd2cc0_300_1579409241580_112.8.215.146_666f9998; yjs_js_security_passport=54bd2e66dc50db2bd3cfb49cf968b3b4bc353348_1579409242_js",
            "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36"}
        self.detect_data = {
            "query": source_text
        }
        with open("/Users/ken/PycharmProjects/hm_15/爬虫/day02/BaiDuFanyi.js", 'r') as f:
            resp = f.read()
        self.sign = execjs.compile(resp).call('e', source_text)

    def _send_post_(self, urls, data):  # 发送post请求
        response = requests.post(urls, data=data, headers=self.header).content.decode("utf-8")
        return response

    def detect(self):  # 语言检测
        language = json.loads(self._send_post_(self.url_detect, self.detect_data))["lan"]
        return language

    def build_trans_data(self, language):  # 构造翻译数据
        trans_data = {
            "query": source_text,
            "from": "en" if language == "en" else "zh",
            "to": "zh" if language == "en" else "en",
            "token": "3018ae176904de63297751917421d1f7",
            "sign": self.sign
        }
        return trans_data

    def translate(self, translate_data):  # 翻译
        p = self._send_post_(self.url_translate, translate_data)
        # print(p)
        ret = json.loads(p)["trans"][0]["dst"]
        return ret

    def run(self):  # 实现主要逻辑
        # 语言检测
        language = self.detect()
        # 构造翻译数据
        trans_data = self.build_trans_data(language)
        # 翻译
        target_text = self.translate(trans_data)
        print(target_text)


if __name__ == '__main__':
    source_text = " ".join(sys.argv[1:])
    # print(source_text)
    trans_spider = TranslateSpider(source_text)
    trans_spider.run()
