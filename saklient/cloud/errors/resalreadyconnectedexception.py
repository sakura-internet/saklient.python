# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.resalreadyconnectedexception

class ResAlreadyConnectedException(HttpConflictException):
    ## 要求された操作を行えません。このリソースは他のリソースと既に接続されています。
    
    # (class field) default_message = "要求された操作を行えません。このリソースは他のリソースと既に接続されています。"
    
    pass
