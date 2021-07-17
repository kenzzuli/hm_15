import py_compile
# import uncompyle6
import os

# 编译
py_compile.compile(r'send_mail.py', 'send_mail.pyc')

# 反编译   使用命令行操作
# os.system("uncompyle6 -o . %s" % "send_mail.pyc")

# pyc也不安全，
# 1. 直接编辑器打开pyc文件，就能看到里面很多内容（不是乱码）
# 2. 能够反编译
