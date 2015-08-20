# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.duplicateentryexception

class DuplicateEntryException(HttpConflictException):
    ## 要求された操作を行えません。リソースが既に存在するか、リソース同士が既に関連付けられています。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DuplicateEntryException, self).__init__(status, code, "要求された操作を行えません。リソースが既に存在するか、リソース同士が既に関連付けられています。" if message is None or message == "" else message)
    
