# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpgatewaytimeoutexception

class HttpGatewayTimeoutException(HttpException):
    ## HTTPエラー。Gateway Timeout.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpGatewayTimeoutException, self).__init__(status, code, "HTTPエラー。Gateway Timeout." if message is None or message == "" else message)
    
