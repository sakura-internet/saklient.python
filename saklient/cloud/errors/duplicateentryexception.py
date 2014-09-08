# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.duplicateentryexception

class DuplicateEntryException(HttpConflictException):
    ## 要求された操作を行えません。リソースが既に存在するか、リソース同士が既に関連付けられています。
    
    # (class field) default_message = "要求された操作を行えません。リソースが既に存在するか、リソース同士が既に関連付けられています。"
    
    pass
