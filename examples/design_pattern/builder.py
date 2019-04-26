#!/usr/bin/env python
# coding: utf-8


class Computer:
    def __init__(self, sn):
        self.sn = sn
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG23385193')

    def configure_memory(self, memory):
        self.computer.memory = memory

    def configure_hdd(self, hdd):
        self.computer.hdd = hdd

    def configure_gpu(self, gpu):
        self.computer.gpu = gpu


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                           self.builder.configure_hdd(hdd),
                           self.builder.configure_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer


if __name__ == '__main__':
    engineer = HardwareEngineer()
    engineer.construct_computer(memory=8, hdd=500, gpu='GeForce')
    computer = engineer.computer
    print computer
