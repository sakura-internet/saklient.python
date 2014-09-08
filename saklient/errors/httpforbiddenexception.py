# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpforbiddenexception

class HttpForbiddenException(HttpException):
    ## 要求された操作は許可されていません。権限エラー。
    
    # (class field) default_message = "要求された操作は許可されていません。権限エラー。"
    
    pass
