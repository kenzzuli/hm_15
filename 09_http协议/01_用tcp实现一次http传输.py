# 模拟服务器与浏览器通信
# 创建tcp服务器，使用浏览器向tcp服务器发送请求，tcp服务器向浏览器返回应答。
# 使用i来记录该网页被访问的次数，并在浏览器网页上显示
import socket


def tcp_server():
    i = 0
    # 创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置服务器先close，即服务器4次挥手后资源能立即释放，这样在下次运行程序时，可以立即绑定端口，不必等待。
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定ip
    local_addr = "127.0.0.1", 8888
    tcp_server_socket.bind(local_addr)

    # 监听(让socket由主动变为被动)
    tcp_server_socket.listen(128)
    # i 用来标记访问次数
    i = 0
    while True:
        # 默认先阻塞，直到有客户端连接
        # 如果有客户端来连接服务器，就会产生一个新的socket专门为这个客户端服务
        client_socket, client_addr = tcp_server_socket.accept()
        print(client_addr)
        # ('127.0.0.1', 4444)
        print(client_socket)
        # <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8888), raddr=('127.0.0.1', 4444)>

        # 默认先阻塞，直到收到数据
        # 接收数据
        recv_data = client_socket.recv(1024)  # 每次最多接收1024个bytes
        print("请求头为：\n" + recv_data.decode())
        # 请求头为：
        # GET / HTTP/1.1
        # Host: 127.0.0.1:8888
        # Connection: keep-alive
        # Cache-Control: max-age=0
        # sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
        # sec-ch-ua-mobile: ?0
        # Upgrade-Insecure-Requests: 1
        # User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36
        # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        # Sec-Fetch-Site: none
        # Sec-Fetch-Mode: navigate
        # Sec-Fetch-User: ?1
        # Sec-Fetch-Dest: document
        # Accept-Encoding: gzip, deflate, br
        # Accept-Language: en,en-US;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6

        # 发送数据 包含应答头和应答体
        send_data = "HTTP/1.1 200 0K\r\n\r\n<h1>{} times </h1>".format(i // 2)  # 这里i除以2是因为每次浏览器都发送了两次请求
        client_socket.send(send_data.encode())
        i += 1
        print(i)
        # 关闭socket
        client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    tcp_server()
