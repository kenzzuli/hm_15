def demo(num, num_list):
    print("函数开始")

    # num = num + num
    num += num

    # 列表变量的相加在赋值，不改变全局变量的引用，仅修改局部变量的引用
    num_list = num_list + num_list

    # 列表变量使用+=不是相加再赋值
    # 而是调用列表的extend方法
    # num_list += num_list
    # num_list.extend(num_list)
    print(num)
    print(num_list)
    print("函数结束")


gl_num = 9
gl_num_list = [1, 2, 3]
demo(gl_num, gl_num_list)
print(gl_num)
print(gl_num_list)
