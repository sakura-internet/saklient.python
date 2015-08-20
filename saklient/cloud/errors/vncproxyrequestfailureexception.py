# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpserviceunavailableexception import HttpServiceUnavailableException
import saklient

str = six.text_type
# module saklient.cloud.errors.vncproxyrequestfailureexception

class VncProxyRequestFailureException(HttpServiceUnavailableException):
    ## サービスが利用できません。VNCプロクシの要求に失敗しました。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(VncProxyRequestFailureException, self).__init__(status, code, "サービスが利用できません。VNCプロクシの要求に失敗しました。" if message is None or message == "" else message)
    
