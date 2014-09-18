# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpmethodnotallowedexception

class HttpMethodNotAllowedException(HttpException):
    ## 要求されたHTTPメソッドは対応していません。
    
    # (class field) default_message = "要求されたHTTPメソッドは対応していません。"
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpMethodNotAllowedException, self).__init__(status, code, message)
    
