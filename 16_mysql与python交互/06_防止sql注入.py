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
        print("[4] 根据名字查询一个商品信息")
        print("退出程序请直接关闭")
        print("-" * 50)
        option = input("请选择: ")
        option = int(option)
        assert option in range(5)
        return option

    def execute_sql_and_print(self, sql):
        self.cursor.execute(sql)
        for line in self.cursor.fetchall():
            print(line)

    def retrieve(self, option):
        sql = "select * from {};".format(self.tables[option])
        self.execute_sql_and_print(sql)

    def add_cates(self):
        new_brand = input("请输入要添加的商品分类: ")
        sql = "insert into goods_cates (name) values ('{}');".format(new_brand)
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        goods_name = input("请输入要查询的商品名称: ")
        # 用%s来占位
        sql = "select * from goods where name = %s;"
        # 用列表里的元素来填充%s，列表元素个数应该等于%s个数
        self.cursor.execute(sql, [goods_name])
        # 用 " or 1=1 or "  测试也没问题
        for line in self.cursor.fetchall():
            print(line)

    def run(self):
        while True:
            try:
                option = self.display_menu()
            except Exception:
                print("选择错误，请重新选择")
            else:
                if option in range(len(self.tables)):
                    self.retrieve(option)
                elif option == 3:
                    self.add_cates()
                elif option == 4:
                    self.get_info_by_name()


def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()
