import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36",

}
cookies = "BIDUPSID=A9ED107CDA04315473528F700F5BB884; PSTM=1602854207; BAIDUID=A9ED107CDA04315459EF911AEED8EAB0:FG=1"

# 将字符串转成字典
cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
print(cookies)
# 在发送请求时，加上cookies参数
r = requests.get("http://www.renren.com/327550029/profile", headers=headers, cookies=cookies)

# 保存页面
with open("renren3.html", "w", encoding="utf8") as f:
    f.write(r.content.decode("utf8"))
