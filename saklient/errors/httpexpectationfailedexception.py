# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpexpectationfailedexception

class HttpExpectationFailedException(HttpException):
    ## HTTPエラー。Expectation Failed.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpExpectationFailedException, self).__init__(status, code, "HTTPエラー。Expectation Failed." if message is None or message == "" else message)
    
