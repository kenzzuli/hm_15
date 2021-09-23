'''
**需求**

* 在控制台依次提示用户输入：**姓名**、**公司**、**职位**、**电话**、**邮箱**
* 按照以下格式输出：
**************************************************
公司名称

姓名 (职位)

电话：电话
邮箱：邮箱
**************************************************
'''
name = input("please enter a name:")
company = input("please enter the company:")
job = input("please enter the job:")
phone = input("your phone number please:")
mail = input("your mail please:")
print('*' * 50)
print(company)
print()
print("%s(%s)" % (name, job))
print()
print("Phone number: %s" % phone)
print("E-mail: %s" % mail)
print('*'*50)