# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ..client import Client
from .resource import Resource
from .ipv4range import Ipv4Range
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.ipv4net

class Ipv4Net(Resource):
    ## IPv4ネットワークの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_address
    
    # (instance field) m_mask_len
    
    # (instance field) m_default_route
    
    # (instance field) m_next_hop
    
    # (instance field) _range
    
    ## @return {saklient.cloud.resources.ipv4range.Ipv4Range}
    def get_range(self):
        return self._range
    
    ## 利用可能なIPアドレス範囲
    range = property(get_range, None, None)
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/subnet"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "Subnet"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "Subnets"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "Ipv4Net"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {Swytch} this
    def reload(self):
        return self._reload()
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(Ipv4Net, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self.api_deserialize(obj, wrapped)
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_after_api_deserialize(self, r, root):
        self._range = None
        addresses = (r["IPAddresses"] if "IPAddresses" in r else None)
        if addresses is not None:
            self._range = Ipv4Range(addresses)
    
    # (instance field) n_id = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_id(self):
        return self.m_id
    
    ## ID
    id = property(get_id, None, None)
    
    # (instance field) n_address = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_address(self):
        return self.m_address
    
    ## ネットワークアドレス
    address = property(get_address, None, None)
    
    # (instance field) n_mask_len = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {int}
    def get_mask_len(self):
        return self.m_mask_len
    
    ## マスク長
    mask_len = property(get_mask_len, None, None)
    
    # (instance field) n_default_route = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_default_route(self):
        return self.m_default_route
    
    ## デフォルトルート
    default_route = property(get_default_route, None, None)
    
    # (instance field) n_next_hop = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_next_hop(self):
        return self.m_next_hop
    
    ## ネクストホップ
    next_hop = property(get_next_hop, None, None)
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {any} r
    def api_deserialize_impl(self, r):
        self.is_new = r is None
        if self.is_new:
            r = {
                
            }
        self.is_incomplete = False
        if Util.exists_path(r, "ID"):
            self.m_id = None if Util.get_by_path(r, "ID") is None else str(Util.get_by_path(r, "ID"))
        else:
            self.m_id = None
            self.is_incomplete = True
        self.n_id = False
        if Util.exists_path(r, "NetworkAddress"):
            self.m_address = None if Util.get_by_path(r, "NetworkAddress") is None else str(Util.get_by_path(r, "NetworkAddress"))
        else:
            self.m_address = None
            self.is_incomplete = True
        self.n_address = False
        if Util.exists_path(r, "NetworkMaskLen"):
            self.m_mask_len = None if Util.get_by_path(r, "NetworkMaskLen") is None else int(str(Util.get_by_path(r, "NetworkMaskLen")))
        else:
            self.m_mask_len = None
            self.is_incomplete = True
        self.n_mask_len = False
        if Util.exists_path(r, "DefaultRoute"):
            self.m_default_route = None if Util.get_by_path(r, "DefaultRoute") is None else str(Util.get_by_path(r, "DefaultRoute"))
        else:
            self.m_default_route = None
            self.is_incomplete = True
        self.n_default_route = False
        if Util.exists_path(r, "NextHop"):
            self.m_next_hop = None if Util.get_by_path(r, "NextHop") is None else str(Util.get_by_path(r, "NextHop"))
        else:
            self.m_next_hop = None
            self.is_incomplete = True
        self.n_next_hop = False
    
    ## @ignore
    # @param {bool} withClean=False
    # @return {any}
    def api_serialize_impl(self, withClean=False):
        Util.validate_type(withClean, "bool")
        ret = {
            
        }
        if withClean or self.n_id:
            Util.set_by_path(ret, "ID", self.m_id)
        if withClean or self.n_address:
            Util.set_by_path(ret, "NetworkAddress", self.m_address)
        if withClean or self.n_mask_len:
            Util.set_by_path(ret, "NetworkMaskLen", self.m_mask_len)
        if withClean or self.n_default_route:
            Util.set_by_path(ret, "DefaultRoute", self.m_default_route)
        if withClean or self.n_next_hop:
            Util.set_by_path(ret, "NextHop", self.m_next_hop)
        return ret
    
