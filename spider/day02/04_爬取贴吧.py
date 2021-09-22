import requests


def tieba_spider(tieba, num):
    for i in range(num):
        url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&tp=0&pn={}".format(tieba, 50 * i)
        file_name = "{}吧-{}.txt".format(tieba, i)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        response = requests.get(url, headers=headers)

        print(response.status_code)
        print(response.request.url)
        print(response.url)
        with open("./tmp/" + file_name, "wb") as f:
            f.write(response.content)


if __name__ == '__main__':
    tieba_spider("李毅", 100)
