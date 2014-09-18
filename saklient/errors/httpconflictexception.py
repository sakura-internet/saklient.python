# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpconflictexception

class HttpConflictException(HttpException):
    ## 要求された操作を行えません。現在の対象の状態では、この操作を受け付けできません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpConflictException, self).__init__(status, code, "要求された操作を行えません。現在の対象の状態では、この操作を受け付けできません。" if message is None or message == "" else message)
    
