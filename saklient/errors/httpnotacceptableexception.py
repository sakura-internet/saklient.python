# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpnotacceptableexception

class HttpNotAcceptableException(HttpException):
    ## 要求を受け付けできません。サポートサイトやメンテナンス情報をご確認ください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpNotAcceptableException, self).__init__(status, code, "要求を受け付けできません。サポートサイトやメンテナンス情報をご確認ください。" if message is None or message == "" else message)
    
