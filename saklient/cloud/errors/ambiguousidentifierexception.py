# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpnotfoundexception import HttpNotFoundException
import saklient

str = six.text_type
# module saklient.cloud.errors.ambiguousidentifierexception

class AmbiguousIdentifierException(HttpNotFoundException):
    ## 対象が見つかりません。識別名から一意にリソースを特定できません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(AmbiguousIdentifierException, self).__init__(status, code, "対象が見つかりません。識別名から一意にリソースを特定できません。" if message is None or message == "" else message)
    
