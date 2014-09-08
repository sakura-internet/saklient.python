# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.duplicateaccountcodeexception

class DuplicateAccountCodeException(HttpConflictException):
    ## 要求された操作を行えません。同一アカウント名で複数のアカウントを作成することはできません。
    
    # (class field) default_message = "要求された操作を行えません。同一アカウント名で複数のアカウントを作成することはできません。"
    
    pass
