# -*- coding:utf-8 -*-

from ...errors.httpforbiddenexception import HttpForbiddenException

# module saklient.cloud.errors.accessapikeydisabledexception

class AccessApiKeyDisabledException(HttpForbiddenException):
    ## 要求された操作は許可されていません。APIキーによるアクセスはできません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(AccessApiKeyDisabledException, self).__init__(status, code, "要求された操作は許可されていません。APIキーによるアクセスはできません。" if message is None or message == "" else message)
    
