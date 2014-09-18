# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.ftpmustbeclosedexception

class FtpMustBeClosedException(HttpConflictException):
    ## 要求された操作を行えません。リソースのFTP共有を終了した後に実行してください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(FtpMustBeClosedException, self).__init__(status, code, "要求された操作を行えません。リソースのFTP共有を終了した後に実行してください。" if message is None or message == "" else message)
    
