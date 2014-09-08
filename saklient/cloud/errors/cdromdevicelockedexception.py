# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.cdromdevicelockedexception

class CdromDeviceLockedException(HttpConflictException):
    ## 要求された操作を行えません。CD-ROMドライブがロックされています。
    
    # (class field) default_message = "要求された操作を行えません。CD-ROMドライブがロックされています。"
    
    pass
