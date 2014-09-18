# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.missingisoimageexception

class MissingIsoImageException(HttpConflictException):
    ## 要求された操作を行えません。ISOイメージが見つかりません。イメージを正しくアップロードし、FTP共有を終了した後に再度お試しください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(MissingIsoImageException, self).__init__(status, code, "要求された操作を行えません。ISOイメージが見つかりません。イメージを正しくアップロードし、FTP共有を終了した後に再度お試しください。" if message is None or message == "" else message)
    
