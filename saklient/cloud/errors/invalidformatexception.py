# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpbadrequestexception import HttpBadRequestException
import saklient

str = six.text_type
# module saklient.cloud.errors.invalidformatexception

class InvalidFormatException(HttpBadRequestException):
    ## 不適切な要求です。パラメータに含まれている値のフォーマットが一部不正です。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(InvalidFormatException, self).__init__(status, code, "不適切な要求です。パラメータに含まれている値のフォーマットが一部不正です。" if message is None or message == "" else message)
    
