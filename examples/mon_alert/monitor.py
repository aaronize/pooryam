#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送给
SEND_TO = '*@*.com'
# 内存占用告警值
MAX_MEM_PERCENT = 0.85
# 最小free内存告警值
MIN_FREE_MEM = 800.0

# 邮箱配置
MAIL_HOST = 'smtp.163.com'
MAIL_USER = '*'
MAIL_PASS = '*'
SENDER = '*@163.com'


def exec_cmd(ip):
    cmd = 'ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 -l root %s "free -m | sed -n \'2p\' | awk \'{print \$2 \\"\t\\" \$3 \\"\t\\" \$4}\'"' % ip

    output = os.popen(cmd, 'r').read().split()
    return output


def send_mail(mon_type, send_to, send_msg):

    if mon_type == 'mem_alert':
        subj = '[ipipservice/sdk-gateway]内存占用过高告警'
    elif mon_type == 'cpu_alert':
        subj = '[ipipservice/sdk-gateway]CPU占用过高告警'
    else:
        subj = '[ipipservice/sdk-gateway]内存/CPU过高告警'

    msg = MIMEText(send_msg, 'plain', 'utf-8')
    msg['From'] = 'Alerts'      # Header('cdswit_service', 'utf-8')
    msg['To'] = send_to         # Header('chendai2004', 'utf-8')
    msg['Subject'] = Header(subj, 'utf-8')

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(MAIL_HOST, 25)
        smtp_obj.login(MAIL_USER, MAIL_PASS)
        smtp_obj.sendmail(SENDER, send_to, msg.as_string())
        print '邮件发送成功！'
        smtp_obj.quit()

        return 'success'
    except smtplib.SMTPAuthenticationError:
        print "邮件发送失败！Error: SMTPAuthenticationError"
        return 'failed'
    except smtplib.SMTPException:
        print '邮件发送失败！ERROR: SMTPException'
        return 'failed'


def run(ip_list):
    to_send_list = dict()

    for ip in ip_list:
        ret = exec_cmd(ip)
        print '命令执行结果：', ret
        total_mem = float(ret[0])
        used_mem = float(ret[1])
        free_mem = float(ret[2])

        if used_mem/total_mem > MAX_MEM_PERCENT or free_mem < MIN_FREE_MEM:
            to_send_list[ip] = ret
        else:
            pass

    if to_send_list:
        data = str(to_send_list)
        msg = '这是一封自动发送的告警邮件，以下主机内存使用高于告警值！请及时查看。\n {}'.format(data)
        send_mail('mem_alert', SEND_TO, msg)
    else:
        pass


if __name__ == '__main__':
    path = sys.argv[1]

    ips = list()
    with open(path, 'r') as f:
        for line in f.readlines():
            ips.append(line.strip())
    print 'monitoring ip list: ', ips

    run(ips)
