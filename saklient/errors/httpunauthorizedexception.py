# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpunauthorizedexception

class HttpUnauthorizedException(HttpException):
    ## この操作は認証が必要です。IDまたはパスワードが誤っている可能性があります。
    
    # (class field) default_message = "この操作は認証が必要です。IDまたはパスワードが誤っている可能性があります。"
    
    pass
