# 文件下载器，客户端
import socket
import os
from tqdm import tqdm

buffer_size = 1024 * 100  # 100k


def download(tcp_client_socket, base_dir):
    # 向服务器发送 下载 选择
    tcp_client_socket.send("1".encode("utf-8"))
    # 接收服务器的文件列表
    file_list = tcp_client_socket.recv(buffer_size)
    while True:
        print("服务器文件列表为：{}".format(file_list.decode("utf-8")))
        file_name = input("请输入要下载的文件名称（结束下载请输入quit）：")
        if file_name == "quit":  # 如果客户端选择quit，则将quit发送给服务器
            tcp_client_socket.send("quit".encode("utf-8"))
            break
        # 向服务器发送要下载的文件名
        tcp_client_socket.send(file_name.encode("utf-8"))
        # 接收文件的大小信息
        file_size = tcp_client_socket.recv(buffer_size)
        if int(file_size.decode("utf-8")) > 0:
            # 向服务器发送任意一个数据
            tcp_client_socket.send("_".encode("utf-8"))
            # 接收数据，并写入文件
            with open(os.path.join(base_dir, file_name), mode="wb") as f:
                total_length = 0
                with tqdm(total=int(file_size.decode("utf-8")), unit="B", unit_scale=True, unit_divisor=1024) as t:
                    while True:
                        t.set_description("Downloading [{}]".format(file_name))
                        file_data = tcp_client_socket.recv(buffer_size)
                        f.write(file_data)
                        t.update(len(file_data))
                        total_length += len(file_data)
                        if total_length == int(file_size.decode("utf-8")):
                            # 向服务器发送任意数据
                            tcp_client_socket.send("_".encode("utf-8"))
                            break
            print("[{}] 下载完成！".format(file_name))
            return
        else:
            print("请求的文件不存在，请重新输入！")


def upload(tcp_client_socket, base_dir):
    # 向服务器发送 上传 选择
    tcp_client_socket.send("2".encode("utf-8"))
    # 接收任意一条数据
    _ = tcp_client_socket.recv(buffer_size)
    while True:
        # 获取本地资源列表
        local_file_list = os.listdir(base_dir)
        print("本地文件列表为：" + str(local_file_list))
        file_name = input("请输入要上传的文件名称（结束上传请输入quit）：")
        if file_name == "quit":
            tcp_client_socket.send("quit".encode("utf-8"))
            return
        elif file_name in local_file_list:
            # 向服务器发送文件名称
            tcp_client_socket.send(file_name.encode("utf-8"))
            total_file_path = os.path.join(base_dir, file_name)
            file_size = os.path.getsize(total_file_path)
            # 接收任意一条数据
            _ = tcp_client_socket.recv(buffer_size)
            # 向服务器发送文件的大小
            tcp_client_socket.send(str(file_size).encode("utf-8"))
            # 接收任意一个数据
            _ = tcp_client_socket.recv(buffer_size)
            # 开始发送文件数据
            with open(total_file_path, mode="rb") as f:
                total_length = 0
                with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as t:
                    while True:
                        t.set_description("Sending [{}]".format(file_name))
                        content = f.read(buffer_size)
                        tcp_client_socket.send(content)
                        t.update(len(content))
                        # 累加发送的数据长度，长度达到总的文件大小时，退出循环
                        total_length += len(content)
                        if total_length == file_size:
                            # 接收服务器任意一个数据
                            _ = tcp_client_socket.recv(buffer_size)
                            break
                print("{}发送完成".format(file_name))
                return
        else:
            print("上传的文件不存在")
            continue


def file_downloader_client():
    # 本地资源路径
    base_dir = os.path.join(os.getcwd(), "local_download")
    # 如果目录不存在，创建该目录
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    # 创建tcp socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    ip = input("请输入对方ip：")
    port = int(input("请输入对方端口："))
    des_addr = ip, port
    # des_addr = "10.4.51.50", 8888
    tcp_client_socket.connect(des_addr)
    while True:
        choice = input("请选择功能:[1]下载 [2]上传 [3]退出  ")
        if choice == "1":
            download(tcp_client_socket, base_dir)
        elif choice == "2":
            upload(tcp_client_socket, base_dir)
        elif choice == "3":
            break
        else:
            print("输入错误，请重新输入！")

    # 关闭socket
    tcp_client_socket.close()


if __name__ == '__main__':
    file_downloader_client()
