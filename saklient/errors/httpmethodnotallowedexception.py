# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpmethodnotallowedexception

class HttpMethodNotAllowedException(HttpException):
    ## 要求されたHTTPメソッドは対応していません。
    
    # (class field) default_message = "要求されたHTTPメソッドは対応していません。"
    
    pass
