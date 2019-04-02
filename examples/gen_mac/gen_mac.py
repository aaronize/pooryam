#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def gen_mac():
    mac1 = hex(random.randint(0, 255))[2:4]
    if len(mac1) == 1:
        mac1 = '0' + mac1
    mac2 = hex(random.randint(0, 255))[2:4]
    if len(mac2) == 1:
        mac2 = '0' + mac2
    mac3 = hex(random.randint(0, 255))[2:4]
    if len(mac3) == 1:
        mac3 = '0' + mac3
    return mac1 + ':' + mac2 + ':' + mac3


def gen_mac_2():
    mac = ''
    for i in range(0, 3, 1):
        tmp = hex(random.randint(0, 255))[2:4]
        if len(tmp) == 1:
            tmp = '0' + tmp
        if i == 2:
            mac = mac + tmp
        else:
            mac = mac + tmp + ':'
    return mac


if __name__ == "__main__":
    print 'generate mac: ', gen_mac()
    print 'generate mac 2:', gen_mac_2()
