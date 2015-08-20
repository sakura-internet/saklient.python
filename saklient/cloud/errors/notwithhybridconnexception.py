# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.notwithhybridconnexception

class NotWithHybridconnException(HttpConflictException):
    ## 要求された操作を行えません。ハイブリッド接続と併用する場合はお問い合わせください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(NotWithHybridconnException, self).__init__(status, code, "要求された操作を行えません。ハイブリッド接続と併用する場合はお問い合わせください。" if message is None or message == "" else message)
    
