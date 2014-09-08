# -*- coding:utf-8 -*-

from ...errors.httpbadrequestexception import HttpBadRequestException

# module saklient.cloud.errors.invalidparamcombexception

class InvalidParamCombException(HttpBadRequestException):
    ## 不適切な要求です。同時に指定できないパラメータが含まれています。
    
    # (class field) default_message = "不適切な要求です。同時に指定できないパラメータが含まれています。"
    
    pass
