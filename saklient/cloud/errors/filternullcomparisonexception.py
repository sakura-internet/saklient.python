# -*- coding:utf-8 -*-

from ...errors.httpbadrequestexception import HttpBadRequestException

# module saklient.cloud.errors.filternullcomparisonexception

class FilterNullComparisonException(HttpBadRequestException):
    ## 不適切な要求です。nullとは比較できない演算子がフィルタ中に含まれています。
    
    # (class field) default_message = "不適切な要求です。nullとは比較できない演算子がフィルタ中に含まれています。"
    
    pass
