# coding: utf-8

"""
通过文件实现进程间通信
使用文件进行通信是最简单的一种通信方式，子进程将结果输出到临时文件，父进程从文件中读出来。文件名使用子进程的进程id来命名。进程随时都可以通过os.getpid()来获取自己的进程id。
"""

import os
import sys
import math
from calc_pi import calc_slice


def pi(n):
    pids = []
    unit = n / 10

    for i in range(10):
        mink = unit * i
        maxk = mink + unit
        pid = os.fork()
        if pid > 0:
            pids.append(pid)
        else:
            s = calc_slice(mink, maxk)
            with open('%d' % os.getpid(), 'w') as f:
                f.write(str(s))

            sys.exit(0)

    sums = []
    for pid in pids:
        os.waitpid(pid, 0)  # 等待子进程结束
        with open('%d' % pid, 'r') as f:
            sums.append(float(f.read()))
        os.remove('%d' % pid)

    return math.sqrt(sum(sums) * 8)


print pi(1000000)
