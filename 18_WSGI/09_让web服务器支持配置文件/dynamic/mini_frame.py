import re


def read_from_file(file_path):
    with open(file_path, mode="rb") as f:
        return f.read()


def index():
    # 这里的路径 都要按照python最开始的执行文件的路径来算。
    # python运行的是web_server.py 所有的路径都以该文件所在的路径来计算
    content = read_from_file("./templates/index.html")
    my_stock_info = "这里是主页数据"
    content = re.sub(r"{%content%}", my_stock_info, content.decode())
    return content


def center():
    content = read_from_file("./templates/center.html")
    my_stock_info = "这里是mysql查询到的数据"
    content = re.sub(r"{%content%}", my_stock_info, content.decode())
    return content


def login():
    return "login"


def register():
    return "register"


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    if environ['url'] == "/index.py":
        return index()
    elif environ['url'] == "/center.py":
        return center()
    elif environ['url'] == "/register.py":
        return register()
    elif environ['url'] == "/login.py":
        return login()
    else:
        return 'page not found'
