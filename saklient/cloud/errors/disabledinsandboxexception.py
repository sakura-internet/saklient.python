# -*- coding:utf-8 -*-

from ...errors.httpforbiddenexception import HttpForbiddenException

# module saklient.cloud.errors.disabledinsandboxexception

class DisabledInSandboxException(HttpForbiddenException):
    ## 要求された操作は許可されていません。このゾーンではこの操作は禁止されています。他のゾーンでお試しください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DisabledInSandboxException, self).__init__(status, code, "要求された操作は許可されていません。このゾーンではこの操作は禁止されています。他のゾーンでお試しください。" if message is None or message == "" else message)
    
