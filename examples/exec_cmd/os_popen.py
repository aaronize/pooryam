#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def exec_cmd():
    cmd = 'ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 -l root ""'

    output = os.popen(cmd, 'r').read()
    print 'execute cmd result>>', output

    return output


if __name__ == '__main__':
    exec_cmd()
