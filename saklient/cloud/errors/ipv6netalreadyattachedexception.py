# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.ipv6netalreadyattachedexception

class IpV6NetAlreadyAttachedException(HttpConflictException):
    ## 要求された操作を行えません。ConnectedなIPv6ネットワークが既に割り当て済みです。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(IpV6NetAlreadyAttachedException, self).__init__(status, code, "要求された操作を行えません。ConnectedなIPv6ネットワークが既に割り当て済みです。" if message is None or message == "" else message)
    
