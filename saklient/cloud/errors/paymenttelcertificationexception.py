# -*- coding:utf-8 -*-

from ...errors.httppaymentrequiredexception import HttpPaymentRequiredException

# module saklient.cloud.errors.paymenttelcertificationexception

class PaymentTelCertificationException(HttpPaymentRequiredException):
    ## 要求を受け付けできません。電話認証を先に実行してください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(PaymentTelCertificationException, self).__init__(status, code, "要求を受け付けできません。電話認証を先に実行してください。" if message is None or message == "" else message)
    
