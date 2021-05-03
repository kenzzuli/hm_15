# 匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
import re

mail_list = ["10086@163.com", "kenzzuli@126.com", "2@qq.com", "xiaoWang@163.com",
             "xiaoWang@163.comheihei", ".com.xiaowang@qq.com", "liulei@1633com"]

for mail in mail_list:
    # res = re.match(r"^[a-zA-Z0-9_]{4,20}@163.com$", mail)  # 这里面有. 必须转义
    # 如果在正则表达式中需要使用一些特殊字符，需要将这些特殊字符转义
    # res = re.match(r"^[a-zA-Z0-9_]{4,20}@163\.com$", mail)
    # 使用分组匹配163和126邮箱
    res = re.match(r"^[a-zA-Z0-9_]{4,20}@(163|126)\.com$", mail)
    if res:
        print(mail, res.group(1))
