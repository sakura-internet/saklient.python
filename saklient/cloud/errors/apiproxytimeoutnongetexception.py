# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

from ...errors.httpgatewaytimeoutexception import HttpGatewayTimeoutException
import saklient

# module saklient.cloud.errors.apiproxytimeoutnongetexception

class ApiProxyTimeoutNonGetException(HttpGatewayTimeoutException):
    ## APIプロクシが応答しません。要求は実行された可能性があります。しばらく時間をおいてからご確認ください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ApiProxyTimeoutNonGetException, self).__init__(status, code, "APIプロクシが応答しません。要求は実行された可能性があります。しばらく時間をおいてからご確認ください。" if message is None or message == "" else message)
    
