# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.packetfilterversionmismatchexception

class PacketFilterVersionMismatchException(HttpConflictException):
    ## 要求された操作を行えません。起動中のサーバが収容されているハイパーバイザとパケットフィルタのバージョンが合致しません。コントロールパネルまたはAPIからの操作によりサーバを一旦停止し、再度起動後にお試しください。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(PacketFilterVersionMismatchException, self).__init__(status, code, "要求された操作を行えません。起動中のサーバが収容されているハイパーバイザとパケットフィルタのバージョンが合致しません。コントロールパネルまたはAPIからの操作によりサーバを一旦停止し、再度起動後にお試しください。" if message is None or message == "" else message)
    
