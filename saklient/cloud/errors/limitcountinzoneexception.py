# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.limitcountinzoneexception

class LimitCountInZoneException(HttpConflictException):
    ## 要求を受け付けできません。ゾーン内リソース数上限により、リソースの割り当てに失敗しました。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(LimitCountInZoneException, self).__init__(status, code, "要求を受け付けできません。ゾーン内リソース数上限により、リソースの割り当てに失敗しました。" if message is None or message == "" else message)
    
