# -*- coding:utf-8 -*-

from ...errors.httpforbiddenexception import HttpForbiddenException

# module saklient.cloud.errors.accesssakuraexception

class AccessSakuraException(HttpForbiddenException):
    ## 要求された操作は許可されていません。さくらインターネットの会員メニューより認証後に実行してください。
    
    # (class field) default_message = "要求された操作は許可されていません。さくらインターネットの会員メニューより認証後に実行してください。"
    
    pass
