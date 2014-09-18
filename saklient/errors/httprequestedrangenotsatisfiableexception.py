# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httprequestedrangenotsatisfiableexception

class HttpRequestedRangeNotSatisfiableException(HttpException):
    ## HTTPエラー。Requested Range Not Satisfiable.
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpRequestedRangeNotSatisfiableException, self).__init__(status, code, "HTTPエラー。Requested Range Not Satisfiable." if message is None or message == "" else message)
    
