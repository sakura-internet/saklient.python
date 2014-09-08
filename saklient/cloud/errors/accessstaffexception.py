# -*- coding:utf-8 -*-

from ...errors.httpforbiddenexception import HttpForbiddenException

# module saklient.cloud.errors.accessstaffexception

class AccessStaffException(HttpForbiddenException):
    ## 要求された操作は許可されていません。権限エラー。
    
    # (class field) default_message = "要求された操作は許可されていません。権限エラー。"
    
    pass
