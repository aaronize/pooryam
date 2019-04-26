#!/usr/bin/env python
# coding: utf-8

import sys


def cp_content(file_path, cp_times):

    with open(file_path, 'r') as fd:
        lines = fd.readlines()

    with open(file_path, 'w') as fw:
        for i in range(0, cp_times, 1):
            for line in lines:
                fw.write(line)


if __name__ == '__main__':
    path = sys.argv[1]
    times = int(sys.argv[2])

    cp_content(file_path=path, cp_times=times)
