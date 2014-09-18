# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httplengthrequiredexception

class HttpLengthRequiredException(HttpException):
    ## HTTPエラー。Length Required.
    
    # (class field) default_message = "HTTPエラー。Length Required."
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpLengthRequiredException, self).__init__(status, code, message)
    
