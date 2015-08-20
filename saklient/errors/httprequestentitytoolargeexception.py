# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from .httpexception import HttpException
import saklient

str = six.text_type
# module saklient.errors.httprequestentitytoolargeexception

class HttpRequestEntityTooLargeException(HttpException):
    ## HTTPエラー。Request Entity Too Large.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpRequestEntityTooLargeException, self).__init__(status, code, "HTTPエラー。Request Entity Too Large." if message is None or message == "" else message)
    
