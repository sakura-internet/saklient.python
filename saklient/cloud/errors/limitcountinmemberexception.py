# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.limitcountinmemberexception

class LimitCountInMemberException(HttpConflictException):
    ## 要求を受け付けできません。アカウント数上限により作成失敗しました。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(LimitCountInMemberException, self).__init__(status, code, "要求を受け付けできません。アカウント数上限により作成失敗しました。" if message is None or message == "" else message)
    
