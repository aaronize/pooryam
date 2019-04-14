from __future__ import absolute_import, unicode_literals
from celery import Celery
import time

# celery configuration
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_BROKER_BACKEND = 'redis://127.0.0.1:6379/1'
CELERY_BROKER_SERIALIZER = 'json'

app = Celery(b'celery_demo', broker=CELERY_BROKER_URL, backend=CELERY_BROKER_BACKEND)
# app.broker_connection = ''
# app.backend_cls = ''

# app.conf.broker_url = ''
# app.conf.result_backend = ''
# app.conf.task_default_exchange = ''


@app.task
def send_mail(mail):
    print 'sending mail to {}...'.format(mail['to'])
    time.sleep(2.0)
    print 'mail sent.'


if __name__ == "__main__":
    ret = send_mail.delay(dict(to='aaron.chen@cdswit.cn'))
    #
    if ret.ready():
        print 'result ready!'
    else:
        print 'result not ready! Pls wait for a while...'

    try:
        # timeout will throw exception
        print 'get result:', ret.get(timeout=3)
    except Exception, e:
        print 'get result exception(s): ', str(e)

    print 'traceback:', ret.traceback

    print 'task_id:', ret.task_id
