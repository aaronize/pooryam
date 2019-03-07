#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess


def exec_cmd(ip):
    cmd = ''

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    proc.wait()
    err_msg = proc.stderr.read().decode('utf-8')
    ret_code = proc.returncode
    output = proc.stdout.read().decode('utf-8')

    print ret_code, err_msg, output


if __name__ == '__main__':
    exec_cmd('192.168.152.183')