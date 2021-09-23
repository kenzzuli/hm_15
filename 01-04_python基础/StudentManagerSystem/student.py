class Student(object):
    """学生类"""

    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        # return f'{self.name}, {self.gender}, {self.tel}'
        return "%s, %s, %s" % (self.name, self.gender, self.tel)


# 测试代码
if __name__ == "__main__":
    stu1 = Student("LIULEI", "male", "110")
    print(stu1)
    stu2 = Student("ken", "female", 120)
    print(stu2)
