# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.cdrominuseexception

class CdromInUseException(HttpConflictException):
    ## 要求された操作を行えません。ISOイメージをサーバから排出後に実行してください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(CdromInUseException, self).__init__(status, code, "要求された操作を行えません。ISOイメージをサーバから排出後に実行してください。" if message is None or message == "" else message)
    
