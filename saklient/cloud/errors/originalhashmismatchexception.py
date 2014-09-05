# -*- coding:utf-8 -*-

from saklient.errors.httpconflictexception import HttpConflictException
from saklient.errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.originalhashmismatchexception

class OriginalHashMismatchException(HttpConflictException):
    ## 要求された操作を行えません。オリジナルのデータを取得してからこのリクエストを行うまでの間に、他の変更が加わった可能性があります。
    
    # (class field) default_message = "要求された操作を行えません。オリジナルのデータを取得してからこのリクエストを行うまでの間に、他の変更が加わった可能性があります。"
    
    pass
