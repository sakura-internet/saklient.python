# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.ipv4range

class Ipv4Range(object):
    ## IPv4ネットワークのIPアドレス範囲。
    
    # (instance field) _first
    
    ## @return {str}
    def get_first(self):
        return self._first
    
    ## 開始アドレス
    first = property(get_first, None, None)
    
    # (instance field) _last
    
    ## @return {str}
    def get_last(self):
        return self._last
    
    ## 終了アドレス
    last = property(get_last, None, None)
    
    # (instance field) _as_array
    
    ## @return {str[]}
    def get_as_array(self):
        ret = []
        i = Util.ip2long(self._first)
        i1 = Util.ip2long(self._last)
        while (i <= i1):
            ret.append(Util.long2ip(i))
            i +=1
        return ret
    
    ## この範囲に属するIPv4アドレスの一覧を取得します。
    as_array = property(get_as_array, None, None)
    
    ## @ignore
    # @param {any} obj=None
    def __init__(self, obj=None):
        if obj is None:
            obj = {}
        first = Util.get_by_path_any([obj], ["Min", "min"])
        self._first = None
        if first is not None:
            self._first = first
        if self._first is not None and self._first == "":
            self._first = None
        last = Util.get_by_path_any([obj], ["Max", "max"])
        self._last = None
        if last is not None:
            self._last = last
        if self._last is not None and self._last == "":
            self._last = None
    
