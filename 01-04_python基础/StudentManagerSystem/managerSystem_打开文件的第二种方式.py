# 这种加载文件的方式，要比教程上的要好，不会出现空白文件读取错误
from student import *


class StudentManager(object):
    """学生管理类"""

    def __init__(self):
        self.student_list = []

    # 主程序入口
    def run(self):
        self.load_data()
        while True:
            StudentManager.show_menu()
            try:
                input_num = int(input("请输入要进行的操作："))
            except Exception:
                print("请输入数字!!!")
                continue
            else:
                if input_num == 1:
                    self.add_student()
                elif input_num == 2:
                    self.del_student()
                elif input_num == 3:
                    self.modify_student()
                elif input_num == 4:
                    self.search_student()
                elif input_num == 5:
                    self.show_all_student()
                elif input_num == 6:
                    self.save_data()
                else:
                    break

    def load_data(self):
        # 1> 打开文件
        try:
            # 如果文件存在，就以只读模式打开
            file = open("stu_data.txt", "r")
        except:
            print("本地文件不存在")
        else:
            # 2> 如果文件存在，读入数据
            # 使用eval函数，将字符串转换成列表
            tmp_list = eval(file.read())
            # 使用列表生成式，生成以学生对象为元素的列表
            self.student_list = [Student(stu["name"], stu["gender"], stu["tel"]) for stu in tmp_list]
            # 3> 关闭文件
            file.close()


    @staticmethod
    def show_menu():
        print('请选择如下功能-----------------')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')

    def add_student(self):
        name = input("请输入学生姓名：")
        gender = input("请输入学生性别：")
        tel = input("请输入学生手机号：")
        stu = Student(name, gender, tel)
        self.student_list.append(stu)
        print("已经添加该学生信息：")
        print(stu)

    def del_student(self):
        self.show_all_student()
        name = input("请输入要删除的学生姓名：")
        for stu in self.student_list:
            if stu.name == name:
                self.student_list.remove(stu)
                print("已经删除该学生信息：")
                print(stu)
                break
        else:
            print("没有这个学生")

    def modify_student(self):
        name = input("请输入要修改的学生姓名：")
        for stu in self.student_list:
            if stu.name == name:
                new_name = input("请输入新的姓名，直接回车表示不修改：")
                if len(new_name) > 0:
                    stu.name = new_name
                new_gender = input("请输入新的性别，直接回车表示不修改：")
                if len(new_gender) > 0:
                    stu.gender = new_gender
                new_tel = input("请输入新的手机号，直接回车表示不修改：")
                if len(new_tel) > 0:
                    stu.tel = new_tel
                print("修改后的信息为：")
                print(stu)
                break
        else:
            print("没有这个学生")

    def search_student(self):
        name = input("请输入学生姓名：")
        for stu in self.student_list:
            if stu.name == name:
                print(stu)
                break
        else:
            print("没有这位学生")

    def show_all_student(self):
        for stu in self.student_list:
            print(stu)

    def save_data(self):
        # 1> 打开文件
        file = open("stu_data.txt", "w")
        # 2> 将学生数据写入文件
        # 注意，写入的学生数据不能是学生对象的内存地址，需要把学生数据，转换成以字典为元素的列表再存储
        # 列表生成式
        # 实例名.__dict__ 返回实例属性和值组成的字典
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        # 文件内数据要求为字符串类型，需要先把列表转成字符串才能写入
        file.write(str(new_list))
        # 3> 关闭文件
        file.close()


if __name__ == "__main__":
    manager1 = StudentManager()
    manager1.run()
