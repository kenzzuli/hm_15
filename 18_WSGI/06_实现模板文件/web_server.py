import socket
import re
from multiprocessing import Process
from dynamic import mini_frame


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
            # 5.使用多进程为客户端服务
            p = Process(target=self.handle_client, args=(client_socket,))
            p.start()
            # linux中一切皆文件。套接字也是一个文件。
            # 创建子进程时，子进程会复制父进程的资源，如套接字。
            # 类似硬链接，父进程子进程的套接字都指向同一个文件描述符，父进程调用close方法只是删去了一个链接，子进程中的套接字仍然指向该文件描述符
            # 只有子进程和父进程都调用close方法，套接字才真正被释放。
            # 这一句必须加上，不然浏览器一直在等待接收，在转圈。
            client_socket.close()

    def handle_client(self, client_socket):
        """为一个客户端服务"""
        # 1.接收浏览器发送的请求
        env = dict()
        recv_data = client_socket.recv(1024).decode("utf-8")
        # 按行分割，方便字典存储
        lines = recv_data.splitlines()
        for line in lines:
            ret = line.split(": ")
            if len(ret) == 2:
                (key, value) = line.split(": ")
                env[key] = value
        # print(env)
        # 2.获取请求的url \S+匹配GET POST PUT DEL等  \s匹配空白字符 (\S+)匹配url \s匹配空白字符
        ret = re.match(r"^\S+\s(\S+)\s", lines[0])
        if ret:
            url = ret.group(1)
        else:
            print(ret)
            print(lines)
        # 3.组装应答头和应答体
        # 3.1 如果浏览器请求的是动态资源
        print(url)
        if url.endswith(".py"):
            # 框架中的application返回body
            env['url'] = url
            response_body = mini_frame.application(env, self.set_response_header)
            if isinstance(response_body, str):
                response_body = response_body.encode("utf-8")
            # 拼接header
            response_header = "HTTP/1.1 %s\r\n" % self.status_code
            for i in self.headers:
                response_header += "%s:%s\r\n" % (i[0], i[1])
            response_header += "\r\n"
            response_header = response_header.encode("utf-8")

        # 3.2 如果浏览器请求的是静态资源，如html/css/js/png/gif等
        else:
            # 设置默认页面，如果url为/，则跳转到index.html
            if url == "/":
                url = "/index.html"
            # 组装
            try:  # 尝试打开文件
                with open(BASE_DIR + url, mode="rb") as f:  # 必须以rb的形式读取，因为有时传输的是图片
                    response_body = f.read()
            except Exception:  # 如果出现异常
                response_header = "HTTP/1.1 404 Error \r\n\r\n".encode("utf-8")
                response_body = "<h1>404 Page Not Found</h1>".encode("utf-8")
            else:  # 如果没有异常
                response_header = "HTTP/1.1 200 0K \r\n\r\n".encode("utf-8")
        # 拼接应答
        response = response_header + response_body
        # 4.返回应答
        client_socket.send(response)
        # 5.关闭套接字
        client_socket.close()

    def set_response_header(self, status_code, headers):
        self.status_code = status_code
        # 在服务器中增加server信息，而不是在框架中增加
        self.headers = [('server', 'mini_frame v1.0')]
        self.headers += headers


def main():
    # 初始化服务器
    httpd = WSGIServer(SERVER_ADDR)
    print("Serving HTTP on {}:{}".format(HOST, PORT))
    # 开始服务
    httpd.serve_forever()


# 配置服务器服务静态资源时的路径
BASE_DIR = "./static"
# 配置服务器地址
# SERVER_ADDR = HOST, PORT = "127.0.0.1", 8888
# 想让同一局域网内其他电脑访问该网站，要把网址改为0.0.0.0
SERVER_ADDR = HOST, PORT = "0.0.0.0", 8888
if __name__ == '__main__':
    main()
