# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.deletestaticroutefirstexception

class DeleteStaticRouteFirstException(HttpConflictException):
    ## 要求された操作を行えません。ルータを削除する前に、スタティックルートを削除してください。
    
    # (class field) default_message = "要求された操作を行えません。ルータを削除する前に、スタティックルートを削除してください。"
    
    pass
