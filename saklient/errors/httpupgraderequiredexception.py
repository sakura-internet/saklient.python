# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpupgraderequiredexception

class HttpUpgradeRequiredException(HttpException):
    ## HTTPエラー。Upgrade Required.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpUpgradeRequiredException, self).__init__(status, code, "HTTPエラー。Upgrade Required." if message is None or message == "" else message)
    
