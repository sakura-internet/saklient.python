# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.lbserver

class LbServer(object):
    ## ロードバランサの監視対象サーバ設定。
    
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
    
    # (instance field) _port
    
    ## @return {int}
    def get_port(self):
        return self._port
    
    ## @param {int} v
    # @return {int}
    def set_port(self, v):
        Util.validate_type(v, "int")
        self._port = v
        return self._port
    
    ## ポート番号
    port = property(get_port, set_port, None)
    
    # (instance field) _protocol
    
    ## @return {str}
    def get_protocol(self):
        return self._protocol
    
    ## @param {str} v
    # @return {str}
    def set_protocol(self, v):
        Util.validate_type(v, "str")
        self._protocol = v
        return self._protocol
    
    ## 監視方法
    protocol = property(get_protocol, set_protocol, None)
    
    # (instance field) _path_to_check
    
    ## @return {str}
    def get_path_to_check(self):
        return self._path_to_check
    
    ## @param {str} v
    # @return {str}
    def set_path_to_check(self, v):
        Util.validate_type(v, "str")
        self._path_to_check = v
        return self._path_to_check
    
    ## 監視対象パス
    path_to_check = property(get_path_to_check, set_path_to_check, None)
    
    # (instance field) _response_expected
    
    ## @return {int}
    def get_response_expected(self):
        return self._response_expected
    
    ## @param {int} v
    # @return {int}
    def set_response_expected(self, v):
        Util.validate_type(v, "int")
        self._response_expected = v
        return self._response_expected
    
    ## 監視時に期待されるレスポンスコード
    response_expected = property(get_response_expected, set_response_expected, None)
    
    # (instance field) _active_connections
    
    ## @return {int}
    def get_active_connections(self):
        return self._active_connections
    
    ## 現在の接続数
    active_connections = property(get_active_connections, None, None)
    
    # (instance field) _status
    
    ## @return {str}
    def get_status(self):
        return self._status
    
    ## 現在の状態
    status = property(get_status, None, None)
    
    ## @ignore
    # @param {any} obj=None
    def __init__(self, obj=None):
        if obj is None:
            obj = {}
        health = Util.get_by_path_any([obj], ["HealthCheck", "healthCheck", "health_check", "health"])
        enabled = Util.get_by_path_any([obj], ["Enabled", "enabled"])
        self._enabled = None
        if enabled is not None:
            enabledStr = enabled
            self._enabled = enabledStr.lower() == "true"
        self._ip_address = Util.get_by_path_any([obj], ["IPAddress", "ipAddress", "ip_address", "ip"])
        self._protocol = Util.get_by_path_any([health, obj], ["Protocol", "protocol"])
        self._path_to_check = Util.get_by_path_any([health, obj], ["Path", "path", "pathToCheck", "path_to_check"])
        port = Util.get_by_path_any([obj], ["Port", "port"])
        self._port = None
        if port is not None:
            self._port = int(port)
        if self._port == 0:
            self._port = None
        responseExpected = Util.get_by_path_any([health, obj], ["Status", "status", "responseExpected", "response_expected"])
        self._response_expected = None
        if responseExpected is not None:
            self._response_expected = int(responseExpected)
        if self._response_expected == 0:
            self._response_expected = None
        self._active_connections = 0
        self._status = None
    
    ## @return {any}
    def to_raw_settings(self):
        return {
            'Enabled': None if self._enabled is None else ("True" if self._enabled else "False"),
            'IPAddress': self._ip_address,
            'Port': self._port,
            'HealthCheck': {
                'Protocol': self._protocol,
                'Path': self._path_to_check,
                'Status': self._response_expected
            }
        }
    
    ## @ignore
    # @param {any} obj
    # @return {saklient.cloud.resources.lbserver.LbServer}
    def update_status(self, obj):
        connStr = (obj["ActiveConn"] if "ActiveConn" in obj else None)
        self._active_connections = 0
        if connStr is not None:
            self._active_connections = int(connStr)
        status = (obj["Status"] if "Status" in obj else None)
        self._status = None if status is None else status.lower()
        return self
    
