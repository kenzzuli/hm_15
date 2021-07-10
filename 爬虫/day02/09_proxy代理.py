import requests

url = "http://www.baidu.com"
proxies = {
    "http": "http://180.183.27.225:8080"
}
headers = {
    "cookie": "BIDUPSID=4605EF59F8ADD4DDC07A417C10B9F3C0; PSTM=1578983328; BAIDUID=4109A7FBACC39A30E12409E85FF9E29B:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; DOUBLE_LANG_SWITCH=0; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; delPer=0; H_PS_PSSID=1429_21095_18559_26350_30498; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1579266775,1579314208,1579402140; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1579402168; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1579314657,1579402168; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1579402168; __yjsv5_shitong=1.0_7_6397b4f578d5cdd3e38a743c63141afd2cc0_300_1579409241580_112.8.215.146_666f9998; yjs_js_security_passport=54bd2e66dc50db2bd3cfb49cf968b3b4bc353348_1579409242_js",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36"}

response = requests.get(url, headers=headers, proxies=proxies)
print(response.request.headers)
# print(response.content.decode())
# print(response.status_code)
