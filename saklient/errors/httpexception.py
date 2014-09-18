# -*- coding:utf-8 -*-


# module saklient.errors.httpexception

class HttpException(Exception):
    
    # (instance field) status
    
    # (instance field) code
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpException, self).__init__(message)
        self.status = status
        self.code = code
    
