import re

template_path = "./templates"
func_dict = dict()


def route(url):  # 这里保存了url，即"index.html"
    def set_func(func):  # 这里保存了原始的index函数，主程序通过字典调用的是原始的index函数，而不是装饰后的index函数
        func_dict[url] = func  # 向字典存储键值对

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func  # 后来的index函数指向call_func

    return set_func


def read_from_file(file_path):
    with open(file_path, mode="rb") as f:
        return f.read()


@route("/index.html")  # route("/index.html")执行的结果指向set_func，用set_func装饰index
def index(file_name):
    # 这里的路径 都要按照python最开始的执行文件的路径来算。
    # python运行的是web_server.py 所有的路径都以该文件所在的路径来计算
    file_name = file_name.replace(".py", ".html")
    content = read_from_file(template_path + file_name)
    my_stock_info = "这里是主页数据"
    content = re.sub(r"{%content%}", my_stock_info, content.decode())
    return content


@route("/center.html")
def center(file_name):
    file_name = file_name.replace(".py", ".html")
    content = read_from_file(template_path + file_name)
    my_stock_info = "这里是mysql查询到的数据"
    content = re.sub(r"{%content%}", my_stock_info, content.decode())
    return content


@route("/login.html")
def login(file_name):
    return "login"


@route("register.html")
def register(file_name):
    return "register"


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    url = environ['url']
    try:
        return func_dict[url](url)
    except Exception as e:
        print(e)
        return "出现异常: {}".format(e)
