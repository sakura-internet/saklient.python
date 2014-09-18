# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.serverpowermustbeupexception

class ServerPowerMustBeUpException(HttpConflictException):
    ## 要求された操作を行えません。サーバが停止中にはこの操作を行えません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ServerPowerMustBeUpException, self).__init__(status, code, "要求された操作を行えません。サーバが停止中にはこの操作を行えません。" if message is None or message == "" else message)
    
