# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httppreconditionfailedexception

class HttpPreconditionFailedException(HttpException):
    ## HTTPエラー。Precondition Failed.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpPreconditionFailedException, self).__init__(status, code, "HTTPエラー。Precondition Failed." if message is None or message == "" else message)
    
