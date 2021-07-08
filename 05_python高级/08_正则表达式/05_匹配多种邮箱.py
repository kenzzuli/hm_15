# 需求：匹配出163、126、qq邮箱
import re

pattern = r"^\w{4,20}@(163|126|qq)\.com$"

mails = ["test@163.com", "test@gmail.com", "test@126.com", "test@qq.com"]

for mail in mails:
    if re.match(pattern, mail) is not None:
        print(mail)