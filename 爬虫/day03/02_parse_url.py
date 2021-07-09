# 一个通用的发送get请求的模板函数
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}


def parse_url(url):
    try:
        response = requests.get(url, headers=headers, timeout=3)
        assert response.status_code == 200
    except Exception as e:
        print(e)
        return None
    else:
        return response.content.decode()


if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(parse_url(url))
