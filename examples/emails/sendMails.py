<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail(type, send_to):
    mail_host = 'smtp.163.com'
    mail_user = 'cdswit'
    mail_pass = '327dcc6fab5f262a'

    sender = 'cdswit@163.com'
    receivers = send_to

    if type == 'mem_alert':
        msg = MIMEText('这是一封自动发送的告警邮件，主机IP【】有内存使用高于告警值！请及时查看', 'plain', 'utf-8')
        msg['From'] = sender  # Header('cdswit_service', 'utf-8')
        msg['To'] = receivers[0]  # Header('chendai2004', 'utf-8')

        subj = '内存过高告警'
        msg['Subject'] = Header(subj, 'utf-8')

    elif type == 'cpu_alert':
        msg = ''

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, 25)
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(sender, receivers, msg.as_string())
        print '>>>>>>.'
        print '邮件发送成功！'
    except smtplib.SMTPAuthenticationError:
        print "Error: SMTPAuthenticationError"
    except smtplib.SMTPException:
        print 'ERROR: SMTPException'
    finally:
        smtp_obj.close()
=======
#!/usr/bin/env python
# coding: utf-8

# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
# import smtplib


# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))
#
#
# from_addr = raw_input('cdswit@163.com')
# password = raw_input('daichen1124')
# to_addr = raw_input('aaron.chen@ucloud.cn')
# smtp_server = raw_input('smtp.163.com')
#
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg['From'] = _format_addr(u'这是一封测试邮件 <%s>' % from_addr)
# msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
# msg['Subject'] = Header(u'测试邮件subject……', 'utf-8').encode()
#
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.close()


import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'cdswit@163.com'
receivers = ['aaron.chen@ucloud.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "cdswit@163.com"  # 用户名
mail_pass = "daichen1124"  # 口令

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("hello, from_msg send by python", 'utf-8')
message['To'] = Header("to_msg 测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
>>>>>>> from_hp
