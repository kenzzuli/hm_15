import re

res = re.sub(r"\d+", "998", "times=100")
# 返回的是替换后的字符串
print(res)
# times=998

def add(tmp):
    num_str = tmp.group()
    num = int(num_str) + 1
    return str(num)


result = re.sub(r"\d+", add, "times=100")
print(result)

# times=101