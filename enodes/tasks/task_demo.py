from __future__ import absolute_import, unicode_literals
from celery import Celery
from enodes import config
import time

app = Celery('tasks', broker=config.CELERY_BROKER_URL, backend=config.CELERY_BROKER_BACKEND)


@app.tasks
def send_mail(mail):
    print 'sending mail to {}...'.format(mail['to'])
    time.sleep(2.0)
    print 'mail sent.'
