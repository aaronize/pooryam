#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.utils.deprecation import MiddlewareMixin

from django.http import HttpResponse
from settings import AUTH_TOKEN

import json

class Authenticate(MiddlewareMixin):

    def process_request(self, request):
        meta = request.META
        if meta.has_key("HTTP_TOKEN"):
            token = meta.get("HTTP_TOKEN")

            if token == AUTH_TOKEN:
                return None
            else:
                info = {"Action":"", "Message": "Invalid Token! "}
        else:
            info = {"Action":"", "Message": "No Token! "}

        return HttpResponse(json.dumps(info))

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     # view_func: django即将使用的视图函数
    #     # view_args: 即将传递给视图函数的参数
    #     # view_kwargs: 即将传递给视图的关键字参数的字典
    #         pass
    #
    # def process_response(self, request, response):
    #     # response是视图函数返回的response对象。这里最后必须要返回response，否则会报错
    #     return response
    #
    # def process_template_response(self, request, response):
    #     pass
    #
    # #
    # def process_exception(self, request, exception):
    #     # exception: 视图产生的异常对象
    #     pass


class Audit(MiddlewareMixin):

    def process_request(self, request):
        # parm = json.loads(request.body.decode('utf-8'))
        meta = request.META

        if meta.has_key('HTTP_USER'):
            user = meta.get('HTTP_USER')
            oper = meta.get('REQUEST_URI')
            print ">>>>>>audit[user: %s, operation: %s]" % (user, oper)
            return None
        else:
            print "No operation user"
            return HttpResponse({"Action":"", "Message":"No operation user."})