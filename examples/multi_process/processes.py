# coding: utf-8

import os
import time
import signal


def create_child():
    pid = os.fork()
    if pid > 0:
        return pid
    elif pid == 0:
        return 0
    else:
        raise Exception


pid = create_child()
if pid == 0:
    while True:
        print 'in child process'
        time.sleep(1)

else:
    print 'in father process'
    time.sleep(5)
    os.kill(pid, signal.SIGTERM)
    ret = os.waitpid(pid, 0)
    print '>>>ret of waitpid>>>', ret
    time.sleep(5)


