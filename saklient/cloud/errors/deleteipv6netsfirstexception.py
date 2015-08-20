# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.deleteipv6netsfirstexception

class DeleteIpV6NetsFirstException(HttpConflictException):
    ## 要求された操作を行えません。ルータを削除する前に、IPv6ネットワークの割当を解除してください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DeleteIpV6NetsFirstException, self).__init__(status, code, "要求された操作を行えません。ルータを削除する前に、IPv6ネットワークの割当を解除してください。" if message is None or message == "" else message)
    
