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

    def run(self):
        while True:
            try:
                option = input("请选择要查询的数据表: [0] {} [1] {} [2] {} (退出程序请直接关闭): ".format(self.tables[0], self.tables[1],
                                                                                       self.tables[2]))
                option = int(option)
                assert option in range(len(self.tables))
            except Exception:
                print("选择错误，请重新选择")
            else:
                sql = "select * from {};".format(self.tables[option])
                count = self.cursor.execute(sql)
                for i in range(count):
                    print(self.cursor.fetchone())


def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()
