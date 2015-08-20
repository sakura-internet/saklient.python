# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpforbiddenexception import HttpForbiddenException
import saklient

str = six.text_type
# module saklient.cloud.errors.accessstaffexception

class AccessStaffException(HttpForbiddenException):
    ## 要求された操作は許可されていません。権限エラー。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(AccessStaffException, self).__init__(status, code, "要求された操作は許可されていません。権限エラー。" if message is None or message == "" else message)
    
