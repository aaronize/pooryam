#!/usr/bin/env python
# coding: utf-8


def rob(nums):
    n = len(nums)
    if n <= 1:
        return 0 if n == 0 else nums[0]
    memo = list()
    memo.append(nums[0])
    memo.append(max(nums[0], nums[1]))

    for i in range(2, n, 1):
        memo.append(max(memo[i - 1], nums[i] + memo[i - 2]))

    return memo[n - 1]


if __name__ == '__main__':
    num_list = [2, 7, 9, 3, 1, 3]
    print 'result is: ', rob(num_list)
