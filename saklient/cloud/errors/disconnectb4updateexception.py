# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.disconnectb4updateexception

class DisconnectB4UpdateException(HttpConflictException):
    ## 要求された操作を行えません。サーバと接続された状態では変更できない値が含まれています。
    
    # (class field) default_message = "要求された操作を行えません。サーバと接続された状態では変更できない値が含まれています。"
    
    pass
