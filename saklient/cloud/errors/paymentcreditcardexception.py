# -*- coding:utf-8 -*-

from ...errors.httppaymentrequiredexception import HttpPaymentRequiredException

# module saklient.cloud.errors.paymentcreditcardexception

class PaymentCreditCardException(HttpPaymentRequiredException):
    ## 要求を受け付けできません。クレジットカードの使用期限、利用限度額をご確認ください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(PaymentCreditCardException, self).__init__(status, code, "要求を受け付けできません。クレジットカードの使用期限、利用限度額をご確認ください。" if message is None or message == "" else message)
    
