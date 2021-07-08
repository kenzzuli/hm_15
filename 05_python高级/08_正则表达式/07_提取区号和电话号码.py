# 提取区号和电话号码
import re

tels = ['010-12345678', "0371-10086", "021-234345"]
pattern = r"^([^-]+)-(\d+)$"
for tel in tels:
    res = re.match(pattern, tel)
    if res is not None:
        print(res.group(1), res.group(2))
