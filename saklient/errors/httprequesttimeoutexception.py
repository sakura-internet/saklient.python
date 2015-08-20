# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from .httpexception import HttpException
import saklient

str = six.text_type
# module saklient.errors.httprequesttimeoutexception

class HttpRequestTimeoutException(HttpException):
    ## HTTPエラー。Request Timeout.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpRequestTimeoutException, self).__init__(status, code, "HTTPエラー。Request Timeout." if message is None or message == "" else message)
    
