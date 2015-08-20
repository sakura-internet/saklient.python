# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.deleterouterb4switchexception

class DeleteRouterB4SwitchException(HttpConflictException):
    ## 要求された操作を行えません。ルータを削除することでスイッチは同時に削除されます。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DeleteRouterB4SwitchException, self).__init__(status, code, "要求された操作を行えません。ルータを削除することでスイッチは同時に削除されます。" if message is None or message == "" else message)
    
