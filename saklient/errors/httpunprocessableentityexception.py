# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpunprocessableentityexception

class HttpUnprocessableEntityException(HttpException):
    ## HTTPエラー。Unprocessable Entity.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpUnprocessableEntityException, self).__init__(status, code, "HTTPエラー。Unprocessable Entity." if message is None or message == "" else message)
    
