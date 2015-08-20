# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpbadrequestexception import HttpBadRequestException
import saklient

str = six.text_type
# module saklient.cloud.errors.filterbadoperatorexception

class FilterBadOperatorException(HttpBadRequestException):
    ## 不適切な要求です。フィールドの型に対応していない演算子がフィルタ中に含まれています。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(FilterBadOperatorException, self).__init__(status, code, "不適切な要求です。フィールドの型に対応していない演算子がフィルタ中に含まれています。" if message is None or message == "" else message)
    
