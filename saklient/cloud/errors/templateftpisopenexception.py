# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.templateftpisopenexception

class TemplateFtpIsOpenException(HttpConflictException):
    ## 要求された操作を行えません。テンプレートのFTP共有を終了後に実行してください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(TemplateFtpIsOpenException, self).__init__(status, code, "要求された操作を行えません。テンプレートのFTP共有を終了後に実行してください。" if message is None or message == "" else message)
    
