# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpfaileddependencyexception

class HttpFailedDependencyException(HttpException):
    ## HTTPエラー。Failed Dependency.
    
    # (class field) default_message = "HTTPエラー。Failed Dependency."
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpFailedDependencyException, self).__init__(status, code, message)
    
