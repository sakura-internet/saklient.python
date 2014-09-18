# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.limitmemoryinaccountexception

class LimitMemoryInAccountException(HttpConflictException):
    ## 要求を受け付けできません。アカウントあたりの全サーバメモリサイズ上限により、リソースの割り当てに失敗しました。
    
    # (class field) default_message = "要求を受け付けできません。アカウントあたりの全サーバメモリサイズ上限により、リソースの割り当てに失敗しました。"
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(LimitMemoryInAccountException, self).__init__(status, code, message)
    
