# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.limitcountinaccountexception

class LimitCountInAccountException(HttpConflictException):
    ## 要求を受け付けできません。アカウントあたりのリソース数上限により、リソースの割り当てに失敗しました。
    
    # (class field) default_message = "要求を受け付けできません。アカウントあたりのリソース数上限により、リソースの割り当てに失敗しました。"
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(LimitCountInAccountException, self).__init__(status, code, message)
    
