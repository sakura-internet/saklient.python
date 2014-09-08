# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.deleterouterb4switchexception

class DeleteRouterB4SwitchException(HttpConflictException):
    ## 要求された操作を行えません。ルータを削除することでスイッチは同時に削除されます。
    
    # (class field) default_message = "要求された操作を行えません。ルータを削除することでスイッチは同時に削除されます。"
    
    pass
