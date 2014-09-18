# -*- coding:utf-8 -*-

from ...errors.httpbadrequestexception import HttpBadRequestException

# module saklient.cloud.errors.paramipnotfoundexception

class ParamIpNotFoundException(HttpBadRequestException):
    ## 不適切な要求です。パラメータで指定されたIPアドレスを含むネットワークが存在しません。
    
    # (class field) default_message = "不適切な要求です。パラメータで指定されたIPアドレスを含むネットワークが存在しません。"
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ParamIpNotFoundException, self).__init__(status, code, message)
    
