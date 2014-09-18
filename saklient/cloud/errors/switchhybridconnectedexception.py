# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.switchhybridconnectedexception

class SwitchHybridConnectedException(HttpConflictException):
    ## 要求された操作を行えません。ハイブリッド接続されているスイッチに対して、この操作はできません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(SwitchHybridConnectedException, self).__init__(status, code, "要求された操作を行えません。ハイブリッド接続されているスイッチに対して、この操作はできません。" if message is None or message == "" else message)
    
