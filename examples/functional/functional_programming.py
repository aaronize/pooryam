# -*- coding: utf-8 -*-

'''
函数式编程
案例：
有数组numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，编写程序完成以下目标：
- 1. 将numberList中的每个元素加1得到一个新的数组
- 2. 将numberList中的每个元素乘2得到一个新的数组
- 3. 将numberList中的每个元素模3得到一个新的数组
'''
numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 定义map函数。对，就是map/reduce中的map
def map(func, numList):
    newList = []
    for num in numList:
        newList.append(func(num))

    return newList


# 1. 将numberList中的每个元素加1得到一个新的数组
print "1：", map(lambda x: x + 1, numberList)

# 2. 将numberList中的每个元素乘2得到一个新的数组
print "2：", map(lambda x: x * 2, numberList)

# 3. 将numberList中的每个元素模3得到一个新的数组
print "3：", map(lambda x: x % 3, numberList)


