import requests

# 带不带s都行
# url = "http://www.baidu.com/s?"
url = "http://www.baidu.com/s"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
kw = {"wd": "上海"}
response = requests.get(url, headers=headers, params=kw)

print(response.status_code)
print(response.request.url)
print(response.url)
print(response.content.decode())
