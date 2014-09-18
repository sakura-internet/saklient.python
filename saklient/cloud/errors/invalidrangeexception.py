# -*- coding:utf-8 -*-

from ...errors.httpbadrequestexception import HttpBadRequestException

# module saklient.cloud.errors.invalidrangeexception

class InvalidRangeException(HttpBadRequestException):
    ## 不適切な要求です。パラメータに含まれている値の範囲が一部不正です。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(InvalidRangeException, self).__init__(status, code, "不適切な要求です。パラメータに含まれている値の範囲が一部不正です。" if message is None or message == "" else message)
    
