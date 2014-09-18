# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpforbiddenexception

class HttpForbiddenException(HttpException):
    ## 要求された操作は許可されていません。権限エラー。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpForbiddenException, self).__init__(status, code, "要求された操作は許可されていません。権限エラー。" if message is None or message == "" else message)
    
