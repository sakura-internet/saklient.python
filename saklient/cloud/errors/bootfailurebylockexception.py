# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpserviceunavailableexception import HttpServiceUnavailableException
import saklient

str = six.text_type
# module saklient.cloud.errors.bootfailurebylockexception

class BootFailureByLockException(HttpServiceUnavailableException):
    ## サービスが利用できません。サーバが予期せず終了したため、ロックされています。しばらく時間をおいてから再度お試しください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(BootFailureByLockException, self).__init__(status, code, "サービスが利用できません。サーバが予期せず終了したため、ロックされています。しばらく時間をおいてから再度お試しください。" if message is None or message == "" else message)
    
