# 无法在mac上运行
import socket
import re
import time
import select


class WSGIServer(object):

    def __init__(self, server_addr):
        # 1.创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置套接字选项
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2.绑定
        self.tcp_server_socket.bind(server_addr)
        # 3.监听，并指定队列长度为128
        self.tcp_server_socket.listen(128)
        # 创建一个epoll对象，该对象对应那块共享内存
        self.epoll = select.epoll()
        # 将创建的套接字添加到epoll事件监听中
        # self.epoll.register(self.tcp_server_socket.fileno(), select.EPOLLIN | select.EPOLLET)
        self.epoll.register(self.tcp_server_socket.fileno(), select.EPOLLIN)
        # 创建一个字典，存储client_sockets, fd:client_socket
        self.client_sockets = dict()
        # 创建一个字典，存储addr, 格式为fd:addr
        self.addrs = dict()

    def serve_forever(self):
        """循环运行web服务器，等待客户端连接并为客户端服务"""
        while True:
            # 获取当前事件通知列表，默认会堵塞，直到os检测到数据到来，通过事件通知方式告诉这个程序，才会解堵塞。
            # 返回结果epoll_list格式为[(fd, event), (fd, event), ...]
            # fd是套接字的文件描述符，event是该文件描述符的事件类型
            epoll_list = self.epoll.poll()
            print(epoll_list)

            # 对事件类型进行判断
            for fd, event in epoll_list:
                # 如果是tcp_server_socket被激活
                if fd == self.tcp_server_socket.fileno():
                    client_socket, client_addr = self.tcp_server_socket.accept()
                    # 将client_socket加入epoll事件监听中
                    # self.epoll.register(client_socket.fileno(), select.EPOLLIN | select.EPOLLET)
                    self.epoll.register(client_socket.fileno(), select.EPOLLIN)
                    # 将client_socket放入client_sockets字典中 键为该socket的fd 值为该socket
                    self.client_sockets[client_socket.fileno()] = client_socket
                    # 将client_addr放入addrs字典中 键为该地址的socket的fd，值为该地址
                    self.addrs[client_socket.fileno()] = client_addr
                    info1 = "新的客户端到来 %s" % str(client_addr)
                    info2 = "当前客户端个数为%d" % len(self.client_sockets)
                    print("\033[32m{}\n{}\033[0m".format(info1, info2))

                # 如果是客户端发送数据
                elif event == select.EPOLLIN:
                    # 接收客户端的数据
                    request = self.client_sockets[fd].recv(1024).decode("utf-8")
                    # 如果请求不为空
                    if request:
                        self.handle_request(request, self.client_sockets[fd])
                    # 如果请求为空
                    else:
                        # 关闭套接字
                        self.client_sockets[fd].close()
                        # 从事件监听中去除
                        self.epoll.unregister(fd)
                        # 从client_sockets字典中删去
                        del self.client_sockets[fd]
                        # 从addrs字典中删去
                        info1 = "客户端断开 %s" % str(self.addrs[fd])
                        info2 = "当前客户端个数为%d" % len(self.client_sockets)
                        print("\033[31m{}\n{}\033[0m".format(info1, info2))
                        del self.addrs[fd]
                # todo 有时候会出现event==25，但查询epoll文档发现根本没有25对应的事件类型，以后处理吧 ❌
                elif event == 25:
                    pass

    @staticmethod
    def handle_request(request, client_socket):
        """处理浏览器发来的请求"""
        # 2.获取请求的url
        ret = re.match(r"^\S+\s(\S+)\s", request)
        if ret:  # 有可能ret为None
            url = ret.group(1)
            if url == "/":
                url = "/index.html"

        # 3.组装应答头和应答体
        try:  # 如果ret为None，此时url未指定会出现异常，但放在了try语句中，出现异常会被捕获
            with open(BASE_DIR + url, mode="rb") as f:  # 必须以rb的形式读取，因为有时传输的是图片
                response_body = f.read()
        except Exception:  # 如果出现异常
            response_header = "HTTP/1.1 404 Error \r\n".encode("utf-8")
            response_body = "<h1>404 Page Not Found</h1>".encode("utf-8")
        else:  # 如果没有异常
            response_header = "HTTP/1.1 200 0K \r\n".encode("utf-8")

        finally:  # 无论是否有异常，都组装应答
            # 长连接必须在header中加上content-length，不然浏览器一直在转圈。✅
            response_header += ("Content-Length: %d\r\n\r\n" % len(response_body)).encode("utf-8")
            response = response_header + response_body
        # 4.返回应答
        client_socket.send(response)


def main():
    # 初始化服务器
    httpd = WSGIServer(SERVER_ADDR)
    print("Serving HTTP on {}:{}".format(HOST, PORT))
    # 开始服务
    httpd.serve_forever()


# 配置服务器服务静态资源时的路径
BASE_DIR = "./html"
# 配置服务器地址
# 想让同一局域网内其他电脑访问该网站，ip不能写127.0.0.1, ip要留空或改为0.0.0.0 ✅
# SERVER_ADDR = HOST, PORT = "0.0.0.0", 8888
SERVER_ADDR = HOST, PORT = "", 8888

if __name__ == '__main__':
    main()
