# -*- coding:utf-8 -*-

from ...errors.httpinternalservererrorexception import HttpInternalServerErrorException

# module saklient.cloud.errors.unknownexception

class UnknownException(HttpInternalServerErrorException):
    ## 予期しないエラーが発生しました。このエラーが繰り返し発生する場合は、サポートサイトやメンテナンス情報をご確認ください。
    
    # (class field) default_message = "予期しないエラーが発生しました。このエラーが繰り返し発生する場合は、サポートサイトやメンテナンス情報をご確認ください。"
    
    pass
