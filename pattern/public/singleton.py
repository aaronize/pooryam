# coding: utf-8

import time
import threading


class Singleton(object):
    # __new__通过super类创建并返回对象实例
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Bus(Singleton):
    lock = threading.RLock()

    def send_data(self, data):
        self.lock.acquire()
        time.sleep(3.0)
        print 'Sending Single Data...', data
        self.lock.release()


class VisitEntity(threading.Thread):
    bus = ''
    name = ''

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.bus = Bus()
        self.bus.send_data(self.name)


if __name__ == '__main__':
    for i in range(3):
        print 'Entity {} begin to run...'.format(i)

        entity = VisitEntity()
        entity.setName('Entity_{}'.format(i))
        entity.start()
