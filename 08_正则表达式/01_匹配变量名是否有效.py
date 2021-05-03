import re

names = ["name1", "_name", "5_names", "__name__", "age!", "a#123", "_刘"]
valid_names = []
for i, name in enumerate(names):
    # 在遍历列表时，千万不要在循环内部删去列表元素，否则会导致下一个元素被跳过。
    # print(i, name)
    # if re.match(r"[a-zA-Z_]\w*", name) is None:
    #     names.remove(name)

    # if re.match(r"[a-zA-Z_]\w*", name) is not None: # \w会匹配中文字符
    # # ['name1', '_name', '__name__', 'age!', 'a#123', '_刘']

    # if re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", name) is not None:  # match默认匹配开头，但不匹配结尾，这样部分匹配也会认为有效
    # ['name1', '_name', '__name__', 'age!', 'a#123', '_刘']

    if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name):  # 加上开头结尾，完全匹配
        valid_names.append(name)
        # ['name1', '_name', '__name__']

print(valid_names)
