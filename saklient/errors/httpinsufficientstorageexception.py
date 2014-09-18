# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpinsufficientstorageexception

class HttpInsufficientStorageException(HttpException):
    ## HTTPエラー。Insufficient Storage.
    
    # (class field) default_message = "HTTPエラー。Insufficient Storage."
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpInsufficientStorageException, self).__init__(status, code, message)
    
