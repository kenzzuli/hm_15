# 自己实现进度条刷新，确定进度条完整
from multiprocessing import Manager, Pool
import os


def copy(q, file_name, source_folder, dest_folder):
    with open(os.path.join(source_folder, file_name), mode="rb") as fin:
        with open(os.path.join(dest_folder, file_name), mode="wb") as fout:
            while True:
                content = fin.read(1024)
                if content:
                    fout.write(content)
                else:
                    break
    q.put(file_name)


def get_source_and_dest_folder():
    # 获取源文件夹
    while True:
        source_folder = input("请输入源文件夹: ")
        if not os.path.exists(source_folder):
            print("源文件夹不存在，请重新输入！")
            continue
        else:
            break

    # 获取目标文件夹
    dest_folder = input("请输入目标文件夹: ")
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)

    return source_folder, dest_folder


if __name__ == '__main__':
    source_folder, dest_folder = get_source_and_dest_folder()
    # 获取源文件夹中的文件
    file_list = os.listdir(source_folder)
    # 创建进程池
    po = Pool(3)
    # 创建Queue
    q = Manager().Queue()
    # 向进程池添加任务
    for file in file_list:
        po.apply_async(copy, (q, file, source_folder, dest_folder))

    po.close()  # 关闭进程池，不再接收新的任务

    # 手动实现进度条

    # 方法1
    # 由于多进程，循环中两次使用qsize()获取的值可能不一样，导致进度条显示不完整，所以要在if判断中再加一次打印信息
    # while True:
    #     # \r每次回到行首
    #     print("\rCopying %.2f%%" % (q.qsize() * 100.0 / len(file_list)), end="")
    #     if q.qsize() == len(file_list):
    #         # 这里还是要加上输出，不然进度条不完整
    #         print("\rCopying %.2f%%" % (q.qsize() * 100.0 / len(file_list)))
    #         break
    while True:
        copied_file_num = q.qsize()
        print("\rCopying %.2f%%" % (copied_file_num * 100.0 / len(file_list)), end="")
        if copied_file_num == len(file_list):
            print()  # 加一个换行
            break

    # 方法2
    # 每次循环中，打印时的copied_file_num和if判断中的copied_file_num一样，不会变化，进度条能完整显示
    # copied_file_num = 0
    # while True:
    #     q.get()
    #     copied_file_num += 1
    #     print("\rCopying %.2f%%" % (copied_file_num / len(file_list) * 100), end="")
    #     if copied_file_num == len(file_list):
    #         print("")  # 加一个换行
    #         break
    print("拷贝结束")
