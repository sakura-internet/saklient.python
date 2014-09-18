# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httprequesturitoolongexception

class HttpRequestUriTooLongException(HttpException):
    ## HTTPエラー。Request Uri Too Long.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpRequestUriTooLongException, self).__init__(status, code, "HTTPエラー。Request Uri Too Long." if message is None or message == "" else message)
    
