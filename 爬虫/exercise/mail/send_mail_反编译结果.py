# uncompyle6 version 3.7.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.13 |Anaconda, Inc.| (default, Feb 23 2021, 12:58:59) 
# [GCC Clang 10.0.0 ]
# Embedded file name: ./send_mail.py
# Compiled at: 2021-07-17 12:46:09
# Size of source mod 2**32: 1454 bytes
import smtplib
from email.mime.text import MIMEText
from retrying import retry
import sys, socket

@retry(stop_max_attempt_number=10)
def notify_me(hostname=socket.gethostname(), task=sys.argv[0]):
    mail_host = 'smtp.yeah.net'
    mail_user = 'liulei666666'
    mail_pass = 'liulei123'
    sender = 'liulei666666@yeah.net'
    receivers = [
     '820710063@qq.com']
    message = MIMEText('请及时查看', 'plain', 'utf-8')
    message['Subject'] = '[{}]上的任务[{}]已经完成！'.format(hostname, task)
    message['From'] = sender
    message['To'] = receivers[0]
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)


if __name__ == '__main__':
    notify_me()