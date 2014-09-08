# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.resalreadydisconnectedexception

class ResAlreadyDisconnectedException(HttpConflictException):
    ## 要求された操作を行えません。このリソースは既に切断されています。
    
    # (class field) default_message = "要求された操作を行えません。このリソースは既に切断されています。"
    
    pass
