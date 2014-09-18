# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpgoneexception

class HttpGoneException(HttpException):
    ## HTTPエラー。Gone.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpGoneException, self).__init__(status, code, "HTTPエラー。Gone." if message is None or message == "" else message)
    
