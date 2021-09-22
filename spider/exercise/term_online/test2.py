import pandas as pd
import os

d1 = {"name": "lihang", "age": 22, "tel": 10010, "gender": "m"}
t1 = pd.DataFrame(d1, index=[0])
t1.to_excel("1.xlsx")
print(t1.head())
print("*" * 50)
dic1 = {"name": "liulei", "gender": "m", "age": 18}
dic2 = {"name": "zhouyan", "age": 20}
dict3 = {"name": "xiaowen", "gender": "f"}
dict4 = {"name": "zhouyan", "age": 20}
dic = [dic1, dic2, dict3, dict4]
info = pd.DataFrame(dic)
total = t1.append(info)
print(total.head(10))
ret = total.drop_duplicates().reset_index(drop=True)
if os.path.exists("./1.xlsx"):
    os.remove("1.xlsx")
print(ret)
ret.to_excel("1.xlsx")
os.remove("2.txt")
