# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

from .httpexception import HttpException
import saklient

# module saklient.errors.httpnotimplementedexception

class HttpNotImplementedException(HttpException):
    ## HTTPエラー。Not Implemented.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpNotImplementedException, self).__init__(status, code, "HTTPエラー。Not Implemented." if message is None or message == "" else message)
    
