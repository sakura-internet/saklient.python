# -*- coding:utf-8 -*-

from saklient.errors.httpconflictexception import HttpConflictException
from saklient.errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.packetfilterapplyingexception

class PacketFilterApplyingException(HttpConflictException):
    ## 要求された操作を行えません。起動中のサーバに対して変更されたパケットフィルタを反映するタスクが既に実行中です。
    
    # (class field) default_message = "要求された操作を行えません。起動中のサーバに対して変更されたパケットフィルタを反映するタスクが既に実行中です。"
    
    pass
