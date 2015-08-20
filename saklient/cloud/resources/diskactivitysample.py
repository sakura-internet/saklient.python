# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.diskactivitysample

class DiskActivitySample(object):
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
    
    # (instance field) _write
    
    ## @return {float}
    def get_write(self):
        return self._write
    
    ## ライト[BPS]
    write = property(get_write, None, None)
    
    # (instance field) _read
    
    ## @return {float}
    def get_read(self):
        return self._read
    
    ## リード[BPS]
    read = property(get_read, None, None)
    
    ## @param {str} atStr
    # @param {any} data
    def __init__(self, atStr, data):
        Util.validate_type(atStr, "str")
        self._at = Util.str2date(atStr)
        self._is_available = True
        v = None
        v = (data["Write"] if "Write" in data else None)
        if v is None:
            self._is_available = False
        else:
            self._write = v
        v = (data["Read"] if "Read" in data else None)
        if v is None:
            self._is_available = False
        else:
            self._read = v
    
