# 循环接收并显示数据
import socket


def receive_smg():
    # 1. 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.1 指定端口
    local_addr = "", 8888
    # 2.2 绑定端口
    udp_socket.bind(local_addr)
    while True:
        # 3. 接收数据
        msg = udp_socket.recvfrom(1024)
        if msg[0].decode("utf-8") == "quit":
            print("对方已下线!")
            break
        # 4. 打印数据
        print("(%s:%s) %s" % (msg[1][0], str(msg[1][1]), msg[0].decode("utf-8")))
    # 5. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    receive_smg()

# (10.4.51.50:57820) hi
# (10.4.51.50:57820) 约吗？
# 对方已下线!
