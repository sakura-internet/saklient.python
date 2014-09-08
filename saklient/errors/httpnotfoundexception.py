# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpnotfoundexception

class HttpNotFoundException(HttpException):
    ## 対象が見つかりません。対象は利用できない状態か、IDまたはパスに誤りがあります。
    
    # (class field) default_message = "対象が見つかりません。対象は利用できない状態か、IDまたはパスに誤りがあります。"
    
    pass
