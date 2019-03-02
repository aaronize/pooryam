# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# models.py
from django.db import models


class Files(models.Model):
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    md5 = models.CharField(max_length=50)
    createTime = models.CharField(max_length=10)
    updateTime = models.CharField(max_length=10)
    recentUpdatePerson = models.CharField(max_length=20)
    createPerson = models.CharField(max_length=20)
    managePerson = models.CharField(max_length=20)
    info = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
