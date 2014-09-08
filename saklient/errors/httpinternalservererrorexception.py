# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpinternalservererrorexception

class HttpInternalServerErrorException(HttpException):
    ## サーバ内部エラーが発生しました。このエラーが繰り返し発生する場合は、メンテナンス情報、サポートサイトをご確認ください。
    
    # (class field) default_message = "サーバ内部エラーが発生しました。このエラーが繰り返し発生する場合は、メンテナンス情報、サポートサイトをご確認ください。"
    
    pass
