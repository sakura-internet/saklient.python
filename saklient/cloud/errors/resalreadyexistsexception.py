# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.resalreadyexistsexception

class ResAlreadyExistsException(HttpConflictException):
    ## 要求された操作を行えません。このIDのリソースは既に存在します。
    
    # (class field) default_message = "要求された操作を行えません。このIDのリソースは既に存在します。"
    
    pass
