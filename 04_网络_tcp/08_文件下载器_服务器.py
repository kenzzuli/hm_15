# 文件下载器 服务器端
import socket
import os
from tqdm import tqdm

buffer_size = 1024 * 100  # 100k


def upload(client_socket, file_list, base_dir):
    client_socket.send(str(file_list).encode("utf-8"))
    # 接收客户端发来的下载请求
    while True:
        file_name = client_socket.recv(buffer_size)
        if not file_name:  # 如果为空，说明客户端已经关闭
            return
        file_name = file_name.decode("utf-8")
        if file_name == "quit":  # 如果为quit，说明客户端已经退出下载功能
            return
        print("客户端请求下载 [{}]".format(file_name))
        # 判断服务器是否有客户端请求的文件
        if file_name in file_list:
            total_file_path = os.path.join(base_dir, file_name)
            file_size = os.path.getsize(total_file_path)
            # 向客户端发送文件的大小
            client_socket.send(str(file_size).encode("utf-8"))
            # 从客户端接收一个数据
            _ = client_socket.recv(buffer_size)
            # 开始发送文件数据
            with open(total_file_path, mode="rb") as f:
                total_length = 0
                with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as t:
                    while True:
                        t.set_description("Sending [{}]".format(file_name))
                        content = f.read(buffer_size)
                        client_socket.send(content)
                        t.update(len(content))
                        # 累加发送的数据长度，长度达到总的文件大小时，退出循环
                        total_length += len(content)
                        if total_length == file_size:
                            # 接收客户端的任意数据
                            _ = client_socket.recv(buffer_size)
                            break
                print("[{}] 发送完成".format(file_name))
                return
        else:
            print("客户端请求下载的文件不存在")
            client_socket.send("0".encode("utf-8"))


def download(tcp_client_socket, base_dir):
    # 发送任意一条数据
    tcp_client_socket.send("_".encode("utf-8"))
    # 接收文件名称
    file_name = tcp_client_socket.recv(buffer_size).decode("utf-8")
    if file_name == "quit":
        return
    # 发送任意一条信息
    tcp_client_socket.send("_".encode("utf-8"))
    # 接收文件的大小信息
    file_size = int(tcp_client_socket.recv(buffer_size).decode("utf-8"))
    # 向客户端发送任意一个数据
    tcp_client_socket.send("_".encode("utf-8"))
    # 接收数据，并写入文件
    with open(os.path.join(base_dir, file_name), mode="wb") as f:
        total_length = 0
        with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as t:
            while True:
                t.set_description("Downloading [{}]".format(file_name))
                file_data = tcp_client_socket.recv(buffer_size)
                f.write(file_data)
                t.update(len(file_data))
                total_length += len(file_data)
                if total_length == file_size:
                    # 向客户端发送任意一个数据
                    tcp_client_socket.send("_".encode("utf-8"))
                    break
    print("[{}] 下载完成！".format(file_name))


def file_downloader_server():
    # 创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定地址
    # local_addr = "127.0.0.1", 8888
    local_addr = "10.4.51.50", 8888
    tcp_server_socket.bind(local_addr)
    # 监听
    tcp_server_socket.listen(128)

    while True:
        print("等待客户端连接...")
        client_socket, client_addr = tcp_server_socket.accept()
        print("新的客户端已经连接：%s" % str(client_addr))

        while True:
            # 服务器上的文件列表
            base_dir = os.path.join(os.getcwd(), "cloud_resources")
            if not os.path.exists(base_dir):
                os.mkdir(base_dir)
            file_list = os.listdir(base_dir)

            # 等待客户端选择
            print("等待客户端选择功能...")
            choice = client_socket.recv(buffer_size).decode("utf-8")
            if not choice:
                print("客户端选择 [退出]")
                break
            if choice == "1":
                print("客户端选择 [下载]")
                upload(client_socket, file_list, base_dir)
            elif choice == "2":
                print("客户端选择 [上传]")
                download(client_socket, base_dir)

        client_socket.close()
        print("该连接已经断开")


if __name__ == '__main__':
    file_downloader_server()
