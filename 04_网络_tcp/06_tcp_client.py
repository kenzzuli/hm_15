# tcp客户端
# 可多次发送消息
import socket


def tcp_client():
    # 1.创建socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.连接服务器
    local_addr = "127.0.0.1", 3333
    tcp_socket.bind(local_addr)
    dest_addr = "127.0.0.1", 8888
    tcp_socket.connect(dest_addr)
    # 3.接收或发送消息
    while True:
        msg = input("消息：")
        tcp_socket.send(msg.encode())
        rcv_msg = tcp_socket.recv(1024)
        print(rcv_msg.decode())
        if msg == "quit":
            break
    # 4.关闭socket
    tcp_socket.close()


if __name__ == '__main__':
    tcp_client()
