#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import freeze_support, Pool
import Queue
import time


def foo(i):
    time.sleep(2)
    print('___time---', time.ctime())
    #queue.put(i+100)
    return i + 100


def bar(arg):
    print('----exec done:', arg, time.ctime())


if __name__ == '__main__':
    freeze_support()

    resultList = list()
    queue = Queue.Queue()
    pool = Pool()

    start = time.time()
    print 'executing...'
    for i in range(4):
        resultList.append(pool.apply_async(func=foo, args=(i, ), callback=bar))

    pool.close()
    pool.join()
    print 'mp ended.', time.time() - start

    #print queue.qsize()

    for i in resultList:
        print "result: ", i.get()



