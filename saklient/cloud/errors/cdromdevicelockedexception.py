# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.cdromdevicelockedexception

class CdromDeviceLockedException(HttpConflictException):
    ## 要求された操作を行えません。CD-ROMドライブがロックされています。
    
    # (class field) default_message = "要求された操作を行えません。CD-ROMドライブがロックされています。"
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(CdromDeviceLockedException, self).__init__(status, code, message)
    
