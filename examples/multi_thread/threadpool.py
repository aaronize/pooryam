#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-

import Queue
import time
from concurrent.futures import ThreadPoolExecutor


def foo(i):
    time.sleep(2)
    print '>>>>time---', time.ctime()
    return i + 100


def bar(arg):
    print '----exec done:', arg, time.ctime()


if __name__ == '__main__':

    resultList = list()
    sendList = list()
    queue = Queue.Queue()
    futureList = list()

    executor = ThreadPoolExecutor(5)

    begin = time.time()
    for i in range(4):
        #future = executor.submit(foo, i)
        sendList.append(i)

    future = executor.map(foo, sendList)

    # for i in range(4):
    #     print ">>>>>future next>>>", future.next()
    # print ">>>>>future next1>>>", future.next()
    # print ">>>>>future next2>>>", future.next()
    # print ">>>>>future next3>>>", future.next()
    # print ">>>>>future next4>>>", future.next()

    for fu in futureList:
        # print ">>>>fun done()>>>>", fu.done()
        print ">>>>result>>>>>>>>", fu.result()

    usedTime = time.time() - begin
    print "used time: ", usedTime





    #print queue.qsize()

    for i in resultList:
        print "result: ", i.get()



