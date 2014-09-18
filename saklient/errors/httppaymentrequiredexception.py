# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httppaymentrequiredexception

class HttpPaymentRequiredException(HttpException):
    ## HTTPエラー。Payment Required.
    
    # (class field) default_message = "HTTPエラー。Payment Required."
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpPaymentRequiredException, self).__init__(status, code, message)
    
