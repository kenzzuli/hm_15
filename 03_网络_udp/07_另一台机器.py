# 使用同一个套接字收发数据
import socket


def recv_and_send():
    # 欢迎信息
    print("*" * 50)
    print("欢迎使用UDP聊天工具，输入quit退出。")
    print("*" * 50)
    # 创建
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    local_addr = "127.0.0.1", 8888
    udp_socket.bind(local_addr)
    # 目标端口
    des_addr = "127.0.0.1", 4444  # 本地主机
    # 发送
    while True:
        # 接收
        receive_msg = udp_socket.recvfrom(1024)  # 每次收到的最大字节数
        print("{: >50} A".format(receive_msg[0].decode()))
        if receive_msg[0].decode() == "quit":
            print("对方已经下线！")
            break
        # 发送
        msg = input("B ")
        udp_socket.sendto(msg.encode(), des_addr)
        if msg == "quit":
            print("您已经下线！")
            break


if __name__ == '__main__':
    recv_and_send()
