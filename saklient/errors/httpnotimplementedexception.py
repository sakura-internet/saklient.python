# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpnotimplementedexception

class HttpNotImplementedException(HttpException):
    ## HTTPエラー。Not Implemented.
    
    # (class field) default_message = "HTTPエラー。Not Implemented."
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpNotImplementedException, self).__init__(status, code, message)
    
