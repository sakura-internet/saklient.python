# -*- coding:utf-8 -*-

from ...errors.httpbadrequestexception import HttpBadRequestException

# module saklient.cloud.errors.copytoitselfexception

class CopyToItselfException(HttpBadRequestException):
    ## 不適切な要求です。自分自身をソースとするコピーはできません。
    
    # (class field) default_message = "不適切な要求です。自分自身をソースとするコピーはできません。"
    
    pass
