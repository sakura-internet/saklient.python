# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.deleteresb4accountexception

class DeleteResB4AccountException(HttpConflictException):
    ## 要求された操作を行えません。現在のアカウントで使用している全てのリソースを削除した後に実行してください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DeleteResB4AccountException, self).__init__(status, code, "要求された操作を行えません。現在のアカウントで使用している全てのリソースを削除した後に実行してください。" if message is None or message == "" else message)
    
