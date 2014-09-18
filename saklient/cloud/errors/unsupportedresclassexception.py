# -*- coding:utf-8 -*-

from ...errors.httpbadrequestexception import HttpBadRequestException

# module saklient.cloud.errors.unsupportedresclassexception

class UnsupportedResClassException(HttpBadRequestException):
    ## 不適切な要求です。この種類のリソースは要求された操作に対応しません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(UnsupportedResClassException, self).__init__(status, code, "不適切な要求です。この種類のリソースは要求された操作に対応しません。" if message is None or message == "" else message)
    
