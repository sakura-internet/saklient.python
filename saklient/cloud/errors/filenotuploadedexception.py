# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.filenotuploadedexception

class FileNotUploadedException(HttpConflictException):
    ## 要求された操作を行えません。ファイルをアップロード後に実行してください。
    
    # (class field) default_message = "要求された操作を行えません。ファイルをアップロード後に実行してください。"
    
    pass
