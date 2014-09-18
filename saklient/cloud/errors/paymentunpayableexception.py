# -*- coding:utf-8 -*-

from ...errors.httppaymentrequiredexception import HttpPaymentRequiredException

# module saklient.cloud.errors.paymentunpayableexception

class PaymentUnpayableException(HttpPaymentRequiredException):
    ## お客様のご都合により操作を受け付けることができません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(PaymentUnpayableException, self).__init__(status, code, "お客様のご都合により操作を受け付けることができません。" if message is None or message == "" else message)
    
