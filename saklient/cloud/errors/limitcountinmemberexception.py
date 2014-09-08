# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.limitcountinmemberexception

class LimitCountInMemberException(HttpConflictException):
    ## 要求を受け付けできません。アカウント数上限により作成失敗しました。
    
    # (class field) default_message = "要求を受け付けできません。アカウント数上限により作成失敗しました。"
    
    pass
