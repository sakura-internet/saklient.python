# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.replicaalreadyexistsexception

class ReplicaAlreadyExistsException(HttpConflictException):
    ## 要求された操作を行えません。このストレージには指定リソースの複製が既に存在します。
    
    # (class field) default_message = "要求された操作を行えません。このストレージには指定リソースの複製が既に存在します。"
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ReplicaAlreadyExistsException, self).__init__(status, code, message)
    
