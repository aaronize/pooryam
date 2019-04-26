#!/usr/bin/env python
# coding: utf-8

'''

__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。

__new__在__init__之前被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数。
'''


class PositiveInteger0(int):
    def __init__(self, value):
        self._val = abs(value)
        super(PositiveInteger0, self).__init__(self._val)


class PositiveInteger(int):
    @staticmethod
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))


if __name__ == '__main__':
    i0 = PositiveInteger0(-1)
    print i0

    i1 = PositiveInteger(-2)
    print i1
