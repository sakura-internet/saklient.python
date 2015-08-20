# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from .httpexception import HttpException
import saklient

str = six.text_type
# module saklient.errors.httpmethodnotallowedexception

class HttpMethodNotAllowedException(HttpException):
    ## 要求されたHTTPメソッドは対応していません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpMethodNotAllowedException, self).__init__(status, code, "要求されたHTTPメソッドは対応していません。" if message is None or message == "" else message)
    
