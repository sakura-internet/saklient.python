# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from .httpexception import HttpException
import saklient

str = six.text_type
# module saklient.errors.httpforbiddenexception

class HttpForbiddenException(HttpException):
    ## 要求された操作は許可されていません。権限エラー。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpForbiddenException, self).__init__(status, code, "要求された操作は許可されていません。権限エラー。" if message is None or message == "" else message)
    
