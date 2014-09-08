# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.limitcountinzoneexception

class LimitCountInZoneException(HttpConflictException):
    ## 要求を受け付けできません。ゾーン内リソース数上限により、リソースの割り当てに失敗しました。
    
    # (class field) default_message = "要求を受け付けできません。ゾーン内リソース数上限により、リソースの割り当てに失敗しました。"
    
    pass
