import gevent
from gevent import monkey
import urllib.request

monkey.patch_all()


def downloader(file_name, file_url):
    print("Downloading: ", file_url)
    file_name = "./img/" + file_name
    r = urllib.request.urlopen(file_url)
    content = r.read()
    with open(file_name, "wb") as f:
        f.write(content)
    print("{} bytes received from {}".format(len(content), file_url))


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg",
                     "https://rpic.douyucdn.cn/live-cover/roomCover/2021/03/12/d6e0881776e1937f723c806773ef897a_big.png"),
        gevent.spawn(downloader, "2.jpg",
                     "https://rpic.douyucdn.cn/live-cover/roomCover/2020/08/13/83df3f8dfa1ade026ad882e76924d926_big.jpg"),
        gevent.spawn(downloader, "3.jpg",
                     "https://rpic.douyucdn.cn/live-cover/roomCover/2021/04/27/761c226e71f16d1797dfde65effe4361_big.png"),
    ])
