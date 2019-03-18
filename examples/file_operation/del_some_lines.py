#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def del_line(path, key_word):
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
    print '释放ip：', path, ip

    file_path = './dhcp.lease'
    release_ip = '192.168.152.172'

    del_line(path, ip)
