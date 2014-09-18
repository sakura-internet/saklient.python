# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httphttpversionnotsupportedexception

class HttpHttpVersionNotSupportedException(HttpException):
    ## HTTPエラー。Http Version Not Supported.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpHttpVersionNotSupportedException, self).__init__(status, code, "HTTPエラー。Http Version Not Supported." if message is None or message == "" else message)
    
