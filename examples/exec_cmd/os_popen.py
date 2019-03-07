#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def exec_cmd(ip):
    cmd = 'ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 -l root {} "ls /root/"'.format(ip)
    print cmd
    output = os.popen(cmd, 'r').read()
    print 'execute cmd result>>', output

    return output


if __name__ == '__main__':
    exec_cmd('192.168.168.154')
