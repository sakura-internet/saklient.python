# -*- coding:utf-8 -*-

from saklient.errors.httpconflictexception import HttpConflictException
from saklient.errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.illegaldasusageexception

class IllegalDasUsageException(HttpConflictException):
    ## 要求された操作を行えません。DASの利用方法に問題があります。1台のサーバには同一のストレージ上にあるDASのみを接続できます。
    
    # (class field) default_message = "要求された操作を行えません。DASの利用方法に問題があります。1台のサーバには同一のストレージ上にあるDASのみを接続できます。"
    
    pass
