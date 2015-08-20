# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.routeractivitysample

class RouterActivitySample(object):
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
    
    # (instance field) _outgoing
    
    ## @return {float}
    def get_outgoing(self):
        return self._outgoing
    
    ## 送信[BPS]
    outgoing = property(get_outgoing, None, None)
    
    # (instance field) _incoming
    
    ## @return {float}
    def get_incoming(self):
        return self._incoming
    
    ## 受信[BPS]
    incoming = property(get_incoming, None, None)
    
    ## @param {str} atStr
    # @param {any} data
    def __init__(self, atStr, data):
        Util.validate_type(atStr, "str")
        self._at = Util.str2date(atStr)
        self._is_available = True
        v = None
        v = (data["Out"] if "Out" in data else None)
        if v is None:
            self._is_available = False
        else:
            self._outgoing = v
        v = (data["In"] if "In" in data else None)
        if v is None:
            self._is_available = False
        else:
            self._incoming = v
    
