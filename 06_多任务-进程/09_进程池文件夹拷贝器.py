# 仅可以拷贝文件夹中的文件，如果文件夹中嵌套文件夹，就不行了，要递归实现
# 这里就不重复造轮子了
# 如果进程池里的进程产生异常，主进程是看不到的
from multiprocessing import Manager, Pool
import os
from tqdm import tqdm


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
    # 使用进度条
    with tqdm(total=len(file_list)) as t:
        while True:
            t.set_description("Copying")
            # 将进度条更新到某个位置
            t.n = q.qsize()
            t.refresh()  # 刷新
            if q.qsize() == len(file_list):
                t.n = q.qsize()  # 由于多进程，这里如果刷新进度条，会出现进度条没走完的情况
                t.refresh()  # 也要刷新
                break
    po.close()  # 关闭进程池，不再接收新的任务
    po.join()  # 让主进程等待进程池的任务全部执行结束后再向下执行
    print("拷贝结束")
