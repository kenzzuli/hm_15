import socket


def main():
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以使用套接字收发数据
    # 接收用户的输入，并按照bytes编码
    msg = input("please input message: ").encode(encoding="utf-8", errors="strict")
    # 在字符串前加b，也表示按照bytes编码
    msg2 = b"abc"
    # 地址 (ip, port)
    addr = "10.4.51.50", 4444
    udp_socket.sendto(msg, addr)
    udp_socket.sendto(msg2, addr)

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
