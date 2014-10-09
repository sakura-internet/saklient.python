# -*- coding:utf-8 -*-

from ...util import Util

# module saklient.cloud.resources.lbserver

class LbServer:
    ## ロードバランサの監視対象サーバ。
    
    # (instance field) _ip_address
    
    ## @return {str}
    def get_ip_address(self):
        return self._ip_address
    
    ## IPアドレス
    ip_address = property(get_ip_address, None, None)
    
    # (instance field) _port
    
    ## @return {int}
    def get_port(self):
        return self._port
    
    ## ポート番号
    port = property(get_port, None, None)
    
    # (instance field) _protocol
    
    ## @return {str}
    def get_protocol(self):
        return self._protocol
    
    ## 監視方法
    protocol = property(get_protocol, None, None)
    
    # (instance field) _path_to_check
    
    ## @return {str}
    def get_path_to_check(self):
        return self._path_to_check
    
    ## パス
    path_to_check = property(get_path_to_check, None, None)
    
    # (instance field) _expected_status
    
    ## @return {int}
    def get_expected_status(self):
        return self._expected_status
    
    ## レスポンスコード
    expected_status = property(get_expected_status, None, None)
    
    ## @ignore
    # @param {any} obj
    def __init__(self, obj):
        health = Util.get_by_path_any([obj], ["HealthCheck", "healthCheck", "health_check", "health"])
        self._ip_address = Util.get_by_path_any([obj], ["IPAddress", "ipAddress", "ip_address", "ip"])
        self._protocol = Util.get_by_path_any([health, obj], ["Protocol", "protocol"])
        self._path_to_check = Util.get_by_path_any([health, obj], ["Path", "path"])
        port = Util.get_by_path_any([obj], ["Port", "port"])
        self._port = None if port is None else int(port)
        if self._port == 0:
            self._port = None
        status = Util.get_by_path_any([health, obj], ["Status", "status"])
        self._expected_status = None if status is None else int(status)
        if self._expected_status == 0:
            self._expected_status = None
    
    ## @return {any}
    def to_raw_settings(self):
        return {
            'IPAddress': self._ip_address,
            'Port': self._port,
            'HealthCheck': {
                'Protocol': self._protocol,
                'Path': self._path_to_check,
                'Status': self._expected_status
            }
        }
    
