def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 学生的姓名
    :param gender: True 男生 False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("[%s]%s是%s" % (title, name, gender_text))


print_info("ken")
print_info("karen", gender=False)
print_info("peter", title="monitor")
