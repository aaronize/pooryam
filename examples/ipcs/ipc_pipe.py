# coding: utf-8

import multiprocessing


def proc1(pipe):
    pipe.send('hello')
    print 'proc 1: ', pipe.recv()


def proc2(pipe):
    pipe.send('hello, too')
    print 'proc 2: ', pipe.recv()


p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))