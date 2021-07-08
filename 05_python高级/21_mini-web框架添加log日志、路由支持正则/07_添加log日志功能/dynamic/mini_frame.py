import re
from pymysql import *
import urllib.parse
import logging

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
    with open(file_path, mode="r") as f:
        return f.read()


# 给路由器添加正则表达式的原因: 在实际开发中，url中往往会带很多参数，例如/add/00007.html中00007就是参数，
# 如果没有正则的话，那么就需要编写N次@route来进行添加url对应的函数到字典中，此时字典中的键值对为N个，浪费空间
# 而如果采用了正则的话，那么只要编写1次@route就可以完成多个url 例如/add/0006.html /add/0003.html等对应同一个函数
# 此时字典中的键值对个数会少很多
@route(r"/add/(\d+)\.html")
def add_focus(*args):
    # 1.获取股票代码
    ret = args[0]
    stock_code = ret.group(1)
    # 2.判断是否存在这个股票代码
    conn = connect(user="root", password="liulei123", host="localhost", database="stock_db", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from info where code=%s;", [stock_code])
    # 如果不能查到结果，说明存在这个股票代码不存在，直接返回
    if not cursor.fetchall():
        cursor.close()
        conn.close()
        return "股票代码(%s)不存在" % stock_code
    # 3.判断是否已经关注过这个股票
    cursor.execute("select * from info inner join focus on focus.info_id = info.id where code=%s;",
                   [stock_code])
    # 如果能查到结果，说明已经关注了，无需再次关注
    if cursor.fetchall():
        cursor.close()
        conn.close()
        return "股票代码(%s)已经关注，无需重复关注" % stock_code
    else:  # 如果查不到结果，则向focus表中写入一条新纪录
        cursor.execute("insert into focus (info_id) (select info.id from info where code = %s);", [stock_code])
        conn.commit()
        cursor.close()
        conn.close()
        return "添加自选成功(%s)" % stock_code


@route(r"/del/(\d+)\.html")
def del_focus(*args):
    # 1.获取股票代码
    ret = args[0]
    stock_code = ret.group(1)
    # 2.判断是否已经关注了该股票代码
    conn = connect(user="root", password="liulei123", host="localhost", database="stock_db", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from info inner join focus on focus.info_id = info.id where code=%s;", [stock_code])
    # 如果不能查到结果，则没有关注该股票，直接返回
    if not cursor.fetchall():
        cursor.close()
        conn.close()
        return "未关注股票代码(%s)，请刷新页面" % stock_code
    # 如果能查到结果，则删去该条关注记录
    else:
        cursor.execute("delete from focus where info_id = (select id from info where code = %s);", [stock_code])
        conn.commit()
        cursor.close()
        conn.close()
        return "取消关注成功(%s)" % stock_code


@route(r"/update/(\d+)\.html")  # /update/000007.html
def show_update_page(*args):
    # 1.获取股票代码
    ret = args[0]
    stock_code = ret.group(1)
    # 2.判断是否已经关注该股票
    conn = connect(user="root", password="liulei123", host="localhost", database="stock_db", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select * from info inner join focus on focus.info_id = info.id where code=%s;", [stock_code])
    # 如果不能查到结果，则没有关注该股票，直接返回
    if not cursor.fetchall():
        cursor.close()
        conn.close()
        return "未关注股票代码(%s)，请先关注再修改" % stock_code
    # 如果能查到结果，说明已经关注，显示修改页面
    else:
        cursor.execute("select note_info from focus where info_id = (select id from info where code=%s);", [stock_code])
        note_info = cursor.fetchall()[0][0]
        content = read_from_file(template_path + "/update.html")
        content = re.sub(r"{%code%}", stock_code, content)
        content = re.sub(r"{%note_info%}", note_info, content)
        return content


@route(r"/update/(\d+)/(.+)\.html")  # /update/000007/fuck_you.html
def modify_stock_info(*args):
    ret = args[0]
    stock_code = ret.group(1)
    note_info = ret.group(2)
    note_info = urllib.parse.unquote(note_info)
    conn = connect(user="root", password="liulei123", host="localhost", database="stock_db", charset="utf8")
    cursor = conn.cursor()
    sql = "update focus set note_info = %s where info_id = (select id from info where code = %s);"
    cursor.execute(sql, [note_info, stock_code])
    conn.commit()
    cursor.close()
    conn.close()
    return "修改股票(%s)成功！" % stock_code


@route(r"/index.html")  # route("/index.html")执行的结果指向set_func，用set_func装饰index
def index(*args):
    # 这里的路径 都要按照python最开始的执行文件的路径来算。
    # python运行的是web_server.py 所有的路径都以该文件所在的路径来计算
    content = read_from_file(template_path + "/index.html")

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

    content = re.sub(r"{%content%}", html, content)
    return content


@route(r"/center.html")
def center(*args):
    content = read_from_file(template_path + "/center.html")

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

    content = re.sub(r"{%content%}", html, content)
    return content


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    url = environ['url']
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    logfile = "./log/log.txt"
    file_handler = logging.FileHandler(logfile, mode="a")
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.debug("当前请求的文件为: %s" % url)

    try:
        # 完整的for循环包括else！✅
        for pattern, func in func_dict.items():
            # {
            #   r"/index.html":index,
            #   r"/center.html":center,
            #   r"/add/\d+\.html":add_focus
            # }
            # 如果能匹配到，直接返回对应函数的运行结果
            ret = re.match(pattern, url)
            if ret:
                return func_dict[pattern](ret)
        # 如果遍历字典，都无法匹配到
        else:
            logger.warning("没有对应的函数")
            return "请求的url(%s)没有对应的函数..." % url

    except Exception as e:
        print(e)
        return "出现异常: {}".format(e)
