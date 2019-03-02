#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
import Queue
import threading
import os


class Download(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.empty():
                print "-----%s-----" % self.name
                os.system("wget " + self.queue.get())
            else:
                break


def do_download(url, rule, num, start, end, decoding=None):
    if not decoding:
        decoding = 'utf8'
