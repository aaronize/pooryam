#!/usr/bin/env python
# coding: utf-8

from itertools import product, takewhile


# 使用enumerate()函数遍历列表的同时获取下标
def traversal_list(alist):
    # low的做法
    index = 0
    for a in alist:
        print 'index:', index, ', name:', a
        index += 1

    print '*' * 60
    # 更地道的做法
    for i, a in enumerate(alist):
        print 'index:', i, ', name:', a


#
class FindSum(object):
    def __init__(self, target):
        self._target = target

    def find_sum_normally(self, a_list, b_list, c_list):
        for a in a_list:
            for b in b_list:
                for c in c_list:
                    if a + b + c == self._target:
                        return a, b, c

    # 使用product函数简化
    def find_sum(self, a_list, b_list, c_list):
        for a, b, c in product(a_list, b_list, c_list):
            if a + b + c == self._target:
                return a, b, c


class TruncateCircle(object):
    def __init__(self, name):
        self.__name = name

    def __is_qualified(self, name):
        if name == self.__name:
            return True
        else:
            return False

    def truncate_circle_normally(self, name_list):
        for name in name_list:
            if self.__is_qualified(name):
                print 'name is ', name
                break

    def take_while_demo(self, name_list):
        for name in takewhile(self.__is_qualified, name_list):
            print 'name is ', name


if __name__ == '__main__':
    names = ['aaron', 'john', 'shawn', 'jessie']
    # traversal_list(names)

    tc = TruncateCircle('aaron')
    tc.truncate_circle_normally(name_list=names)
    tc.take_while_demo(name_list=names)
