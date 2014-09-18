# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.notwithhybridconnexception

class NotWithHybridconnException(HttpConflictException):
    ## 要求された操作を行えません。ハイブリッド接続と併用する場合はお問い合わせください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(NotWithHybridconnException, self).__init__(status, code, "要求された操作を行えません。ハイブリッド接続と併用する場合はお問い合わせください。" if message is None or message == "" else message)
    
