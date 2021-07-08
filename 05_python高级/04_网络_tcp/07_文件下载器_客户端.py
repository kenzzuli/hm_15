# 文件下载器，客户端
import socket
import os
from tqdm import tqdm

buffer_size = 1024 * 1024 * 100  # 100M


def file_downloader_client():
    base_dir = os.path.join(os.getcwd(), "local_download")
    # 如果文件不存在，创建该文件
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    # 创建tcp socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    # des_addr = "127.0.0.1", 8888
    des_addr = "10.4.51.50", 8888
    tcp_client_socket.connect(des_addr)
    while True:
        # 向服务器发送任意一个数据
        tcp_client_socket.send("hi".encode("utf-8"))
        # 接收服务器的文件列表
        file_list = tcp_client_socket.recv(buffer_size)
        print("服务器文件列表为：{}".format(file_list.decode("utf-8")))
        file_name = input("请输入要下载的文件名称（结束下载请输入quit）：")
        if file_name == "quit":
            break
        # 向服务器发送要下载的文件名
        tcp_client_socket.send(file_name.encode("utf-8"))
        # 接收文件的大小信息
        file_size = tcp_client_socket.recv(buffer_size)
        if int(file_size.decode("utf-8")) > 0:
            # print("[{}] 存在，大小为 [{}]".format(file_name, file_size.decode("utf-8")))
            # 向服务器发送任意一个数据
            tcp_client_socket.send("1111".encode("utf-8"))
            # 接收数据，并写入文件
            with open(os.path.join(base_dir, file_name), mode="wb") as f:
                total_length = 0
                # 使用B作为tqdm的单位
                with tqdm(total=int(file_size.decode("utf-8")), unit="B", unit_scale=True, unit_divisor=1024) as t:
                    while True:
                        t.set_description("Downloading [{}]".format(file_name))
                        file_data = tcp_client_socket.recv(buffer_size)
                        f.write(file_data)
                        t.update(len(file_data))
                        # 累加接收的数据长度，当总长度达到文件大小时，退出循环
                        total_length += len(file_data)
                        if total_length == int(file_size.decode("utf8")):
                            break
            print("[{}] 下载完成！".format(file_name))
        else:
            print("请求的文件不存在，请重新输入！")
            continue
    # 关闭socket
    tcp_client_socket.close()


if __name__ == '__main__':
    file_downloader_client()
