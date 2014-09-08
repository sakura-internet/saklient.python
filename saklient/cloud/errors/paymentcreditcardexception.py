# -*- coding:utf-8 -*-

from ...errors.httppaymentrequiredexception import HttpPaymentRequiredException

# module saklient.cloud.errors.paymentcreditcardexception

class PaymentCreditCardException(HttpPaymentRequiredException):
    ## 要求を受け付けできません。クレジットカードの使用期限、利用限度額をご確認ください。
    
    # (class field) default_message = "要求を受け付けできません。クレジットカードの使用期限、利用限度額をご確認ください。"
    
    pass
