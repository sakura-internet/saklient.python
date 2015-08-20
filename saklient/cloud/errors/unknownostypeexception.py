# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpserviceunavailableexception import HttpServiceUnavailableException
import saklient

str = six.text_type
# module saklient.cloud.errors.unknownostypeexception

class UnknownOsTypeException(HttpServiceUnavailableException):
    ## サービスが利用できません。ディスクにインストールされたOSが特定できないため、正しく修正できません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(UnknownOsTypeException, self).__init__(status, code, "サービスが利用できません。ディスクにインストールされたOSが特定できないため、正しく修正できません。" if message is None or message == "" else message)
    
