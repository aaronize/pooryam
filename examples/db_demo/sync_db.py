#!/usr/bin/env python
# coding: utf-8

import pymysql
import time


# 批量读取，批量插入
class SyncDB(object):

    def __init__(self, src_db_conf, dst_db_conf):
        self._src_conf = src_db_conf
        self._dst_conf = dst_db_conf

    def __enter__(self):
        self._src_db = pymysql.connect(host=self._src_conf['host'], user=self._src_conf['user'], passwd=self._src_conf['passwd'],
                                       db=self._src_conf['db'], charset=self._src_conf['charset'])
        self._src_cur = self._src_db.cursor()

        self._dst_db = pymysql.connect(host=self._dst_conf['host'], user=self._dst_conf['user'], passwd=self._dst_conf['passwd'],
                                       db=self._dst_conf['db'], charset=self._dst_conf['charset'])
        self._dst_cur = self._dst_db.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'closing src_db'
        self._src_db.commit()
        self._src_cur.close()
        self._src_db.close()

        print 'closing dst_db'
        self._dst_db.commit()
        self._dst_cur.close()
        self._dst_db.close()

    def exec_sync(self, src_table, dst_table):
        print 'Executing sync... from:', src_table.keys(), ", to:", dst_table.keys()
        self._sync_specify_table(src_table, dst_table)

    def _sync_all(self):
        print 'syncing all tables'
        self._src_cur.execute("SHOW TABLES")

    def _sync_specify_table(self, src_table, dst_table):
        src_table_name = ''
        src_table_columns = list()
        dst_table_name = ''
        dst_table_columns = list()
        for k, v in src_table.items():
            src_table_name, src_table_columns = k, v
        for k, v in dst_table.items():
            dst_table_name, dst_table_columns = k, v

        src_sql = 'SELECT '
        for column in src_table_columns:
            src_sql += column + ','

        if src_sql:
            src_sql = src_sql.rstrip(',')
        src_sql += ' FROM {}'.format(src_table_name)

        print '>>>src sql>>>', src_sql
        self._src_cur.execute(src_sql)
        rows = self._src_cur.fetchall()

        dst_sql = 'INSERT INTO {} ('.format(dst_table_name)
        holders = ''
        for column in dst_table_columns:
            dst_sql += column + ','
            holders += '%s,'
        if dst_sql:
            dst_sql = dst_sql.rstrip(',')
        if holders:
            holders = holders.rstrip(',')

        dst_sql += ') VALUES ({})'.format(holders)

        print '>>>dst sql>>>', dst_sql
        for row in rows:
            values = list()
            for i in row:
                values.append(i)
            try:
                self._dst_cur.executemany(dst_sql, (values,))
            except Exception, e:
                if 'Duplicate entry' in e[1]:
                    print 'duplicate entry... continued'

    def keep_alive(self):
        while True:
            time.sleep(5.0)
            print 'ping check...'
            try:
                self._src_db.ping()
                print 'success!'
            except Exception, e:
                print 'connection error,', str(e)
                break
        return

    def execute_sql_src(self, sql):
        self._src_cur.execute(sql)
        return self._src_cur.fetchall()

    def execute_sql_dst(self, sql):
        self._dst_cur.execute(sql)
        return self._dst_cur.fetchall()

    def backup_table(self):
        pass


if __name__ == '__main__':
    src_conf = {
        'host': 'localhost',
        'user': 'root',
        'passwd': '123456',
        'db': 'testdb',
        'charset': 'utf8'
    }
    dst_conf = {
        'host': 'localhost',
        'user': 'root',
        'passwd': '123456',
        'db': 'usa2',
        'charset': 'utf8'
    }

    with SyncDB(src_db_conf=src_conf, dst_db_conf=dst_conf) as sync:
        from_table = {'table_name1': ['column11', 'column12', 'column13']}
        to_table = {'table_name2': ['column21', 'column22', 'column23']}

        sync.exec_sync(src_table=from_table, dst_table=to_table)

