# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.samelicenserequiredexception

class SameLicenseRequiredException(HttpConflictException):
    ## 要求された操作を行えません。再インストール時に指定できるソースは、同一のライセンスを必要とするアーカイブに限られます。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(SameLicenseRequiredException, self).__init__(status, code, "要求された操作を行えません。再インストール時に指定できるソースは、同一のライセンスを必要とするアーカイブに限られます。" if message is None or message == "" else message)
    
