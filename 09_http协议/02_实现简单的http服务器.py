import socket


def handle_client(client_socket):
    """为客户端服务"""
    # 1.接收浏览器发送的请求
    recv_data = client_socket.recv(1024).decode("utf-8")
    # 2.按行打印请求头
    request_header = recv_data.splitlines()
    for line in request_header:
        print(line)

    # 3.组装应答头和应答体
    response_header = "HTTP/1.1 200 0K \r\n"
    response_header += "\r\n"  # 用空白行将应答头和应答体分割
    response_body = "<h1>hello</h1>"
    response = response_header + response_body
    # 4.返回应答
    client_socket.send(response.encode("utf-8"))
    # 5.关闭套接字
    client_socket.close()


def main():
    """完成整体的流程控制"""
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置服务器先close，即服务器4次挥手后资源能立即释放，这样在下次运行程序时，可以立即绑定端口，不必等待，不然会报错。
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
