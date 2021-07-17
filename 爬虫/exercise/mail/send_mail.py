import smtplib
from email.mime.text import MIMEText
from retrying import retry
import sys
import socket


@retry(stop_max_attempt_number=10)
def notify_me(hostname=socket.gethostname(), task=sys.argv[0]):
    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.yeah.net'
    # 163用户名
    mail_user = 'liulei666666'
    # 密码(部分邮箱为授权码)
    mail_pass = 'liulei123'
    # 邮件发送方邮箱地址
    sender = 'liulei666666@yeah.net'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['820710063@qq.com']

    # 设置email信息
    # 邮件内容设置
    message = MIMEText('请及时查看', 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = "[{}]上的任务[{}]已经完成！".format(hostname, task)
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误


if __name__ == '__main__':
    notify_me()
