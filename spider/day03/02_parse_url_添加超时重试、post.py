# 一个通用的发送get请求的模板函数
# 使用retrying模块，增加超时重新请求
# 添加post请求
import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}


# 最多尝试10次
@retry(stop_max_attempt_number=10)
def _parse_url(url, method, data):
    # print("*" * 50) # 测试retry是否进行了多次请求
    if method.lower() == "get":
        response = requests.get(url, headers=headers, timeout=3)
    elif method.lower() == "post":
        response = requests.post(url, data=data, headers=headers, timeout=3)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method="GET", data=None):
    try:
        html_str = _parse_url(url, method, data)
    except Exception as e:
        print(e)
        html_str = None
    return html_str


if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(parse_url(url))
    data = {"from": "zh",
            "to": "en",
            "token": "3018ae176904de63297751917421d1f7",
            }
    print(parse_url(url, method="POST", data=data))
