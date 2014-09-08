# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.cdromdisabledexception

class CdromDisabledException(HttpConflictException):
    ## 要求された操作を行えません。ISOイメージが無効化されています。排出後に再度お試しください。
    
    # (class field) default_message = "要求された操作を行えません。ISOイメージが無効化されています。排出後に再度お試しください。"
    
    pass
