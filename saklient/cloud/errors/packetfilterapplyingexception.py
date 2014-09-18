# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.packetfilterapplyingexception

class PacketFilterApplyingException(HttpConflictException):
    ## 要求された操作を行えません。起動中のサーバに対して変更されたパケットフィルタを反映するタスクが既に実行中です。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(PacketFilterApplyingException, self).__init__(status, code, "要求された操作を行えません。起動中のサーバに対して変更されたパケットフィルタを反映するタスクが既に実行中です。" if message is None or message == "" else message)
    
