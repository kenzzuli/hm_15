# *_* coding=utf-8 *_*
import sys

print(sys.argv)


def readfile(filename):  # 从文件中读取文件内容
    f = open(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
            print("wrong! EOF")
        print(line)


# 脚本从此开始
if len(sys.argv) < 2:  # 如果接收到的命令行参数只有一个（默认只有一个），则什么也不干
    print('No action specified.')
    sys.exit()
if sys.argv[1].startswith('--'):  # 如果接收到的命令行参数以--开始
    option = sys.argv[1][2:]  # 提取选项，选项不包括--，所以去掉前两个字符
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':  # 如果选项是version
        print('Version 1.2')
    elif option == 'help':  # 如果选项是help
        print('''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
  --version : Prints the version number
  --help    : Display this help''')
    else:  # 如果是其他选项
        print('Unknown option.')
    sys.exit()
else:  # sys.argv是一个参数列表， sys.argv[0]表示当前文件，这里对列表切片，遍历列表，读取所有文件的内容
    for filename in sys.argv[1:]:
        readfile(filename)
