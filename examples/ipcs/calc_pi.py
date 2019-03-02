# coding: utf-8

"""
计算圆周率
"""

import math


def pi(n):
    s = 0.0
    for i in range(n):
        s += 1.0/(2*i+1)/(2*i+1)

    return math.sqrt(8 * s)


def calc_slice(mink, maxk):
    s = 0.0
    for k in range(mink, maxk):
        s += 1.0 / (2 * k + 1) / (2 * k + 1)

    return s


print pi(10000000)
