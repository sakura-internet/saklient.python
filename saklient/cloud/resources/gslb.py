# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.saklientexception import SaklientException
from ..client import Client
from .commonserviceitem import CommonServiceItem
from .gslbserver import GslbServer
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.gslb

class Gslb(CommonServiceItem):
    ## GSLBの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) _servers
    
    ## @return {saklient.cloud.resources.gslbserver.GslbServer[]}
    def get_servers(self):
        return self._servers
    
    ## 仮想IPアドレス {@link GslbServer} の配列
    servers = property(get_servers, None, None)
    
    ## @return {str}
    def get_protocol(self):
        raw = Util.get_by_path(self.raw_settings, "GSLB.HealthCheck.Protocol")
        if raw is None:
            raise SaklientException("invalid_data", "Data of the resource is invalid")
        return raw
    
    ## @param {str} v
    # @return {str}
    def set_protocol(self, v):
        Util.validate_type(v, "str")
        self._normalize()
        Util.set_by_path(self.raw_settings, "GSLB.HealthCheck.Protocol", v)
        return v
    
    ## 監視方法
    protocol = property(get_protocol, set_protocol, None)
    
    ## @return {str}
    def get_path_to_check(self):
        if not Util.exists_path(self.raw_settings, "GSLB.HealthCheck.Path"):
            return None
        raw = Util.get_by_path(self.raw_settings, "GSLB.HealthCheck.Path")
        return raw
    
    ## @param {str} v
    # @return {str}
    def set_path_to_check(self, v):
        Util.validate_type(v, "str")
        self._normalize()
        Util.set_by_path(self.raw_settings, "GSLB.HealthCheck.Path", v)
        return v
    
    ## 監視対象パス
    path_to_check = property(get_path_to_check, set_path_to_check, None)
    
    ## @return {int}
    def get_response_expected(self):
        raw = Util.get_by_path(self.raw_settings, "GSLB.HealthCheck.Status")
        if raw is None:
            raise SaklientException("invalid_data", "Data of the resource is invalid")
        return int(raw)
    
    ## @param {int} v
    # @return {int}
    def set_response_expected(self, v):
        Util.validate_type(v, "int")
        self._normalize()
        Util.set_by_path(self.raw_settings, "GSLB.HealthCheck.Status", v)
        return v
    
    ## 監視時に期待されるレスポンスコード
    response_expected = property(get_response_expected, set_response_expected, None)
    
    ## @return {int}
    def get_delay_loop(self):
        delayLoop = Util.get_by_path(self.raw_settings, "GSLB.DelayLoop")
        if delayLoop is None:
            raise SaklientException("invalid_data", "Data of the resource is invalid")
        return int(delayLoop)
    
    ## @param {int} v
    # @return {int}
    def set_delay_loop(self, v):
        Util.validate_type(v, "int")
        self._normalize()
        Util.set_by_path(self.raw_settings, "GSLB.DelayLoop", v)
        return v
    
    ## チェック間隔(秒)
    delay_loop = property(get_delay_loop, set_delay_loop, None)
    
    ## @return {bool}
    def get_weighted(self):
        weighted = Util.get_by_path(self.raw_settings, "GSLB.Weighted")
        if weighted is None:
            raise SaklientException("invalid_data", "Data of the resource is invalid")
        return weighted.lower() == "true"
    
    ## @param {bool} v
    # @return {bool}
    def set_weighted(self, v):
        Util.validate_type(v, "bool")
        self._normalize()
        Util.set_by_path(self.raw_settings, "GSLB.Weighted", "True" if v else "False")
        return v
    
    ## 重み付け応答
    weighted = property(get_weighted, set_weighted, None)
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self._servers = None
        super(Gslb, self).__init__(client, obj, wrapped)
        self._normalize()
    
    ## @private
    # @ignore 
    # @return {void}
    def _normalize(self):
        if self._servers is None:
            self._servers = []
        if self.raw_settings is None:
            self.raw_settings = {}
        if not Util.exists_path(self.raw_settings, "GSLB"):
            Util.set_by_path(self.raw_settings, "GSLB", {})
        if not Util.exists_path(self.raw_settings, "GSLB.HealthCheck"):
            Util.set_by_path(self.raw_settings, "GSLB.HealthCheck", {})
        if not Util.exists_path(self.raw_settings, "GSLB.Servers"):
            Util.set_by_path(self.raw_settings, "GSLB.Servers", [])
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_after_api_deserialize(self, r, root):
        self._normalize()
        self._servers = []
        settings = self.raw_settings
        if settings is not None:
            raw = Util.get_by_path(settings, "GSLB.Servers")
            if raw is None:
                raw = []
            servers = raw
            for server in servers:
                self._servers.append(GslbServer(server))
    
    ## @private
    # @param {bool} withClean
    # @return {void}
    def _on_before_api_serialize(self, withClean):
        Util.validate_type(withClean, "bool")
        self._normalize()
        servers = []
        for server in self._servers:
            servers.append(server.to_raw_settings())
        Util.set_by_path(self.raw_settings, "GSLB.Servers", servers)
    
    ## @private
    # @param {any} r
    # @param {bool} withClean
    # @return {void}
    def _on_after_api_serialize(self, r, withClean):
        Util.validate_type(withClean, "bool")
        if r is None:
            return
        Util.set_by_path(r, "Provider", {})
        Util.set_by_path(r, "Provider.Class", "gslb")
    
    ## @ignore
    # @param {str} protocol
    # @param {int} delayLoop=10
    # @param {bool} weighted=True
    # @return {saklient.cloud.resources.gslb.Gslb}
    def set_initial_params(self, protocol, delayLoop=10, weighted=True):
        Util.validate_type(protocol, "str")
        Util.validate_type(delayLoop, "int")
        Util.validate_type(weighted, "bool")
        settings = self.raw_settings
        self.protocol = protocol
        self.delay_loop = delayLoop
        self.weighted = weighted
        return self
    
    ## 監視対象サーバ設定を追加します。
    # 
    # @param {any} settings=None 設定オブジェクト
    # @return {saklient.cloud.resources.gslbserver.GslbServer}
    def add_server(self, settings=None):
        ret = GslbServer(settings)
        self._servers.append(ret)
        return ret
    
