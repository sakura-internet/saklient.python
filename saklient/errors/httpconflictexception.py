# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpconflictexception

class HttpConflictException(HttpException):
    ## 要求された操作を行えません。現在の対象の状態では、この操作を受け付けできません。
    
    # (class field) default_message = "要求された操作を行えません。現在の対象の状態では、この操作を受け付けできません。"
    
    pass
