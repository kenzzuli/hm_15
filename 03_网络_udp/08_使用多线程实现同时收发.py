# 使用多线程，实现同时收发
# 比较粗糙 哈哈哈哈哈
import threading
import socket

# 创建socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 指定源地址和目标地址
local_addr = "127.0.0.1", 4444
des_addr = "127.0.0.1", 8888
udp_socket.bind(local_addr)


def receive_msg():
    while True:
        recv_data = udp_socket.recvfrom(1024)
        if recv_data[0].decode() == "quit":
            print("\n对方已经下线！\n自己：", end="")
            break
        print("\n对方：" + recv_data[0].decode() + "\n自己：", end="")


def send_msg():
    while True:
        msg = input("自己：")
        udp_socket.sendto(msg.encode(), des_addr)
        if msg == "quit":
            print("您已经下线！")
            break


def chat():
    # 欢迎界面
    print("*" * 50)
    print("欢迎使用UDP聊天工具，输入quit退出！")
    print("*" * 50)
    t1 = threading.Thread(target=receive_msg)
    t2 = threading.Thread(target=send_msg)
    t1.start()
    t2.start()


if __name__ == '__main__':
    chat()

# **************************************************
# 欢迎使用UDP聊天工具，输入quit退出！
# **************************************************
# 自己：你好啊
# 自己：
# 对方：你也好啊
# 自己：
# 对方：你叫什么
# 自己：我叫ken
# 自己：
# 对方：我叫peter
# 自己：
# 对方：很高兴认识你
# 自己：
# 对方：约不约？
# 自己：好啊
# 自己：约啊
# 自己：如家？
# 自己：
# 对方：ok
# 自己：
# 对方：不见不散
# 自己：
# 对方：bye
# 自己：bye
# 自己：quit
# 您已经下线！
#
# 对方已经下线！
