# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.notwithhybridconnexception

class NotWithHybridconnException(HttpConflictException):
    ## 要求された操作を行えません。ハイブリッド接続と併用する場合はお問い合わせください。
    
    # (class field) default_message = "要求された操作を行えません。ハイブリッド接続と併用する場合はお問い合わせください。"
    
    pass
