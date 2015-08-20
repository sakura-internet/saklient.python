# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ..client import Client
from .resource import Resource
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.ipv6net

class Ipv6Net(Resource):
    ## IPv6ネットワークの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_prefix
    
    # (instance field) m_prefix_len
    
    # (instance field) m_prefix_tail
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/ipv6net"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "IPv6Net"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "IPv6Nets"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "Ipv6Net"
    
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
        super(Ipv6Net, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self.api_deserialize(obj, wrapped)
    
    # (instance field) n_id = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_id(self):
        return self.m_id
    
    ## ID
    id = property(get_id, None, None)
    
    # (instance field) n_prefix = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_prefix(self):
        return self.m_prefix
    
    ## ネットワークプレフィックス
    prefix = property(get_prefix, None, None)
    
    # (instance field) n_prefix_len = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {int}
    def get_prefix_len(self):
        return self.m_prefix_len
    
    ## ネットワークプレフィックス長
    prefix_len = property(get_prefix_len, None, None)
    
    # (instance field) n_prefix_tail = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_prefix_tail(self):
        return self.m_prefix_tail
    
    ## このネットワーク範囲における最後のIPv6アドレス
    prefix_tail = property(get_prefix_tail, None, None)
    
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
        if Util.exists_path(r, "IPv6Prefix"):
            self.m_prefix = None if Util.get_by_path(r, "IPv6Prefix") is None else str(Util.get_by_path(r, "IPv6Prefix"))
        else:
            self.m_prefix = None
            self.is_incomplete = True
        self.n_prefix = False
        if Util.exists_path(r, "IPv6PrefixLen"):
            self.m_prefix_len = None if Util.get_by_path(r, "IPv6PrefixLen") is None else int(str(Util.get_by_path(r, "IPv6PrefixLen")))
        else:
            self.m_prefix_len = None
            self.is_incomplete = True
        self.n_prefix_len = False
        if Util.exists_path(r, "IPv6PrefixTail"):
            self.m_prefix_tail = None if Util.get_by_path(r, "IPv6PrefixTail") is None else str(Util.get_by_path(r, "IPv6PrefixTail"))
        else:
            self.m_prefix_tail = None
            self.is_incomplete = True
        self.n_prefix_tail = False
    
    ## @ignore
    # @param {bool} withClean=False
    # @return {any}
    def api_serialize_impl(self, withClean=False):
        Util.validate_type(withClean, "bool")
        ret = {
            
        }
        if withClean or self.n_id:
            Util.set_by_path(ret, "ID", self.m_id)
        if withClean or self.n_prefix:
            Util.set_by_path(ret, "IPv6Prefix", self.m_prefix)
        if withClean or self.n_prefix_len:
            Util.set_by_path(ret, "IPv6PrefixLen", self.m_prefix_len)
        if withClean or self.n_prefix_tail:
            Util.set_by_path(ret, "IPv6PrefixTail", self.m_prefix_tail)
        return ret
    
