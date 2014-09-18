# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.runoutofipaddressexception

class RunOutOfIpAddressException(HttpConflictException):
    ## 要求された操作を行えません。指定されたネットワークに属するIPアドレスはすべて使用中です。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(RunOutOfIpAddressException, self).__init__(status, code, "要求された操作を行えません。指定されたネットワークに属するIPアドレスはすべて使用中です。" if message is None or message == "" else message)
    
