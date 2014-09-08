# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.resusedinzoneexception

class ResUsedInZoneException(HttpConflictException):
    ## 要求された操作を行えません。同一ゾーン内の他のリソースが既にこのリソースを使用中です。
    
    # (class field) default_message = "要求された操作を行えません。同一ゾーン内の他のリソースが既にこのリソースを使用中です。"
    
    pass
