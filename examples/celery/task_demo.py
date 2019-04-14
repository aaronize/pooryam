from __future__ import absolute_import, unicode_literals
from celery import Celery
import time

# celery configuration
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_BROKER_BACKEND = 'redis://127.0.0.1:6379/1'
CELERY_BROKER_SERIALIZER = 'json'

app = Celery(b'tasks', broker=CELERY_BROKER_URL, backend=CELERY_BROKER_BACKEND)


@app.task
def send_mail(mail):
    print 'sending mail to {}...'.format(mail['to'])
    time.sleep(2.0)
    print 'mail sent.'


if __name__ == "__main__":
    ret = send_mail.delay(dict(to='aaron.chen@cdswit.cn'))
    print 'task_id:', ret.task_id
