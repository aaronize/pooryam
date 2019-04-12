#!/usr/bin/env python
# coding: utf-8


class BaseTool(object):
    def __init__(self):
        self._condition = Conditional('cond01')
        self._state = 'running'
        self._tools = list()

    def add_tool(self, tool):
        with self._condition as c:
            print '>>>', c              # >>> __enter__ return
            if self._state == 'running':
                self._tools.append(tool)

    def get_tools(self):
        for tool in self._tools:
            print 'tool:', tool

'''
实现两个方法：
__enter__(self)
__exit__(self, exc_type, exc_val, exc_tb)
'''
class Conditional:
    def __init__(self, condition):
        self.condition = condition

    def __enter__(self):
        print '__enter__ method'
        return '__enter__ return'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__ method'
        pass

    def get_condition(self):
        return self.condition

    def update_condition(self, condition):
        self.condition = condition


if __name__ == '__main__':
    bt = BaseTool()
    bt.add_tool('operator')
    bt.add_tool('starter')

    bt.get_tools()
