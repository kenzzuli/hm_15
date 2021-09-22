# 贪婪和非贪婪，以及换行符对.的影响
import re

a = """
<meta charset="UTF-8">
<meta name="description">
<meta name="keywords">"""

# 非贪婪模式下匹配
print(re.findall("<.*?>", a))
# 匹配到3个结果
# ['<meta charset="UTF-8">', '<meta name="description">', '<meta name="keywords">']

# 贪婪模式下匹配
print(re.findall("<.*>", a))
# 匹配到3个结果，是因为a中存在换行符，这种换行符无法通过print打印看到，通过ipython可以看到
# ['<meta charset="UTF-8">', '<meta name="description">', '<meta name="keywords">']

# 如果在re.或re.DOTALL模式下，.可以匹配换行，此时再贪婪匹配
print(re.findall("<.*>", a, re.S))
# 匹配到一个结果
# ['<meta charset="UTF-8">\n<meta name="description">\n<meta name="keywords">']

# 如果在re.或re.DOTALL模式下，.可以匹配换行，用非贪婪匹配
print(re.findall("<.*?>", a, re.DOTALL))
# 匹配三个结果
# ['<meta charset="UTF-8">', '<meta name="description">', '<meta name="keywords">']
