#!/usr/bin/env python
# coding: utf-8

from pymongo import MongoClient


class MongoDBConnectionManager():
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(host=self.hostname, port=self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


if __name__ == '__main__':
    host = '192.168.32.128'
    port = 27017

    with MongoDBConnectionManager(host, port) as db:
        collection = db.connection.umgr.user
        rets = collection.find({'age': {'$gt': 20}})
        for ret in rets:
            print '$gt查询数据结果：', ret
