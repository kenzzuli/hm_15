# 循环发送任意数据
import socket


def main():
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 循环发送
    while True:
        msg = input("please input message (quit to quit): ")
        # 地址 (ip, port) 元组 ip是字符串，port是数字
        des_addr = "10.4.51.50", 8888
        udp_socket.sendto(msg.encode("utf-8"), des_addr)
        # 如果输入的是quit，将quit发送出去，然后退出
        if msg == "quit":
            print("您已经下线！")
            break

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
