# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.notreplicatingexception

class NotReplicatingException(HttpConflictException):
    ## 要求された操作を行えません。このストレージ上への指定リソースの複製は実行されていません。
    
    # (class field) default_message = "要求された操作を行えません。このストレージ上への指定リソースの複製は実行されていません。"
    
    pass
