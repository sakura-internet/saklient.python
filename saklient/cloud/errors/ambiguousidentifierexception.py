# -*- coding:utf-8 -*-

from ...errors.httpnotfoundexception import HttpNotFoundException

# module saklient.cloud.errors.ambiguousidentifierexception

class AmbiguousIdentifierException(HttpNotFoundException):
    ## 対象が見つかりません。識別名から一意にリソースを特定できません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(AmbiguousIdentifierException, self).__init__(status, code, "対象が見つかりません。識別名から一意にリソースを特定できません。" if message is None or message == "" else message)
    
