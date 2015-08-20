# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpbadrequestexception import HttpBadRequestException
import saklient

str = six.text_type
# module saklient.cloud.errors.cantresizesmallerexception

class CantResizeSmallerException(HttpBadRequestException):
    ## 不適切な要求です。現在の容量よりも小さくリサイズすることはできません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(CantResizeSmallerException, self).__init__(status, code, "不適切な要求です。現在の容量よりも小さくリサイズすることはできません。" if message is None or message == "" else message)
    
