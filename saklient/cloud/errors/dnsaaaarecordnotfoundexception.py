# -*- coding:utf-8 -*-

from ...errors.httpbadrequestexception import HttpBadRequestException

# module saklient.cloud.errors.dnsaaaarecordnotfoundexception

class DnsAaaaRecordNotFoundException(HttpBadRequestException):
    ## 不適切な要求です。対応するAAAAレコードが見つかりません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(DnsAaaaRecordNotFoundException, self).__init__(status, code, "不適切な要求です。対応するAAAAレコードが見つかりません。" if message is None or message == "" else message)
    
