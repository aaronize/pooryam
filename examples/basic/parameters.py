#!/usr/bin/env python
# coding: utf-8


def exc_sync(table_name, *args, **kwargs):
    print 'table_name: ', table_name
    print 'args: ', args
    print 'kwargs', kwargs


if __name__ == '__main__':
    exc_sync('user', 'host', 'port', db='test_db')
