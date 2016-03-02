# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.saklientexception import SaklientException
from ..client import Client
from .resource import Resource
from .swytch import Swytch
from .ifaceactivity import IfaceActivity
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.iface

class Iface(Resource):
    ## インタフェースの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_mac_address
    
    # (instance field) m_ip_address
    
    # (instance field) m_user_ip_address
    
    # (instance field) m_server_id
    
    # (instance field) m_swytch_id
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/interface"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "Interface"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "Interfaces"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "Iface"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @return {saklient.cloud.resources.iface.Iface} this
    def save(self):
        return self._save()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {saklient.cloud.resources.iface.Iface} this
    def reload(self):
        return self._reload()
    
    # (instance field) _activity
    
    ## @return {saklient.cloud.resources.ifaceactivity.IfaceActivity}
    def get_activity(self):
        return self._activity
    
    ## アクティビティ
    activity = property(get_activity, None, None)
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(Iface, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self._activity = IfaceActivity(client)
        self.api_deserialize(obj, wrapped)
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_after_api_deserialize(self, r, root):
        if r is not None:
            self._activity.set_source_id(self._id())
    
    ## スイッチに接続します。
    # 
    # @param {saklient.cloud.resources.swytch.Swytch} swytch 接続先のスイッチ。
    # @return {saklient.cloud.resources.iface.Iface} this
    def connect_to_swytch(self, swytch):
        Util.validate_type(swytch, "saklient.cloud.resources.swytch.Swytch")
        self._client.request("PUT", self._api_path() + "/" + Util.url_encode(self._id()) + "/to/switch/" + Util.url_encode(swytch._id()))
        return self.reload()
    
    ## 指定したIDのスイッチに接続します。
    # 
    # @param {str} swytchId 接続先のスイッチID。
    # @return {saklient.cloud.resources.iface.Iface} this
    def connect_to_swytch_by_id(self, swytchId):
        Util.validate_type(swytchId, "str")
        self._client.request("PUT", self._api_path() + "/" + Util.url_encode(self._id()) + "/to/switch/" + swytchId)
        return self.reload()
    
    ## 共有セグメントに接続します。
    # 
    # @return {saklient.cloud.resources.iface.Iface} this
    def connect_to_shared_segment(self):
        self._client.request("PUT", self._api_path() + "/" + Util.url_encode(self._id()) + "/to/switch/shared")
        return self.reload()
    
    ## スイッチから切断します。
    # 
    # @return {saklient.cloud.resources.iface.Iface} this
    def disconnect_from_swytch(self):
        self._client.request("DELETE", self._api_path() + "/" + Util.url_encode(self._id()) + "/to/switch")
        return self.reload()
    
    # (instance field) n_id = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_id(self):
        return self.m_id
    
    ## ID
    id = property(get_id, None, None)
    
    # (instance field) n_mac_address = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_mac_address(self):
        return self.m_mac_address
    
    ## MACアドレス
    mac_address = property(get_mac_address, None, None)
    
    # (instance field) n_ip_address = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_ip_address(self):
        return self.m_ip_address
    
    ## IPv4アドレス（共有セグメントによる自動割当）
    ip_address = property(get_ip_address, None, None)
    
    # (instance field) n_user_ip_address = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_user_ip_address(self):
        return self.m_user_ip_address
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {str} v
    # @return {str}
    def set_user_ip_address(self, v):
        Util.validate_type(v, "str")
        self.m_user_ip_address = v
        self.n_user_ip_address = True
        return self.m_user_ip_address
    
    ## ユーザ設定IPv4アドレス
    user_ip_address = property(get_user_ip_address, set_user_ip_address, None)
    
    # (instance field) n_server_id = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_server_id(self):
        return self.m_server_id
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {str} v
    # @return {str}
    def set_server_id(self, v):
        Util.validate_type(v, "str")
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.iface.Iface#server_id")
        self.m_server_id = v
        self.n_server_id = True
        return self.m_server_id
    
    ## このインタフェースが取り付けられているサーバのID
    server_id = property(get_server_id, set_server_id, None)
    
    # (instance field) n_swytch_id = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_swytch_id(self):
        return self.m_swytch_id
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {str} v
    # @return {str}
    def set_swytch_id(self, v):
        Util.validate_type(v, "str")
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.iface.Iface#swytch_id")
        self.m_swytch_id = v
        self.n_swytch_id = True
        return self.m_swytch_id
    
    ## このインタフェースの接続先スイッチのID
    swytch_id = property(get_swytch_id, set_swytch_id, None)
    
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
        if Util.exists_path(r, "MACAddress"):
            self.m_mac_address = None if Util.get_by_path(r, "MACAddress") is None else str(Util.get_by_path(r, "MACAddress"))
        else:
            self.m_mac_address = None
            self.is_incomplete = True
        self.n_mac_address = False
        if Util.exists_path(r, "IPAddress"):
            self.m_ip_address = None if Util.get_by_path(r, "IPAddress") is None else str(Util.get_by_path(r, "IPAddress"))
        else:
            self.m_ip_address = None
            self.is_incomplete = True
        self.n_ip_address = False
        if Util.exists_path(r, "UserIPAddress"):
            self.m_user_ip_address = None if Util.get_by_path(r, "UserIPAddress") is None else str(Util.get_by_path(r, "UserIPAddress"))
        else:
            self.m_user_ip_address = None
            self.is_incomplete = True
        self.n_user_ip_address = False
        if Util.exists_path(r, "Server.ID"):
            self.m_server_id = None if Util.get_by_path(r, "Server.ID") is None else str(Util.get_by_path(r, "Server.ID"))
        else:
            self.m_server_id = None
            self.is_incomplete = True
        self.n_server_id = False
        if Util.exists_path(r, "Switch.ID"):
            self.m_swytch_id = None if Util.get_by_path(r, "Switch.ID") is None else str(Util.get_by_path(r, "Switch.ID"))
        else:
            self.m_swytch_id = None
            self.is_incomplete = True
        self.n_swytch_id = False
    
    ## @ignore
    # @param {bool} withClean=False
    # @return {any}
    def api_serialize_impl(self, withClean=False):
        Util.validate_type(withClean, "bool")
        missing = []
        ret = {
            
        }
        if withClean or self.n_id:
            Util.set_by_path(ret, "ID", self.m_id)
        if withClean or self.n_mac_address:
            Util.set_by_path(ret, "MACAddress", self.m_mac_address)
        if withClean or self.n_ip_address:
            Util.set_by_path(ret, "IPAddress", self.m_ip_address)
        if withClean or self.n_user_ip_address:
            Util.set_by_path(ret, "UserIPAddress", self.m_user_ip_address)
        if withClean or self.n_server_id:
            Util.set_by_path(ret, "Server.ID", self.m_server_id)
        else:
            if self.is_new:
                missing.append("server_id")
        if withClean or self.n_swytch_id:
            Util.set_by_path(ret, "Switch.ID", self.m_swytch_id)
        if len(missing) > 0:
            raise SaklientException("required_field", "Required fields must be set before the Iface creation: " + ", ".join(missing))
        return ret
    
