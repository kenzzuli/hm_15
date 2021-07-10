import re

# 不分组匹配的是全部
print(re.findall(r"a.*bc", "a\nbc", re.DOTALL))
# ['a\nbc']
# 分组匹配的是组内的内容
print(re.findall(r"a(.*)b", "a\nb", re.DOTALL))
# ['\n']
