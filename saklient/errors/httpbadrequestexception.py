# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from .httpexception import HttpException
import saklient

str = six.text_type
# module saklient.errors.httpbadrequestexception

class HttpBadRequestException(HttpException):
    ## 不適切な要求です。パラメータの指定誤り、入力規則違反です。入力内容をご確認ください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpBadRequestException, self).__init__(status, code, "不適切な要求です。パラメータの指定誤り、入力規則違反です。入力内容をご確認ください。" if message is None or message == "" else message)
    
