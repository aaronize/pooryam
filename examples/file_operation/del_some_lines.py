#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

'''
这种方式的问题在于，读取文件写入文件的过程中，文件有可能有其他的写入
'''


def del_lines(path, key_word):
    sign = False

    with open(path, 'r') as f:
        lines = f.readlines()

    with open(path, 'w') as fw:
        for line in lines:
            if key_word in line or sign:
                sign = True
                if '}' in line:
                    sign = False
            else:
                fw.write(line)


if __name__ == "__main__":
    path = sys.argv[1]
    ip = sys.argv[2]

    local_time = time.asctime(time.localtime(time.time()))
    print '[%s] 操作%s释放IP:%s' % (local_time, path, ip)

    del_lines(path, ip)
