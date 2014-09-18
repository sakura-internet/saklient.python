# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.resalreadyexistsexception

class ResAlreadyExistsException(HttpConflictException):
    ## 要求された操作を行えません。このIDのリソースは既に存在します。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ResAlreadyExistsException, self).__init__(status, code, "要求された操作を行えません。このIDのリソースは既に存在します。" if message is None or message == "" else message)
    
