# -*- coding:utf-8 -*-

from ...errors.httpforbiddenexception import HttpForbiddenException

# module saklient.cloud.errors.accesssakuraexception

class AccessSakuraException(HttpForbiddenException):
    ## 要求された操作は許可されていません。さくらインターネットの会員メニューより認証後に実行してください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(AccessSakuraException, self).__init__(status, code, "要求された操作は許可されていません。さくらインターネットの会員メニューより認証後に実行してください。" if message is None or message == "" else message)
    
