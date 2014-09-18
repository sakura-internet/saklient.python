# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpbadgatewayexception

class HttpBadGatewayException(HttpException):
    ## HTTPエラー。Bad Gateway.
    
    # (class field) default_message = "HTTPエラー。Bad Gateway."
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpBadGatewayException, self).__init__(status, code, message)
    
