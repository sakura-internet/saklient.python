# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.gslbserver

class GslbServer(object):
    ## GSLBの監視対象サーバ設定。
    
    # (instance field) _enabled
    
    ## @return {bool}
    def get_enabled(self):
        return self._enabled
    
    ## @param {bool} v
    # @return {bool}
    def set_enabled(self, v):
        Util.validate_type(v, "bool")
        self._enabled = v
        return self._enabled
    
    ## 有効状態
    enabled = property(get_enabled, set_enabled, None)
    
    # (instance field) _ip_address
    
    ## @return {str}
    def get_ip_address(self):
        return self._ip_address
    
    ## @param {str} v
    # @return {str}
    def set_ip_address(self, v):
        Util.validate_type(v, "str")
        self._ip_address = v
        return self._ip_address
    
    ## IPアドレス
    ip_address = property(get_ip_address, set_ip_address, None)
    
    # (instance field) _weight
    
    ## @return {int}
    def get_weight(self):
        return self._weight
    
    ## @param {int} v
    # @return {int}
    def set_weight(self, v):
        Util.validate_type(v, "int")
        self._weight = v
        return self._weight
    
    ## 重み値
    weight = property(get_weight, set_weight, None)
    
    ## @ignore
    # @param {any} obj=None
    def __init__(self, obj=None):
        if obj is None:
            obj = {}
        enabled = Util.get_by_path_any([obj], ["Enabled", "enabled"])
        self._enabled = None
        if enabled is not None:
            enabledStr = enabled
            self._enabled = enabledStr.lower() == "true"
        self._ip_address = Util.get_by_path_any([obj], ["IPAddress", "ipAddress", "ip_address", "ip"])
        weight = Util.get_by_path_any([obj], ["Weight", "weight"])
        self._weight = None
        if weight is not None:
            self._weight = int(weight)
        if self._weight == 0:
            self._weight = None
    
    ## @return {any}
    def to_raw_settings(self):
        return {
            'Enabled': None if self._enabled is None else ("True" if self._enabled else "False"),
            'IPAddress': self._ip_address,
            'Weight': self._weight
        }
    
