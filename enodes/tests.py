# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import grequests

# Create your tests here.

ret = [grequests.get("https://www.baidu.com")]

print grequests.map(ret)
