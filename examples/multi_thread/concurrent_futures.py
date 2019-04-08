#!/usr/bin/env python
# coding=utf-8

import re
import time
import logging
import requests
import subprocess as sp

URL = ''


def exec_cmd(cmd):
    process = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    try:
        start_time = time.time()
        time_out = 30
        while True:
            if process.poll() is not None:
                break
            time.sleep(1)
            delta_time = time.time() - start_time
            if delta_time > time_out:
                process.terminate()
                print '执行超时了'
                return False

        process.wait()
        ret_code = process.returncode
        err_msg = process.stderr.read().decode('utf-8')

        if re.search('Connection refused|Permission denied', err_msg) is not None:
            if ret_code != 0:
                print '返回码：', ret_code, '错误信息：', err_msg
                return False
            else:
                print '执行成功'
                return True
        else:
            print '返回码：', ret_code, '错误信息：', err_msg
            return False
    except Exception, e:
        print '错误信息：', str(e)
        return False


def callback_after(arg):
    res = arg.result()
    try:
        if res:
            print 'callback_after收到返回信息', res
            requests.post(URL, )
        else:
            print 'callback_after收到返回信息', res
    except Exception, e:
        pass


def release(info_list):
    pass


if __name__ == '__main__':
    pass