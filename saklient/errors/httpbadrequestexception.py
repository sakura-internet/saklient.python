# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpbadrequestexception

class HttpBadRequestException(HttpException):
    ## 不適切な要求です。パラメータの指定誤り、入力規則違反です。入力内容をご確認ください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpBadRequestException, self).__init__(status, code, "不適切な要求です。パラメータの指定誤り、入力規則違反です。入力内容をご確認ください。" if message is None or message == "" else message)
    
