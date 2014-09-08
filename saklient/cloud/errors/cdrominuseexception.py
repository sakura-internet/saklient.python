# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.cdrominuseexception

class CdromInUseException(HttpConflictException):
    ## 要求された操作を行えません。ISOイメージをサーバから排出後に実行してください。
    
    # (class field) default_message = "要求された操作を行えません。ISOイメージをサーバから排出後に実行してください。"
    
    pass
