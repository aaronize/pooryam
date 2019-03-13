#!/usr/bin/env python
# -*- coding: utf-8 -*-


DEFAULT_CONF_PATH = "../config/development.py"
path = DEFAULT_CONF_PATH


def load_config():
    global path
    path = "./config/production.py"
    print path


load_config()
print path
