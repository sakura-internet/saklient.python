# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.ftpisalreadycloseexception

class FtpIsAlreadyCloseException(HttpConflictException):
    ## 要求された操作を行えません。FTP共有は既に終了されています。
    
    # (class field) default_message = "要求された操作を行えません。FTP共有は既に終了されています。"
    
    pass
