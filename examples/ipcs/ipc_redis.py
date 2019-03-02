# coding: utf-8

"""
使用redis实现进程间通信
"""

import math
import os
import sys

import redis

from examples.ipcs.calc_pi import calc_slice


def pi(n):
    pids = []
    unit = n / 10
    client = redis.StrictRedis()
    client.delete('pi')  # 先清理，保证结果干净
    del client
    for i in range(10):     # 启动10个子进程
        mink = unit * i
        maxk = mink + unit
        pid = os.fork()
        if pid > 0:
            pids.append(pid)
        else:
            s = calc_slice(mink, maxk)
            client = redis.StrictRedis()    # 每个子进程开启一个client，向redis发送数据
            client.rpush('pi', str(s))  # rpush 一个或多个值插入到列表的尾部
            sys.exit(0)

    for pid in pids:
        os.waitpid(pid, 0)  # 等待子进程结束

    sums = 0
    client = redis.StrictRedis()    # 父进程开启一个client收集子进程计算结果
    for s in client.lrange('pi', 0, -1):  # 从列表pi中获取全部数据(0到-1)
        sums += float(s)

    return math.sqrt(sums * 8)


print pi(1000000)
