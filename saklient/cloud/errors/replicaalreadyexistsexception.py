# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.replicaalreadyexistsexception

class ReplicaAlreadyExistsException(HttpConflictException):
    ## 要求された操作を行えません。このストレージには指定リソースの複製が既に存在します。
    
    # (class field) default_message = "要求された操作を行えません。このストレージには指定リソースの複製が既に存在します。"
    
    pass
