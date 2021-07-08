import pickle

# 将本地文件加载为列表
try:
    with open('card_list.txt', 'rb') as f:
        card_list = pickle.load(f)
        # print(card_list)
        print("本地文件已加载")
except FileNotFoundError:
    card_list = []


def dump_card():
    """将列表保存到本地"""
    with open('card_list.txt', 'wb') as f:
        pickle.dump(card_list, f)
        print("名片已保存到本地")


def show_menu():
    """
    显示功能菜单
    :return: null
    """
    print("*" * 50)
    print("欢迎使用【名片管理系统】V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入email：")

    # 2.使用用户输入的信息建立一个名片字典
    temp_dic = {"name": name_str,
                "phone": phone_str,
                "qq": qq_str,
                "email": email_str}

    # 3.将名片添加到字典中
    card_list.append(temp_dic)
    print(card_list)

    # 4.提示用户名片添加成功
    print("新增%s的名片成功!" % name_str)

    # 5.将列表更新到本地
    dump_card()


def show_table_head():
    """打印表头"""

    # 我第一遍写的
    print("%s%s%s%s" % ("name".ljust(12),
                        "phone".ljust(12),
                        "qq".ljust(12),
                        "email".ljust(12)))

    # 视频写的
    # for key in ["Name", "Phone", "QQ", "Email"]:
    #     print(key, end="\t\t\t")
    # print("")

    # 打印分割线
    print("-" * 50)


def show_table_tail():
    """打印表尾的分割线"""
    print("-" * 50)


def show_table_body(card_dict):
    """打印表体，每次一行"""

    # 我第一遍写的
    # print(card_dict["name"].ljust(12), end="", )
    # print(card_dict["phone"].ljust(12), end="")
    # print(card_dict["qq"].ljust(12), end="")
    # print(card_dict["email"].ljust(12))

    # 我第二遍写的
    print("%s%s%s%s" % (card_dict["name"].ljust(12),
                        card_dict["phone"].ljust(12),
                        card_dict["qq"].ljust(12),
                        card_dict["email"].ljust(12)))

    # 视频写的
    # print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
    #                                       card_dict["phone"],
    #                                       card_dict["qq"],
    #                                       card_dict["email"]))


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户并返回
    if len(card_list) == 0:
        print("当前没有任何名片，请返回新增名片！")

        # return 可以返回一个函数的执行结果，也可以什么都不返回
        # return 下方的代码不会被执行
        # return 语句执行后，程序会返回到调用函数的位置
        return

    show_table_head()

    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        show_table_body(card_dict)

    show_table_tail()


def input_card_info(card_value, message):
    """
    输入名片信息

    :param card_value: 字典中原有的值
    :param message: 输入提示信息
    :return: 如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    # 提示用户输入信息
    result_str = input(message)
    # 针对用户的输入进行判断，如果输入了内容，则返回输入内容
    if len(result_str) > 0:
        return result_str
    # 如果没有输入内容，则返回原来的值
    else:
        return card_value


def deal_card(card_dict):
    """处理查找到的名片

    :param card_dict: 查找到的名片字典
    """
    while True:
        action_str = input("请输入对名片的操作   "
                           "[1]：修改   [2]：删除   [0]：返回上级菜单：")
        if action_str in ["1", "2", "0"]:
            # 修改名片的功能
            if action_str == "1":
                card_dict["name"] = input_card_info(card_dict["name"], "请输入新的姓名，如无需更改，请直接回车：")
                card_dict["phone"] = input_card_info(card_dict["phone"], "请输入新的手机号，如无需更改，请直接回车：")
                card_dict["qq"] = input_card_info(card_dict["qq"], "请输入新的QQ，如无需更改，请直接回车：")
                card_dict["email"] = input_card_info(card_dict["email"], "请输入新的Email，如无需修改，请直接回车：")

                # 我第一遍写的
                # new_email_str = input("请输入新的email，如无需更改，请直接回车：")
                # if new_email_str != "":
                #     card_dict["email"] = new_email_str
                print("%s的信息修改成功" % card_dict["name"])
                # 将新列表保存到本地
                dump_card()
                break
            # 删除名片的功能
            elif action_str == "2":
                card_list.remove(card_dict)
                print("%s的名片已经删除" % card_dict["name"])
                # 将新列表保存到本地
                dump_card()
                break
            elif action_str == "0":
                break
        else:
            print("输入错误，请重新输入")


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要查找的姓名：")

    # 2.遍历列表中的名片，查询要搜索的姓名
    for card_dict in card_list:
        # 如果找到，打印该名片
        if card_dict["name"] == find_name:
            show_table_head()

            show_table_body(card_dict)

            show_table_tail()

            # 针对找到的名片记录执行修改和删除操作
            deal_card(card_dict)

            # 找到后直接退出循环，不再继续搜索
            break

    # 如果没有找到，需要提示用户
    else:
        print("抱歉，没有找到%s的名片" % find_name)
