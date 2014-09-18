# -*- coding:utf-8 -*-

from ...errors.httpgatewaytimeoutexception import HttpGatewayTimeoutException

# module saklient.cloud.errors.apiproxytimeoutnongetexception

class ApiProxyTimeoutNonGetException(HttpGatewayTimeoutException):
    ## APIプロクシが応答しません。要求は実行された可能性があります。しばらく時間をおいてからご確認ください。
    
    # (class field) default_message = "APIプロクシが応答しません。要求は実行された可能性があります。しばらく時間をおいてからご確認ください。"
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(ApiProxyTimeoutNonGetException, self).__init__(status, code, message)
    
