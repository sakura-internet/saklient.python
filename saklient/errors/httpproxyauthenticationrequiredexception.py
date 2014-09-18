# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpproxyauthenticationrequiredexception

class HttpProxyAuthenticationRequiredException(HttpException):
    ## HTTPエラー。Proxy Authentication Required.
    
    # (class field) default_message = "HTTPエラー。Proxy Authentication Required."
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(HttpProxyAuthenticationRequiredException, self).__init__(status, code, message)
    
