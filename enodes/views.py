# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import time

from enodes.tasks import task_demo
from models import Files
from public import *


# Create your views here.
def check(request):
    print "this is check..."
    # time.sleep(300)
    check_ret = ExecCheck.exec_check(10)
    info = check_ret['Info']
    status = check_ret['SubStatus']

    ret = {"Action": "check", "Message": "checking.", "Info": info}

    return HttpResponse(json.dumps(ret))


def verify(request):
    print "verifying info..."
    ret = {"Action": "verify", "Message": "verify_success", "Info": ""}

    return HttpResponse(json.dumps(ret))


def get_files(request):
    file_list = Files.objects.all()
    print file_list.all()

    ret = {'Action': 'get_file', 'Message': '', 'Data': file_list.all()}

    return HttpResponse(json.dumps(ret))


@csrf_exempt
def send_mail(request):
    param = request.body.decode(encoding='utf-8')
    send_to = param['to']
    ret = task_demo.send_mail.delay(dict(to=send_to))

    if ret:
        pass
    else:
        pass

    data = {'status': 'successful', 'task_result': ret.task_id, 'code': 0}
    return HttpResponse(json.dumps(data), content_type='application/json')

