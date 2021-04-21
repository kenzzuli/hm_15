# tcp客户端
import socket


def tcp_client():
    # 1.创建socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.连接服务器
    dest_addr = "127.0.0.1", 8080
    tcp_socket.connect(dest_addr)
    # 3.接收或发送消息
    msg = "hello"
    tcp_socket.send(msg.encode())
    # 4.关闭socket
    tcp_socket.close()


if __name__ == '__main__':
    tcp_client()
