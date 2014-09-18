# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.serveriscleaningexception

class ServerIsCleaningException(HttpConflictException):
    ## 要求された操作を行えません。サーバが終了処理中です。しばらく時間をおいてから再度お試しください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ServerIsCleaningException, self).__init__(status, code, "要求された操作を行えません。サーバが終了処理中です。しばらく時間をおいてから再度お試しください。" if message is None or message == "" else message)
    
