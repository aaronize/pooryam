#!/usr/bin/env python
# coding=utf-8

import re
import time
import subprocess as sp
from concurrent import futures


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

        if re.search('Connection refused|Permission denied', err_msg) is None:
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
        else:
            print 'callback_after收到返回信息', res
    except Exception, e:
        print 'callback exception，', str(e)

    return


def release(info_list):
    # ret = list()
    # task_list = list()

    exector = futures.ThreadPoolExecutor()
    for info in info_list:
        exector.submit(exec_cmd, info['CMD']).add_done_callback(callback_after)

    return


if __name__ == '__main__':
    infos = [{
        'CMD': '/usr/bin/ssh -l root 192.168.152.183 "touch /tmp/test.txt; echo `date` >> /tmp/test.txt"'
    }]
    release(infos)
