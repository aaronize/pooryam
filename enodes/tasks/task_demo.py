# coding: utf-8

from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time


# @app.task
@shared_task
def send_mail(mail):
    print 'sending mail to {}...'.format(mail['to'])
    time.sleep(2.0)

    print 'mail sent.'
