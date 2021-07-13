import tarfile
import zipfile
import rarfile
import os
import sys


def uncompress(compressed_file_path, dest_dir):
    """解压各种类型的压缩包
    :param compressed_file_path: 你要解压的压缩包文件的路径
    :param dest_dir: 你要解压到的目标路径
    """
    file_name, file_type = os.path.splitext(compressed_file_path)

    try:
        if file_type == '.zip':
            zip_file = zipfile.ZipFile(compressed_file_path)
            for names in zip_file.namelist():
                zip_file.extract(names, dest_dir)
            zip_file.close()

        elif file_type == '.rar':
            rar = rarfile.RarFile(compressed_file_path)
            os.chdir(dest_dir)
            rar.extractall()
            rar.close()

        else:
            # file_type == '.tgz' or file_type == '.tar' or file_type == '.gz'
            # Python自带tarfile模块
            tar = tarfile.open(name=compressed_file_path)
            for name in tar.getnames():
                tar.extract(name, dest_dir)
            tar.close()

    except Exception as e:
        print("[{}]解压失败".format(compressed_file_path))
        print(e)

    print("[{}]解压成功".format(compressed_file_path))


def get_all_file_list(dir):
    # 递归获取一个路径下的所有文件
    total_file_list = list()
    file_list = os.listdir(dir)
    for file in file_list:
        file_path = os.path.join(dir, file)
        if os.path.isfile(file_path):
            total_file_list.append(file_path)
        else:
            total_file_list += get_all_file_list(file_path)
    return total_file_list


def run():
    print(sys.argv)
    if len(sys.argv) < 4:
        print("使用方法: '\n'uncompress -i source_dir/source_file [-o dest_dir]")
    base_dir = sys.argv[1]
    compressed_files_path = sys.argv[2]
    dest_dir = sys.argv[3] if len(sys.argv) == 4 else "./"
    os.chdir(base_dir)

    # 路径转换
    compressed_files_path = os.path.abspath(compressed_files_path) if compressed_files_path.startswith(
        ".") else compressed_files_path
    dest_dir = os.path.abspath(dest_dir) if dest_dir.startswith(".") else dest_dir
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    # print(compressed_files_path)
    # print(dest_dir)
    if os.path.isfile(compressed_files_path):
        uncompress(compressed_files_path, dest_dir)
    else:
        file_list = get_all_file_list(compressed_files_path)
        for file in file_list:
            if file.endswith((".rar", ".zip", ".tar", ".gz", ".tgz")):
                uncompress(file, dest_dir)
            else:
                continue


if __name__ == '__main__':
    run()
