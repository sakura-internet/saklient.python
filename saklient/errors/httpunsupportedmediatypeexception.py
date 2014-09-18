# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpunsupportedmediatypeexception

class HttpUnsupportedMediaTypeException(HttpException):
    ## HTTPエラー。Unsupported Media Type.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpUnsupportedMediaTypeException, self).__init__(status, code, "HTTPエラー。Unsupported Media Type." if message is None or message == "" else message)
    
