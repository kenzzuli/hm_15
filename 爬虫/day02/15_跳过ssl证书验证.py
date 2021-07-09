import requests

# 跳过SSL证书验证
response = requests.get("https://www.12306.cn/mormhweb/ ", verify=False)
print(response.status_code)
