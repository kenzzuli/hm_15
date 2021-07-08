# 绑定端口，接收数据
import socket


def receive_smg():
    # 1. 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.1 指定端口
    local_addr = "", 8888
    # 2.2 绑定端口
    udp_socket.bind(local_addr)
    # 3. 接收数据
    msg = udp_socket.recvfrom(1024)
    # 4. 打印数据
    # print(type(msg))  # 收到的信息是一个元组 (data, source_addr)
    # <class 'tuple'>
    # print(msg)
    # (b'fuck you', ('10.4.51.50', 61216))
    # print(msg[0].decode(encoding="utf-8"))  # 对data解码成str
    # fuck you
    # print(msg[1])  # 查看source_addr
    # ('10.4.51.50', 61216)
    print("(%s:%s) %s" % (msg[1][0], str(msg[1][1]), msg[0].decode("utf-8")))
    # (10.4.51.50:61216) 你好
    # 5. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    receive_smg()
