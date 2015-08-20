# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpserviceunavailableexception import HttpServiceUnavailableException
import saklient

str = six.text_type
# module saklient.cloud.errors.diskstockrunoutexception

class DiskStockRunOutException(HttpServiceUnavailableException):
    ## サービスが利用できません。作成済みディスクを確保できませんでした。サーバが混雑している可能性があります。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DiskStockRunOutException, self).__init__(status, code, "サービスが利用できません。作成済みディスクを確保できませんでした。サーバが混雑している可能性があります。" if message is None or message == "" else message)
    
