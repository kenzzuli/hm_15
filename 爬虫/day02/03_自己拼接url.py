import requests

kw = {"wd": "上海"}
url = "http://www.baidu.com/s?wd={}".format(kw["wd"])
print(url)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.request.url)
print(response.url)
# print(response.content.decode())

