# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.duplicateaccountcodeexception

class DuplicateAccountCodeException(HttpConflictException):
    ## 要求された操作を行えません。同一アカウント名で複数のアカウントを作成することはできません。
    
    # (class field) default_message = "要求された操作を行えません。同一アカウント名で複数のアカウントを作成することはできません。"
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DuplicateAccountCodeException, self).__init__(status, code, message)
    
