import socket
import re

# 配置服务器文件路径
base_dir = "./html"


def handle_client(client_socket):
    """为客户端服务"""
    # 1.接收浏览器发送的请求
    recv_data = client_socket.recv(1024).decode("utf-8")
    # 2.获取请求的url \S+匹配GET POST PUT DEL等  \s匹配空白字符 (\S+)匹配url \s匹配空白字符
    url = re.match(r"^\S+\s(\S+)\s", recv_data).group(1)

    # 3.组装应答头和应答体
    # 如果url为/，则跳转到index.html
    if url == "/":
        url = base_dir + "/index.html"
    else:
        url = base_dir + url
    print("请求的内容为：", url)
    # 请求的内容为： ./html/index.html
    # 请求的内容为： ./html/classic.css
    # 请求的内容为： ./html/images/qt-logo.png
    # 请求的内容为： ./html/images/trolltech-logo.png

    try:
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
    """完成整体的流程控制"""
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置套接字选项，服务器4次挥手后资源能立即释放，这样在下次运行程序时，可以立即绑定端口，不必等待，不然会报错。
    # [Errno 98] address already in use.
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定
    local_addr = "127.0.0.1", 8888
    tcp_server_socket.bind(local_addr)
    # 3.监听
    tcp_server_socket.listen(128)
    while True:
        # 4.等待客户端连接
        client_socket, client_addr = tcp_server_socket.accept()
        # 5.为客户端服务
        handle_client(client_socket)
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
