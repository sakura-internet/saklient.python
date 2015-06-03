# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

from .httpexception import HttpException
import saklient

# module saklient.errors.httpgoneexception

class HttpGoneException(HttpException):
    ## HTTPエラー。Gone.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpGoneException, self).__init__(status, code, "HTTPエラー。Gone." if message is None or message == "" else message)
    
