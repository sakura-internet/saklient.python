# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpnotextendedexception

class HttpNotExtendedException(HttpException):
    ## HTTPエラー。Not Extended.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpNotExtendedException, self).__init__(status, code, "HTTPエラー。Not Extended." if message is None or message == "" else message)
    
