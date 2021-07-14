import requests

session = requests.session()
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email": "mr_mao_hacker@163.com", "password": "alarmchime"}
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36"
}
# 使用session发送post请求，cookie保存在其中
session.post(post_url, data=post_data, headers=headers)
# 再使用session请求登录之后才能访问的地址
r = session.get("http://www.renren.com/327550029/profile", headers=headers)

# 保存页面
with open("renren1.html", "w", encoding="utf8") as f:
    f.write(r.content.decode("utf8"))
