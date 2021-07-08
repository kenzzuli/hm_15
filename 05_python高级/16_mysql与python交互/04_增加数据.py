from pymysql import *


class JD(object):
    def __init__(self):
        self.conn = connect(host="localhost", user="root", password="liulei123", database="jing_dong", port=3306,
                            charset="utf8")
        self.cursor = self.conn.cursor()
        self.tables = ["goods", "goods_brands", "goods_cates"]

    def __del__(self):
        """将关闭sql的代码放在del中，结束程序时python解释器会自动执行"""
        self.cursor.close()
        self.conn.close()
        print("\n[INFO]已经全部关闭")

    def display_menu(self):
        print("-" * 50)
        print("[0] 查询{}".format(self.tables[0]))
        print("[1] 查询{}".format(self.tables[1]))
        print("[2] 查询{}".format(self.tables[2]))
        print("[3] 增加商品分类")
        print("退出程序请直接关闭")
        option = input("请选择: ")
        option = int(option)
        assert option in range(4)
        return option

    def retrieve(self, option):
        sql = "select * from {};".format(self.tables[option])
        count = self.cursor.execute(sql)
        for i in range(count):
            print(self.cursor.fetchone())

    def add_cates(self):
        new_brand = input("请输入要添加的商品分类: ")
        sql = "insert into goods_cates (name) values ('{}');".format(new_brand)
        self.cursor.execute(sql)
        self.conn.commit()

    def run(self):
        while True:
            try:
                option = self.display_menu()
            except Exception:
                print("选择错误，请重新选择")
            else:
                if option in range(len(self.tables)):
                    self.retrieve(option)
                else:
                    self.add_cates()


def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()
