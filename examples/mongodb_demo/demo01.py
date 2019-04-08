#!/usr/bin/env python
# coding: utf-8

import pymongo


def mongo_demo():
    # client = pymongo.MongoClient(host='192.168.32.128', port=27017)
    client = pymongo.MongoClient('mongodb://192.168.32.128:27017/')
    # 指定数据库
    db = client['umgr']
    # 指定集合user（理解为表格吧）
    user = db['user']
    # 根据id查询
    user1 = user.find_one({'id': '20112420201'})
    print type(user1)  # <type 'dict'>
    print user1['name']  # 获取name域的值


# 插入数据
def insert_demo(client):
    # 指定数据库
    db = client['umgr']
    # 指定集合user（理解为表格吧）
    user = db['user']
    user2 = {
        'id': '20112420202',
        'name': 'Jessica',
        'age': 18,
        'gender': 'female'
    }
    user3 = {
        'id': '20112420203',
        'name': 'jeffery',
        'age': 21,
        'gender': 'male'
    }

    ret = user.insert([user2, user3])
    print '插入数据结果：', ret


def query_demo(client):
    user = client['umgr']['user']
    rets = user.find()
    for ret in rets:
        print '查询所有数据：', ret

    print '------------------------------'
    # 查询age>20的记录
    rets = user.find({'age': {'$gt': 20}})
    for ret in rets:
        print '$gt查询数据结果：', ret

    print '------------------------------'
    rets = user.find({'age': {'$lt': 20}})
    for ret in rets:
        print '$lt查询数据结果：', ret


if __name__ == '__main__':
    # mongo_demo()
    client = pymongo.MongoClient('mongodb://192.168.32.128:27017/')
    # insert_demo(client)
    query_demo(client)
