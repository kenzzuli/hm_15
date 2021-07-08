import socket
import re
import time


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
        # 设为非堵塞
        self.tcp_server_socket.setblocking(False)
        # 用来保存所有的client_socket
        self.client_socket_list = list()

    def serve_forever(self):
        """循环运行web服务器，等待客户端连接并为客户端服务"""
        while True:
            # time.sleep(0.5)
            try:
                # 4.等待客户端连接
                client_socket, _ = self.tcp_server_socket.accept()
            except Exception:
                # print("没有新的客户端到来")
                pass
            else:
                client_socket.setblocking(False)  # 设为非堵塞
                self.client_socket_list.append(client_socket)
            # 这里用copy是因为在遍历一个列表时，不能对列表进行增删操作，否则会遍历不完整。
            # list.copy()是浅拷贝，拷贝的是引用，没有拷贝内容，即两个列表都指向相同的sockets。
            # 协程是单线程，socket等资源只有一份，每个socket也只需关闭一次。
            client_socket_list_back = self.client_socket_list.copy()
            for client_socket in client_socket_list_back:
                try:
                    # 1.接收浏览器发送的请求
                    request = client_socket.recv(1024).decode("utf-8")
                except Exception as e:
                    # print("客户端尚未发送消息")
                    pass
                else:
                    if request:  # 如果不为空，说明是http请求
                        self.handle_request(request, client_socket)
                    else:  # 如果为空，说明浏览器断开连接
                        client_socket.close()
                        self.client_socket_list.remove(client_socket)

            print("client_socket数量为:", len(self.client_socket_list))

    @staticmethod
    def handle_request(request, client_socket):
        """处理浏览器发来的请求"""
        # 2.获取请求的url
        url = re.match(r"^\S+\s(\S+)\s", request).group(1)
        # 3.组装应答头和应答体
        if url == "/":
            url = BASE_DIR + "/index.html"
        else:
            url = BASE_DIR + url

        # 组装
        try:  # 尝试打开文件
            with open(url, mode="rb") as f:  # 必须以rb的形式读取，因为有时传输的是图片
                response_body = f.read()
        except IOError:  # 如果出现异常
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
# 如果ip写127.0.0.1只能由本地连接，这一点非常类似mysql的配置文件中有一行:
# bind_addr = 127.0.0.1，要将这行配置注释掉，其他电脑才能登录该电脑上的mysql。
# SERVER_ADDR = HOST, PORT = "0.0.0.0", 8888
SERVER_ADDR = HOST, PORT = "", 8888

if __name__ == '__main__':
    main()
