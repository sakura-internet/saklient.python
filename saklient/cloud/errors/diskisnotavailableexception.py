# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.diskisnotavailableexception

class DiskIsNotAvailableException(HttpConflictException):
    ## 要求された操作を行えません。ディスクが利用可能な状態ではありません。コピー処理等の完了後に再度お試しください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DiskIsNotAvailableException, self).__init__(status, code, "要求された操作を行えません。ディスクが利用可能な状態ではありません。コピー処理等の完了後に再度お試しください。" if message is None or message == "" else message)
    
