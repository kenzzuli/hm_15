import requests

url = "http://www.baidu.com"
response = requests.get(url, timeout=1)
print(response)
