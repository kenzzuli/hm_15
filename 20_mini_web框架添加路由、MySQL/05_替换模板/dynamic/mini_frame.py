import re
from pymysql import *

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

    # 从数据库查询数据
    conn = connect(user="root", password="liulei123", host="localhost", database="stock_db", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from info;")
    my_stock_info = cursor.fetchall()
    cursor.close()
    conn.close()

    # 拼装html模板
    html = ""

    # 不要自己拼，直接用模板
    # for line in my_stock_info:
    #         html += "<tr>"
    #     for col in line:
    #             html += "<td>{}</td>".format(col)
    #         html += """<td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue="00001"></td>"""
    #         html += "</tr>"

    html_template = """
               <tr>
                   <td>%s</td>
                   <td>%s</td>
                   <td>%s</td>
                   <td>%s</td>
                   <td>%s</td>
                   <td>%s</td>
                   <td>%s</td>
                   <td>%s</td>
                   <td>
                       <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                   </td>
                   </tr>"""
    for line in my_stock_info:
        html += html_template % (*line, line[1])

    content = re.sub(r"{%content%}", html, content.decode())
    return content


@route("/center.html")
def center(file_name):
    file_name = file_name.replace(".py", ".html")
    content = read_from_file(template_path + file_name)

    # 从数据库查询数据
    conn = connect(user="root", password="liulei123", host="localhost", database="stock_db", charset="utf8")
    cursor = conn.cursor()
    sql = """select info.code, info.short, info.chg, info.turnover, info.price, info.highs, focus.note_info
from info inner join focus on focus.info_id = info.id;"""
    cursor.execute(sql)
    my_stock_info = cursor.fetchall()
    cursor.close()
    conn.close()

    # 拼装html模板
    html = ""
    html_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
            </td>
        </tr>
        """
    for line in my_stock_info:
        html += html_template % (*line, line[0], line[0])

    content = re.sub(r"{%content%}", html, content.decode())
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
