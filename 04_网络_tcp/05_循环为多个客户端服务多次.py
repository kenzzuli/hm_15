# 循环为多个客户端服务多次
import socket


def tcp_server():
    # 创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定ip
    local_addr = "127.0.0.1", 8888
    tcp_server_socket.bind(local_addr)

    # 监听(让socket由主动变为被动)
    tcp_server_socket.listen(128)
    # 循环为多个客户端服务
    while True:
        print("等待客户端连接...")
        # 默认先阻塞，直到有客户端连接
        # 如果有客户端来连接服务器，就会产生一个新的socket专门为这个客户端服务
        client_socket, client_addr = tcp_server_socket.accept()
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("新的客户端已经到来：%s" % str(client_addr))

        # 循环为单个客户端服务多次
        while True:
            # 默认先阻塞，直到收到数据
            # 接收数据
            recv_data = client_socket.recv(1024)  # 每次最多接收1024个bytes
            # 当客户端关闭socket时，服务器收到的数据为空
            if not recv_data:  # 等价于 if len(字典、元组、列表) == 0:
                # 当字典、元组、列表、字符串元素为空时，判断为False
                break
            else:
                print("接收到的数据为：" + recv_data.decode())
                # 发送数据
                client_socket.send("ok".encode())

        # 关闭socket
        client_socket.close()
        print("服务完毕")
    tcp_server_socket.close()


if __name__ == '__main__':
    tcp_server()
