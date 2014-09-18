# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpupgraderequiredexception

class HttpUpgradeRequiredException(HttpException):
    ## HTTPエラー。Upgrade Required.
    
    # (class field) default_message = "HTTPエラー。Upgrade Required."
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpUpgradeRequiredException, self).__init__(status, code, message)
    
