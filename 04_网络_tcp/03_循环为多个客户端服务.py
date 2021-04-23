# 循环为多个客户端服务
import socket


def tcp_server():
    # 创建socket
    tcp_tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定ip
    local_addr = "127.0.0.1", 8888
    tcp_tcp_server_socket.bind(local_addr)

    # 监听(让socket由主动变为被动)
    tcp_tcp_server_socket.listen(128)
    while True:
        print("等待客户端连接...")
        # 默认先阻塞，直到有客户端连接
        # 如果有客户端来连接服务器，就会产生一个新的socket专门为这个客户端服务
        client_socket, client_addr = tcp_tcp_server_socket.accept()
        print("新的客户端已经到来：%s" % str(client_addr))

        # 默认先阻塞，直到收到数据
        # 接收数据
        recv_data = client_socket.recv(1024)  # 每次最多接收1024个bytes
        print("接收到的数据为：" + recv_data.decode())

        # 发送数据
        client_socket.send("ok".encode())

        # 关闭socket
        client_socket.close()
        print("服务完毕")
    tcp_tcp_server_socket.close()


if __name__ == '__main__':
    tcp_server()


# 等待客户端连接...
# 新的客户端已经到来：('127.0.0.1', 3333)
# 接收到的数据为：hello
# 服务完毕
# 等待客户端连接...
# 新的客户端已经到来：('127.0.0.1', 4444)
# 接收到的数据为：hello
# 服务完毕
# 等待客户端连接...