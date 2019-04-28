#!/usr/bin/env python
# coding: utf-8

BLOCK_SIZE = 1024 * 1024


def read_block(path):
    f = open(path)
    while True:
        block = f.read(BLOCK_SIZE)
        if not block:
            break
        yield block


if __name__ == '__main__':
    pass