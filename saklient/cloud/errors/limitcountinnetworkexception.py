# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.limitcountinnetworkexception

class LimitCountInNetworkException(HttpConflictException):
    ## 要求を受け付けできません。ネットワーク内リソース数上限により、リソースの割り当てに失敗しました。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(LimitCountInNetworkException, self).__init__(status, code, "要求を受け付けできません。ネットワーク内リソース数上限により、リソースの割り当てに失敗しました。" if message is None or message == "" else message)
    
