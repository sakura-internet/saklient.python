# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpbadrequestexception import HttpBadRequestException
import saklient

str = six.text_type
# module saklient.cloud.errors.paramresnotfoundexception

class ParamResNotFoundException(HttpBadRequestException):
    ## 不適切な要求です。パラメータで指定されたリソースが存在しません。IDをご確認ください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ParamResNotFoundException, self).__init__(status, code, "不適切な要求です。パラメータで指定されたリソースが存在しません。IDをご確認ください。" if message is None or message == "" else message)
    
