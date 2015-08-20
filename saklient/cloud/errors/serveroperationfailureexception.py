# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpserviceunavailableexception import HttpServiceUnavailableException
import saklient

str = six.text_type
# module saklient.cloud.errors.serveroperationfailureexception

class ServerOperationFailureException(HttpServiceUnavailableException):
    ## サービスが利用できません。サーバの操作に失敗しました。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ServerOperationFailureException, self).__init__(status, code, "サービスが利用できません。サーバの操作に失敗しました。" if message is None or message == "" else message)
    
