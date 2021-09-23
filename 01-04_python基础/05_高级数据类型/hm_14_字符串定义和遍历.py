str1 = "hello python"
# 字符串一般都用双引号，只有当双引号出现在字符串中时，才使用单引号
str2 = '我的外号是"大西瓜"'

# 取值
print(str1[6])

# 取索引
print(str1.index('e'))

# 统计
# 字符串长度
print(len(str1))
# 小字符串在大字符串中出现的次数
str3 = "hello, hi"
str4 = "he"
print(str3.count(str4))

# 遍历
for char in str2:
    print(char)

