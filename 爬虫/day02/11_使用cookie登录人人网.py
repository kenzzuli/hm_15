import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36",
    "Cookie": "bid=bGhQvRDCvUA; gr_user_id=178b9403-9b62-4e36-936f-027fae51de34"
}
# 加上登录后获取的cookie请求登录后才能访问的地址
r = requests.get("http://www.renren.com/327550029/profile", headers=headers)

# 保存页面
with open("renren2.html", "w", encoding="utf8") as f:
    f.write(r.content.decode("utf8"))
