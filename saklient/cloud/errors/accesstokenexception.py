# -*- coding:utf-8 -*-

from saklient.errors.httpforbiddenexception import HttpForbiddenException
from saklient.errors.httpforbiddenexception import HttpForbiddenException

# module saklient.cloud.errors.accesstokenexception

class AccessTokenException(HttpForbiddenException):
    ## 要求された操作は許可されていません。この操作は有効期限内のトークンが必要です。
    
    # (class field) default_message = "要求された操作は許可されていません。この操作は有効期限内のトークンが必要です。"
    
    pass
