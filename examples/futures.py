#!/usr/bin/python
# -*- coding: utf-8 -*-


import Queue
import time
from concurrent.futures import ThreadPoolExecutor


def foo(i):
    time.sleep(2)
    #print '>>>>time---', time.ctime()
    return i + 100


def bar(arg):
    print '----exec done:', arg.result()


if __name__ == '__main__':

    resultList = list()
    sendList = list()
    queue = Queue.Queue()
    futureList = list()

    executor = ThreadPoolExecutor(5)

    begin = time.time()
    for i in range(4):
        future = executor.submit(foo, i).add_done_callback(bar)





