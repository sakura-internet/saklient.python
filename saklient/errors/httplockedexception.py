# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httplockedexception

class HttpLockedException(HttpException):
    ## HTTPエラー。Locked.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpLockedException, self).__init__(status, code, "HTTPエラー。Locked." if message is None or message == "" else message)
    
