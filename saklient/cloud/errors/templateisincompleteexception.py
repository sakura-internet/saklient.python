# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.templateisincompleteexception

class TemplateIsIncompleteException(HttpConflictException):
    ## 要求された操作を行えません。このテンプレートは不完全です。複製処理等の完了後に再度お試しください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(TemplateIsIncompleteException, self).__init__(status, code, "要求された操作を行えません。このテンプレートは不完全です。複製処理等の完了後に再度お試しください。" if message is None or message == "" else message)
    
