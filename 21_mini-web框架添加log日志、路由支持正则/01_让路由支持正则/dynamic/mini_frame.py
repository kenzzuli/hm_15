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


# 给路由器添加正则表达式的原因: 在实际开发中，url中往往会带很多参数，例如/add/00007.html中00007就是参数，
# 如果没有正则的话，那么就需要编写N次@route来进行添加url对应的函数到字典中，此时字典中的键值对为N个，浪费空间
# 而如果采用了正则的话，那么只要编写1次@route就可以完成多个url 例如/add/0006.html /add/0003.html等对应同一个函数
# 此时字典中的键值对个数会少很多
@route(r"/add/\d+\.html")
def add_focus(file_name):
    return "add ok ..."


@route(r"/index.html")  # route("/index.html")执行的结果指向set_func，用set_func装饰index
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


@route(r"/center.html")
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


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    url = environ['url']
    try:
        # 完整的for循环包括else！✅
        for pattern, func in func_dict.items():
            # {
            #   r"/index.html":index,
            #   r"/center.html":center,
            #   r"/add/\d+\.html":add_focus
            # }
            # 如果能匹配到，直接返回对应函数的运行结果
            if re.match(pattern, url):
                return func_dict[pattern](url)
        # 如果遍历字典，都无法匹配到
        else:
            return "请求的url(%s)没有对应的函数..." % url

    except Exception as e:
        print(e)
        return "出现异常: {}".format(e)
