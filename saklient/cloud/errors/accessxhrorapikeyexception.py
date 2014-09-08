# -*- coding:utf-8 -*-

from ...errors.httpforbiddenexception import HttpForbiddenException

# module saklient.cloud.errors.accessxhrorapikeyexception

class AccessXhrOrApiKeyException(HttpForbiddenException):
    ## 要求された操作は許可されていません。XHRまたはAPIキーによるアクセスのみ許可されています。
    
    # (class field) default_message = "要求された操作は許可されていません。XHRまたはAPIキーによるアクセスのみ許可されています。"
    
    pass
