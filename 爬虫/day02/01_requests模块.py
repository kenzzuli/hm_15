import requests


url = "http://www.baidu.com"
response = requests.get(url)

print(response.text)

# print(response.content)
print(response.status_code)
print(response.request.headers)
print(response.headers)