#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail(type, send_to):
    mail_host = 'smtp.163.com'
    mail_user = '*'
    mail_pass = '*'

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
