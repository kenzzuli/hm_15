# *-* coding:utf8 *-*
hello_str = u"你好世界"
print(hello_str)

# 如果不在头部添加编码说明 在Python2中执行 会报错
"""
~/PycharmProjects/13_文件 $ python2 hm_07_python2字符串.py
File "hm_07_python2字符串.py", line 1
SyntaxError: Non-ASCII character '\xe4' in file hm_07_python2字符串.py on line 1, 
but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
"""

# 即使在文件头部添加了编码说明，在遍历包含中文的字符串时，Python2解释器仍会以字节为单位，输出乱码
# 可以在定义字符串时，在字符串的引号前加一个u，告诉Python2解释器，这是一个unicode字符串（utf8是Unicode的一种)
for s in hello_str:
    print(s)

print("_" * 50)
print(hello_str[1:3])
