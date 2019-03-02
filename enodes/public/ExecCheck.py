#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def exec_check(parm):
    time.sleep(parm)

    info = 'exec check success'

    return {'SubStatus': 'success', 'Info': info, 'Code': 0}

