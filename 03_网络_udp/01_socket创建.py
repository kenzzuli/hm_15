import socket


def main():
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以使用套接字收发数据
    # 接收用户的输入，并转成bytes类型
    msg = input("please input message: ").encode(encoding="utf-8", errors="strict")
    # 在字符串前加b，也表示bytes类型
    msg2 = b"abc"
    # 地址 (ip, port) 元组 ip是字符串，port是数字
    addr = "10.4.51.50", 4444
    udp_socket.sendto(msg, addr)
    udp_socket.sendto(msg2, addr)

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
