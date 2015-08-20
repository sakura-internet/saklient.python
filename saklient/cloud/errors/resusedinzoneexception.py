# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.resusedinzoneexception

class ResUsedInZoneException(HttpConflictException):
    ## 要求された操作を行えません。同一ゾーン内の他のリソースが既にこのリソースを使用中です。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ResUsedInZoneException, self).__init__(status, code, "要求された操作を行えません。同一ゾーン内の他のリソースが既にこのリソースを使用中です。" if message is None or message == "" else message)
    
