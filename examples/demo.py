#!/usr/bin/env python
# -*- coding: utf-8 -*-


def digit_sum(num):
    num_str = str(num)
    ret = 0
    for dig_str in num_str:
        ret += int(dig_str)

    return ret


if __name__ == "__main__":

    print digit_sum(1021196)
