# 绑定端口并循环发送数据
import socket


def send_smg():
    # 1.实例化socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定端口
    local_addr = "", 4444
    udp_socket.bind(local_addr)
    # 3.发送数据
    des_addr = "10.4.51.50", 8888
    while True:
        msg = input("input message(quit for quit): ")
        udp_socket.sendto(msg.encode(), des_addr)
        if msg == "quit":
            print("您已经下线！")
            break
    # 4.关闭socket
    udp_socket.close()


if __name__ == '__main__':
    send_smg()
