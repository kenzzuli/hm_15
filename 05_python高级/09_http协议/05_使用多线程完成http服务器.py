import socket
import re
from threading import Thread
import threading


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

    def serve_forever(self):
        """循环运行web服务器，等待客户端连接并为客户端服务"""
        while True:
            # 4.等待客户端连接
            client_socket, client_addr = self.tcp_server_socket.accept()
            # 5.使用多线程为客户端服务
            t = Thread(target=self.handle_client, args=(client_socket,))
            t.start()
            # 多线程共用一个套接字，因此不能在主线程中关闭套接字，要等子线程执行完代码后关闭套接字，否则会报错。
            # OSError: [Errno 9] Bad file descriptor
            # client_socket.close()

    @staticmethod
    def handle_client(client_socket):
        """为一个客户端服务"""
        t = threading.currentThread()
        print("Thread ID: {}\tThread Name: {}".format(t.ident, t.getName()))
        # 1.接收浏览器发送的请求
        recv_data = client_socket.recv(1024).decode("utf-8")
        # 2.获取请求的url \S+匹配GET POST PUT DEL等  \s匹配空白字符 (\S+)匹配url \s匹配空白字符
        url = re.match(r"^\S+\s(\S+)\s", recv_data).group(1)
        # 3.组装应答头和应答体
        # 设置默认页面，如果url为/，则跳转到index.html
        if url == "/":
            url = BASE_DIR + "/index.html"
        else:
            url = BASE_DIR + url

        # 组装
        try:  # 尝试打开文件
            with open(url, mode="rb") as f:  # 必须以rb的形式读取，因为有时传输的是图片
                response_body = f.read()
        except IOError:  # 如果出现异常
            response_header = "HTTP/1.1 404 Error \r\n\r\n".encode("utf-8")
            response_body = "<h1>404 Page Not Found</h1>".encode("utf-8")
        else:  # 如果没有异常
            response_header = "HTTP/1.1 200 0K \r\n\r\n".encode("utf-8")
        finally:  # 无论是否有异常，都组装应答
            response = response_header + response_body
        # 4.返回应答
        client_socket.send(response)
        # 5.关闭套接字
        client_socket.close()


def main():
    # 初始化服务器
    httpd = WSGIServer(SERVER_ADDR)
    print("Serving HTTP on {}:{}".format(HOST, PORT))
    # 开始服务
    httpd.serve_forever()


# 配置服务器服务静态资源时的路径
BASE_DIR = "./html"
# 配置服务器地址
# SERVER_ADDR = HOST, PORT = "127.0.0.1", 8888
# 想让同一局域网内其他电脑访问该网站，要把网址改为0.0.0.0
SERVER_ADDR = HOST, PORT = "0.0.0.0", 8888
if __name__ == '__main__':
    main()
