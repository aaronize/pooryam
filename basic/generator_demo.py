# coding: utf-8

import time
from itertools import islice


def consumer():
    product = None
    while True:
        if product is not None:
            print 'consumer: {}'.format(product)
        product = yield None


def producer():
    c = consumer()
    next(c)
    for i in range(10):
        c.send(i)


class Fib(object):
    def __init__(self):
        self.__prev = 0
        self.__curr = 1

    def fib(self):
        while True:
            yield self.__curr
            self.__prev, self.__curr = \
                self.__curr, self.__curr + self.__prev


if __name__ == '__main__':
    start = time.time()
    producer()
    end = time.time()
    print 'spend time: {}'.format(end - start)

    fib = Fib()
    # print 'list: ', list(islice(fib, 0, 10))
    type(fib)
    print next(fib)
