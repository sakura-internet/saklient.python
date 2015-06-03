# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

from .httpexception import HttpException
import saklient

# module saklient.errors.httprequesttimeoutexception

class HttpRequestTimeoutException(HttpException):
    ## HTTPエラー。Request Timeout.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpRequestTimeoutException, self).__init__(status, code, "HTTPエラー。Request Timeout." if message is None or message == "" else message)
    
