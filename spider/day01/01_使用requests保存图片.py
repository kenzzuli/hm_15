import requests

url = "https://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png"
# 发送请求
r = requests.get(url)
# 保存
with open("./img.png", mode="wb") as f:
    f.write(r.content)
