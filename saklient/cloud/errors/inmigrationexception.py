# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.inmigrationexception

class InMigrationException(HttpConflictException):
    ## 要求された操作を行えません。このリソースから他のリソースへのコピー処理が進行中です。完了後に再度お試しください。
    
    # (class field) default_message = "要求された操作を行えません。このリソースから他のリソースへのコピー処理が進行中です。完了後に再度お試しください。"
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(InMigrationException, self).__init__(status, code, message)
    
