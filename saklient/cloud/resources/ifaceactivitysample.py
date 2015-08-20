# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.ifaceactivitysample

class IfaceActivitySample(object):
    ## @ignore
    
    # (instance field) _at
    
    ## @return {NativeDate}
    def get_at(self):
        return self._at
    
    ## 記録日時
    at = property(get_at, None, None)
    
    # (instance field) _is_available
    
    ## @return {bool}
    def get_is_available(self):
        return self._is_available
    
    ## 有効な値のとき真
    is_available = property(get_is_available, None, None)
    
    # (instance field) _send
    
    ## @return {float}
    def get_send(self):
        return self._send
    
    ## 送信[byte/sec]
    send = property(get_send, None, None)
    
    # (instance field) _receive
    
    ## @return {float}
    def get_receive(self):
        return self._receive
    
    ## 受信[byte/sec]
    receive = property(get_receive, None, None)
    
    ## @param {str} atStr
    # @param {any} data
    def __init__(self, atStr, data):
        Util.validate_type(atStr, "str")
        self._at = Util.str2date(atStr)
        self._is_available = True
        v = None
        v = (data["Send"] if "Send" in data else None)
        if v is None:
            self._is_available = False
        else:
            self._send = v
        v = (data["Receive"] if "Receive" in data else None)
        if v is None:
            self._is_available = False
        else:
            self._receive = v
    
