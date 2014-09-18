# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.connecttosameswitchexception

class ConnectToSameSwitchException(HttpConflictException):
    ## 要求された操作を行えません。複数のインタフェースから同一のスイッチに接続することはできません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ConnectToSameSwitchException, self).__init__(status, code, "要求された操作を行えません。複数のインタフェースから同一のスイッチに接続することはできません。" if message is None or message == "" else message)
    
