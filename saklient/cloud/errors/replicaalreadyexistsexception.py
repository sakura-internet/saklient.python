# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpconflictexception import HttpConflictException
import saklient

str = six.text_type
# module saklient.cloud.errors.replicaalreadyexistsexception

class ReplicaAlreadyExistsException(HttpConflictException):
    ## 要求された操作を行えません。このストレージには指定リソースの複製が既に存在します。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ReplicaAlreadyExistsException, self).__init__(status, code, "要求された操作を行えません。このストレージには指定リソースの複製が既に存在します。" if message is None or message == "" else message)
    
