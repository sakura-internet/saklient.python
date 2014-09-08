# -*- coding:utf-8 -*-

from ...errors.httpforbiddenexception import HttpForbiddenException

# module saklient.cloud.errors.accountnotspecifiedexception

class AccountNotSpecifiedException(HttpForbiddenException):
    ## 要求された操作は許可されていません。このAPIはアカウントを特定できる認証方法でアクセスする必要があります。
    
    # (class field) default_message = "要求された操作は許可されていません。このAPIはアカウントを特定できる認証方法でアクセスする必要があります。"
    
    pass
