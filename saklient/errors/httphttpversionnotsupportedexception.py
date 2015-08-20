# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from .httpexception import HttpException
import saklient

str = six.text_type
# module saklient.errors.httphttpversionnotsupportedexception

class HttpHttpVersionNotSupportedException(HttpException):
    ## HTTPエラー。Http Version Not Supported.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpHttpVersionNotSupportedException, self).__init__(status, code, "HTTPエラー。Http Version Not Supported." if message is None or message == "" else message)
    
