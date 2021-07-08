def index():
    return "index"


def login():
    return "login"


def register():
    return "register"


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    if environ['url'] == "/index.py":
        return index()
    elif environ['url'] == "/register.py":
        return register()
    elif environ['url'] == "/login.py":
        return login()
    else:
        return 'page not found'
