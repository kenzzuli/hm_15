import requests
from requests.utils import dict_from_cookiejar, cookiejar_from_dict

response = requests.get("http://www.baidu.com")
print(response.cookies)
# <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>

# 将cookiejar对象转成字典
cookies = dict_from_cookiejar(response.cookies)
print(cookies)
# {'BDORZ': '27315'}
# 将字典转成cookiejar
cookiejar = cookiejar_from_dict(cookies)
print(cookiejar)
# <RequestsCookieJar[<Cookie BDORZ=27315 for />]>
