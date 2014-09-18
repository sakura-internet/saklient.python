# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.disconnectb4updateexception

class DisconnectB4UpdateException(HttpConflictException):
    ## 要求された操作を行えません。サーバと接続された状態では変更できない値が含まれています。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DisconnectB4UpdateException, self).__init__(status, code, "要求された操作を行えません。サーバと接続された状態では変更できない値が含まれています。" if message is None or message == "" else message)
    
