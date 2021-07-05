import time


def login():
    return "<h1>login!</h1><h2>{}</h2>".format(time.ctime())


def register():
    return "<h1>register!</h1><h2>{}</h2>".format(time.ctime())


def profile():
    return "<h1>profile!</h1><h2>{}</h2>".format(time.ctime())


def error():
    return "<h1>error!</h1><h2>{}</h2>".format(time.ctime())


def application(url):
    url = url[1:-3]
    print(url)
    if url == "profile":
        return profile()
    elif url == "login":
        return login()
    elif url == "register":
        return register()
    else:
        return error()
