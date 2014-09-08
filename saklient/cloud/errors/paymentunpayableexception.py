# -*- coding:utf-8 -*-

from ...errors.httppaymentrequiredexception import HttpPaymentRequiredException

# module saklient.cloud.errors.paymentunpayableexception

class PaymentUnpayableException(HttpPaymentRequiredException):
    ## お客様のご都合により操作を受け付けることができません。
    
    # (class field) default_message = "お客様のご都合により操作を受け付けることができません。"
    
    pass
