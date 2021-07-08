# 用装饰器为字符串加标签
def add_h1_tag(func):
    def add_tag(*args, **kwargs):
        return "<h1>" + func() + "</h1>"

    return add_tag


def add_td_tag(func):
    def add_tag(*args, **kwargs):
        return "<td>" + func() + "</td>"

    return add_tag


@add_h1_tag  # 先执行add_h1_tag，所以h1标签在最外面
@add_td_tag
def get_str():
    return "hello"


print(get_str())
# <h1><td>hello</td></h1>
