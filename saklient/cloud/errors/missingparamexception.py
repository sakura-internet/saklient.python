# -*- coding:utf-8 -*-

from ...errors.httpbadrequestexception import HttpBadRequestException

# module saklient.cloud.errors.missingparamexception

class MissingParamException(HttpBadRequestException):
    ## 不適切な要求です。必要なパラメータが指定されていません。
    
    # (class field) default_message = "不適切な要求です。必要なパラメータが指定されていません。"
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(MissingParamException, self).__init__(status, code, message)
    
