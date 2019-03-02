#!/usr/bin/env python
# -*- coding: utf-8 -*-



def counter(initial):
    arr = list()
    for i in range(5):
        def tmp(n):
            def data():
                print n
            arr.append(data)
        tmp(i)
    return arr

func = counter("nihao shijie")

func[0]()
func[1]()
func[2]()
func[3]()
func[4]()





