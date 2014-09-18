# -*- coding:utf-8 -*-

from ...errors.httpforbiddenexception import HttpForbiddenException

# module saklient.cloud.errors.accessxhrorapikeyexception

class AccessXhrOrApiKeyException(HttpForbiddenException):
    ## 要求された操作は許可されていません。XHRまたはAPIキーによるアクセスのみ許可されています。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(AccessXhrOrApiKeyException, self).__init__(status, code, "要求された操作は許可されていません。XHRまたはAPIキーによるアクセスのみ許可されています。" if message is None or message == "" else message)
    
