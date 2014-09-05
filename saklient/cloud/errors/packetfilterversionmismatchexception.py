# -*- coding:utf-8 -*-

from saklient.errors.httpconflictexception import HttpConflictException
from saklient.errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.packetfilterversionmismatchexception

class PacketFilterVersionMismatchException(HttpConflictException):
    ## 要求された操作を行えません。起動中のサーバが収容されているハイパーバイザとパケットフィルタのバージョンが合致しません。コントロールパネルまたはAPIからの操作によりサーバを一旦停止し、再度起動後にお試しください。
    
    # (class field) default_message = "要求された操作を行えません。起動中のサーバが収容されているハイパーバイザとパケットフィルタのバージョンが合致しません。コントロールパネルまたはAPIからの操作によりサーバを一旦停止し、再度起動後にお試しください。"
    
    pass
