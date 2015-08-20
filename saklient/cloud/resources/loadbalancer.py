# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.saklientexception import SaklientException
from ..client import Client
from .appliance import Appliance
from .lbvirtualip import LbVirtualIp
from .swytch import Swytch
from .ipv4net import Ipv4Net
from ..enums.eapplianceclass import EApplianceClass
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.loadbalancer

class LoadBalancer(Appliance):
    ## ロードバランサの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) _virtual_ips
    
    ## @return {saklient.cloud.resources.lbvirtualip.LbVirtualIp[]}
    def get_virtual_ips(self):
        return self._virtual_ips
    
    ## 仮想IPアドレス {@link LbVirtualIp} の配列
    virtual_ips = property(get_virtual_ips, None, None)
    
    ## @return {str}
    def get_default_route(self):
        return Util.get_by_path(self.raw_annotation, "Network.DefaultRoute")
    
    ## @param {str} v
    # @return {str}
    def set_default_route(self, v):
        Util.validate_type(v, "str")
        Util.set_by_path(self.raw_annotation, "Network.DefaultRoute", v)
        return v
    
    ## デフォルトルート
    default_route = property(get_default_route, set_default_route, None)
    
    ## @return {int}
    def get_mask_len(self):
        maskLen = Util.get_by_path(self.raw_annotation, "Network.NetworkMaskLen")
        if maskLen is None:
            raise SaklientException("invalid_data", "Data of the resource is invalid")
        return int(maskLen)
    
    ## @param {int} v
    # @return {int}
    def set_mask_len(self, v):
        Util.validate_type(v, "int")
        Util.set_by_path(self.raw_annotation, "Network.NetworkMaskLen", v)
        return v
    
    ## マスク長
    mask_len = property(get_mask_len, set_mask_len, None)
    
    ## @return {int}
    def get_vrid(self):
        vrid = Util.get_by_path(self.raw_annotation, "VRRP.VRID")
        if vrid is None:
            raise SaklientException("invalid_data", "Data of the resource is invalid")
        return int(vrid)
    
    ## @param {int} v
    # @return {int}
    def set_vrid(self, v):
        Util.validate_type(v, "int")
        Util.set_by_path(self.raw_annotation, "VRRP.VRID", v)
        return v
    
    ## VRID
    vrid = property(get_vrid, set_vrid, None)
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(LoadBalancer, self).__init__(client, obj, wrapped)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        if self.raw_annotation is None:
            self.raw_annotation = {}
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_after_api_deserialize(self, r, root):
        if self.raw_annotation is None:
            self.raw_annotation = {}
        self._virtual_ips = []
        settings = self.raw_settings
        if settings is not None:
            lb = (settings["LoadBalancer"] if "LoadBalancer" in settings else None)
            if lb is None:
                lb = []
            vips = lb
            for vip in vips:
                self._virtual_ips.append(LbVirtualIp(vip))
    
    ## @private
    # @param {bool} withClean
    # @return {void}
    def _on_before_api_serialize(self, withClean):
        Util.validate_type(withClean, "bool")
        lb = []
        for vip in self._virtual_ips:
            lb.append(vip.to_raw_settings())
        if self.raw_settings is None:
            self.raw_settings = {}
        self.raw_settings["LoadBalancer"] = lb
        if self.is_new:
            self.clazz = EApplianceClass.loadbalancer
    
    ## @ignore
    # @param {saklient.cloud.resources.swytch.Swytch} swytch
    # @param {int} vrid
    # @param {str[]} realIps
    # @param {bool} isHighSpec=False
    # @return {saklient.cloud.resources.loadbalancer.LoadBalancer}
    def set_initial_params(self, swytch, vrid, realIps, isHighSpec=False):
        Util.validate_type(swytch, "saklient.cloud.resources.swytch.Swytch")
        Util.validate_type(vrid, "int")
        Util.validate_type(realIps, "list")
        Util.validate_type(isHighSpec, "bool")
        annot = self.raw_annotation
        self.vrid = vrid
        Util.set_by_path(annot, "Switch.ID", swytch._id())
        if swytch.ipv4_nets is not None and 0 < len(swytch.ipv4_nets):
            net = swytch.ipv4_nets[0]
            self.default_route = net.default_route
            self.mask_len = net.mask_len
        else:
            self.default_route = swytch.user_default_route
            self.mask_len = swytch.user_mask_len
        servers = []
        for ip in realIps:
            servers.append({
                'IPAddress': ip
            })
        Util.set_by_path(annot, "Servers", servers)
        self.plan_id = 2 if isHighSpec else 1
        return self
    
    ## @return {saklient.cloud.resources.loadbalancer.LoadBalancer}
    def clear_virtual_ips(self):
        while (0 < len(self._virtual_ips)):
            self._virtual_ips.pop()
        return self
    
    ## 仮想IPアドレス設定を追加します。
    # 
    # @param {any} settings=None 設定オブジェクト
    # @return {saklient.cloud.resources.lbvirtualip.LbVirtualIp}
    def add_virtual_ip(self, settings=None):
        ret = LbVirtualIp(settings)
        self._virtual_ips.append(ret)
        return ret
    
    ## 指定したIPアドレスにマッチする仮想IPアドレス設定を取得します。
    # 
    # @param {str} address
    # @return {saklient.cloud.resources.lbvirtualip.LbVirtualIp}
    def get_virtual_ip_by_address(self, address):
        Util.validate_type(address, "str")
        for vip in self._virtual_ips:
            if vip.virtual_ip_address == address:
                return vip
        return None
    
    ## 監視対象サーバのステータスを最新の状態に更新します。
    # 
    # @return {saklient.cloud.resources.loadbalancer.LoadBalancer}
    def reload_status(self):
        result = self.request_retry("GET", self._api_path() + "/" + Util.url_encode(self._id()) + "/status")
        if result is not None and ( "LoadBalancer" in result if isinstance(result, dict) else hasattr(result, "LoadBalancer")):
            vips = (result["LoadBalancer"] if "LoadBalancer" in result else None)
            for vipDyn in vips:
                vipStr = (vipDyn["VirtualIPAddress"] if "VirtualIPAddress" in vipDyn else None)
                vip = self.get_virtual_ip_by_address(vipStr)
                if vip is None:
                    next
                vip.update_status((vipDyn["Servers"] if "Servers" in vipDyn else None))
        return self
    
