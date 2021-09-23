from distutils.core import setup

# setup接收字典参数
setup(name="hm_message",  # 包名
      version="1.0",  # 版本
      description="发送和接收消息模块",  # 描述信息
      long_description="这是一个完整的发送和接收消息模块",  # 完整描述信息
      author="itheima",  # 作者
      author_email="itheima@itheima.com",  # 作者邮箱
      url="www.itheima.com",  # 主页
      py_modules=["hm_message.send_message",
                  "hm_message.receive_message"]) # 要分享的模块的名称
