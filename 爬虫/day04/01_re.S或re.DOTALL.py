import re

# 一般模式下，(.)无法匹配换行(\n)
print(re.findall(".", "\n"))  # []

# 在DOTALL模式或S模式下，(.)可以匹配换行(\n)
# 查看源码发现 S = DOTALL
print(re.findall(".", "\n", re.DOTALL))  # ['\n']
print(re.findall(".", "\n", re.S))  # ['\n']
