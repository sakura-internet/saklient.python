# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpvariantalsonegotiatesexception

class HttpVariantAlsoNegotiatesException(HttpException):
    ## HTTPエラー。Variant Also Negotiates.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpVariantAlsoNegotiatesException, self).__init__(status, code, "HTTPエラー。Variant Also Negotiates." if message is None or message == "" else message)
    
