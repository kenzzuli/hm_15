from pymysql import *


def main():
    conn = connect(host="localhost", user="root", password="liulei123", database="jing_dong", port=3306, charset="utf8")
    cursor = conn.cursor()
    tables = ["goods", "goods_brands", "goods_cates"]
    while True:
        try:
            option = input("请选择要查询的数据表: [1] {} [2] {} [3] {} (退出程序请直接关闭): ".format(tables[0], tables[1], tables[2]))
            option = int(option)
            assert option in [1, 2, 3]
        except KeyboardInterrupt:
            cursor.close()
            conn.close()
            print("\n[INFO]已经全部关闭")
            exit()
        except Exception:
            print("选择错误，请重新选择")
        else:
            sql = "select * from {};".format(tables[option - 1])
            count = cursor.execute(sql)
            for i in range(count):
                print(cursor.fetchone())


if __name__ == '__main__':
    main()
