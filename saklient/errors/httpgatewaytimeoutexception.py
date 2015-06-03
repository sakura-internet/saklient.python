# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

from .httpexception import HttpException
import saklient

# module saklient.errors.httpgatewaytimeoutexception

class HttpGatewayTimeoutException(HttpException):
    ## HTTPエラー。Gateway Timeout.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpGatewayTimeoutException, self).__init__(status, code, "HTTPエラー。Gateway Timeout." if message is None or message == "" else message)
    
