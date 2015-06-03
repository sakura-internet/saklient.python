# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

from ...errors.httpconflictexception import HttpConflictException
import saklient

# module saklient.cloud.errors.archiveisincompleteexception

class ArchiveIsIncompleteException(HttpConflictException):
    ## 要求された操作を行えません。このアーカイブは不完全です。複製処理等の完了後に再度お試しください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ArchiveIsIncompleteException, self).__init__(status, code, "要求された操作を行えません。このアーカイブは不完全です。複製処理等の完了後に再度お試しください。" if message is None or message == "" else message)
    
