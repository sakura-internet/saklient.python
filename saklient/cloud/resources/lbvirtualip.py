# -*- coding:utf-8 -*-

from ...util import Util
from .lbserver import LbServer

# module saklient.cloud.resources.lbvirtualip

class LbVirtualIp:
    ## ロードバランサの仮想IPアドレス。
    
    # (instance field) _virtual_ip_address
    
    ## @return {str}
    def get_virtual_ip_address(self):
        return self._virtual_ip_address
    
    ## @param {str} v
    # @return {str}
    def set_virtual_ip_address(self, v):
        Util.validate_type(v, "str")
        self._virtual_ip_address = v
        return self._virtual_ip_address
    
    ## VIPアドレス
    virtual_ip_address = property(get_virtual_ip_address, set_virtual_ip_address, None)
    
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
    
    # (instance field) _delay_loop
    
    ## @return {int}
    def get_delay_loop(self):
        return self._delay_loop
    
    ## @param {int} v
    # @return {int}
    def set_delay_loop(self, v):
        Util.validate_type(v, "int")
        self._delay_loop = v
        return self._delay_loop
    
    ## チェック間隔 [秒]
    delay_loop = property(get_delay_loop, set_delay_loop, None)
    
    # (instance field) _servers
    
    ## @return {saklient.cloud.resources.lbserver.LbServer[]}
    def get_servers(self):
        return self._servers
    
    ## 実サーバ
    servers = property(get_servers, None, None)
    
    ## @ignore
    # @param {any} obj=None
    def __init__(self, obj=None):
        if obj is None:
            obj = {}
        vip = Util.get_by_path_any([obj], ["VirtualIPAddress", "virtualIpAddress", "virtual_ip_address", "vip"])
        self._virtual_ip_address = vip
        port = Util.get_by_path_any([obj], ["Port", "port"])
        self._port = None
        if port is not None:
            self._port = int(port)
        if self._port == 0:
            self._port = None
        delayLoop = Util.get_by_path_any([obj], ["DelayLoop", "delayLoop", "delay_loop", "delay"])
        self._delay_loop = None
        if delayLoop is not None:
            self._delay_loop = int(delayLoop)
        if self._delay_loop == 0:
            self._delay_loop = None
        self._servers = []
        serversDyn = Util.get_by_path_any([obj], ["Servers", "servers"])
        if serversDyn is not None:
            servers = serversDyn
            for server in servers:
                self._servers.append(LbServer(server))
    
    ## @param {any} settings=None
    # @return {saklient.cloud.resources.lbserver.LbServer}
    def add_server(self, settings=None):
        ret = LbServer(settings)
        self._servers.append(ret)
        return ret
    
    ## @return {any}
    def to_raw_settings(self):
        servers = []
        for server in self._servers:
            servers.append(server.to_raw_settings())
        return {
            'VirtualIPAddress': self._virtual_ip_address,
            'Port': self._port,
            'DelayLoop': self._delay_loop,
            'Servers': servers
        }
    
    ## @param {str} address
    # @return {saklient.cloud.resources.lbserver.LbServer}
    def get_server_by_address(self, address):
        Util.validate_type(address, "str")
        for srv in self._servers:
            if srv.ip_address == address:
                return srv
        return None
    
    ## @param {any[]} srvs
    # @return {saklient.cloud.resources.lbvirtualip.LbVirtualIp}
    def update_status(self, srvs):
        Util.validate_type(srvs, "list")
        for srvDyn in srvs:
            ip = (srvDyn["IPAddress"] if "IPAddress" in srvDyn else None)
            srv = self.get_server_by_address(ip)
            if srv is None:
                next
            srv.update_status(srvDyn)
        return self
    
