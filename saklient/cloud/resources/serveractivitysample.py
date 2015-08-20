# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.serveractivitysample

class ServerActivitySample(object):
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
    
    # (instance field) _cpu_time
    
    ## @return {float}
    def get_cpu_time(self):
        return self._cpu_time
    
    ## CPU時間
    cpu_time = property(get_cpu_time, None, None)
    
    ## @param {str} atStr
    # @param {any} data
    def __init__(self, atStr, data):
        Util.validate_type(atStr, "str")
        self._at = Util.str2date(atStr)
        self._is_available = False
        v = (data["CPU-TIME"] if "CPU-TIME" in data else None)
        if v is not None:
            self._is_available = True
            self._cpu_time = v
    
