import pickle

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
        try:
            with open("student.data", "rb") as file:
                self.student_list = pickle.load(file)
        except FileNotFoundError:
            print("文件不存在，已经新建！")

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
        with open("student.data", "wb") as file:
            pickle.dump(self.student_list, file)
            print("文件保存成功")


if __name__ == "__main__":
    manager1 = StudentManager()
    manager1.run()
