# -*- coding:utf-8 -*-

from ...errors.httpforbiddenexception import HttpForbiddenException

# module saklient.cloud.errors.accesstokenexception

class AccessTokenException(HttpForbiddenException):
    ## 要求された操作は許可されていません。この操作は有効期限内のトークンが必要です。
    
    # (class field) default_message = "要求された操作は許可されていません。この操作は有効期限内のトークンが必要です。"
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(AccessTokenException, self).__init__(status, code, message)
    
