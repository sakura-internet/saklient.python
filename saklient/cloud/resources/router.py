# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpexception import HttpException
from ...errors.saklientexception import SaklientException
from ..client import Client
from .resource import Resource
from .icon import Icon
from .ipv4net import Ipv4Net
from .ipv6net import Ipv6Net
from .routeractivity import RouterActivity
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.router

class Router(Resource):
    ## ルータの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_name
    
    # (instance field) m_description
    
    # (instance field) m_network_mask_len
    
    # (instance field) m_band_width_mbps
    
    # (instance field) m_swytch_id
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/internet"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "Internet"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "Internet"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "Router"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @return {saklient.cloud.resources.router.Router} this
    def save(self):
        return self._save()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {saklient.cloud.resources.router.Router} this
    def reload(self):
        return self._reload()
    
    # (instance field) _activity
    
    ## @return {saklient.cloud.resources.routeractivity.RouterActivity}
    def get_activity(self):
        return self._activity
    
    ## アクティビティ
    activity = property(get_activity, None, None)
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(Router, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self._activity = RouterActivity(client)
        self.api_deserialize(obj, wrapped)
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_after_api_deserialize(self, r, root):
        if r is not None:
            self._activity.set_source_id(self._id())
    
    ## 作成中のルータが利用可能になるまで待機します。
    # 
    # @ignore
    # @param {int} timeoutSec
    # @param {(saklient.cloud.resources.router.Router, bool) => void} callback
    # @return {void}
    def after_create(self, timeoutSec, callback):
        Util.validate_type(timeoutSec, "int")
        Util.validate_type(callback, "function")
        ret = self.sleep_while_creating(timeoutSec)
        callback(self, ret)
    
    ## 作成中のルータが利用可能になるまで待機します。
    # 
    # @param {int} timeoutSec=120
    # @return {bool} 成功時はtrue、タイムアウトやエラーによる失敗時はfalseを返します。
    def sleep_while_creating(self, timeoutSec=120):
        Util.validate_type(timeoutSec, "int")
        step = 3
        isOk = False
        while (0 < timeoutSec):
            try:
                if self.exists():
                    self.reload()
                    isOk = True
            except saklient.errors.httpexception.HttpException:
                pass
            timeoutSec -= step
            if isOk:
                timeoutSec = 0
            if 0 < timeoutSec:
                Util.sleep(step)
        return isOk
    
    ## このルータが接続されているスイッチを取得します。
    # 
    # @return {Swytch}
    def get_swytch(self):
        model = Util.create_class_instance("saklient.cloud.models.Model_Swytch", [self._client])
        id = self.get_swytch_id()
        return model.get_by_id(id)
    
    ## このルータ＋スイッチでIPv6アドレスを有効にします。
    # 
    # @return {saklient.cloud.resources.ipv6net.Ipv6Net} 有効化されたIPv6ネットワーク
    def add_ipv6_net(self):
        result = self._client.request("POST", self._api_path() + "/" + Util.url_encode(self._id()) + "/ipv6net")
        self.reload()
        return Ipv6Net(self._client, (result["IPv6Net"] if "IPv6Net" in result else None))
    
    ## このルータ＋スイッチでIPv6アドレスを無効にします。
    # 
    # @param {saklient.cloud.resources.ipv6net.Ipv6Net} ipv6Net
    # @return {saklient.cloud.resources.router.Router} this
    def remove_ipv6_net(self, ipv6Net):
        Util.validate_type(ipv6Net, "saklient.cloud.resources.ipv6net.Ipv6Net")
        self._client.request("DELETE", self._api_path() + "/" + Util.url_encode(self._id()) + "/ipv6net/" + ipv6Net._id())
        self.reload()
        return self
    
    ## このルータ＋スイッチにスタティックルートを追加します。
    # 
    # @param {int} maskLen
    # @param {str} nextHop
    # @return {saklient.cloud.resources.ipv4net.Ipv4Net} 追加されたスタティックルート
    def add_static_route(self, maskLen, nextHop):
        Util.validate_type(maskLen, "int")
        Util.validate_type(nextHop, "str")
        q = {}
        Util.set_by_path(q, "NetworkMaskLen", maskLen)
        Util.set_by_path(q, "NextHop", nextHop)
        result = self._client.request("POST", self._api_path() + "/" + Util.url_encode(self._id()) + "/subnet", q)
        self.reload()
        return Ipv4Net(self._client, (result["Subnet"] if "Subnet" in result else None))
    
    ## このルータ＋スイッチからスタティックルートを削除します。
    # 
    # @param {saklient.cloud.resources.ipv4net.Ipv4Net} ipv4Net
    # @return {saklient.cloud.resources.router.Router} this
    def remove_static_route(self, ipv4Net):
        Util.validate_type(ipv4Net, "saklient.cloud.resources.ipv4net.Ipv4Net")
        self._client.request("DELETE", self._api_path() + "/" + Util.url_encode(self._id()) + "/subnet/" + ipv4Net._id())
        self.reload()
        return self
    
    ## このルータ＋スイッチの帯域プランを変更します。
    # 
    # 成功時はリソースIDが変わることにご注意ください。
    # 
    # @param {int} bandWidthMbps
    # @return {saklient.cloud.resources.router.Router} this
    def change_plan(self, bandWidthMbps):
        Util.validate_type(bandWidthMbps, "int")
        path = self._api_path() + "/" + Util.url_encode(self._id()) + "/bandwidth"
        q = {}
        Util.set_by_path(q, "Internet.BandWidthMbps", bandWidthMbps)
        result = self._client.request("PUT", path, q)
        self.api_deserialize(result, True)
        return self
    
    # (instance field) n_id = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_id(self):
        return self.m_id
    
    ## ID
    id = property(get_id, None, None)
    
    # (instance field) n_name = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_name(self):
        return self.m_name
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {str} v
    # @return {str}
    def set_name(self, v):
        Util.validate_type(v, "str")
        self.m_name = v
        self.n_name = True
        return self.m_name
    
    ## 名前
    name = property(get_name, set_name, None)
    
    # (instance field) n_description = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_description(self):
        return self.m_description
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {str} v
    # @return {str}
    def set_description(self, v):
        Util.validate_type(v, "str")
        self.m_description = v
        self.n_description = True
        return self.m_description
    
    ## 説明
    description = property(get_description, set_description, None)
    
    # (instance field) n_network_mask_len = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {int}
    def get_network_mask_len(self):
        return self.m_network_mask_len
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {int} v
    # @return {int}
    def set_network_mask_len(self, v):
        Util.validate_type(v, "int")
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.router.Router#network_mask_len")
        self.m_network_mask_len = v
        self.n_network_mask_len = True
        return self.m_network_mask_len
    
    ## ネットワークのマスク長
    network_mask_len = property(get_network_mask_len, set_network_mask_len, None)
    
    # (instance field) n_band_width_mbps = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {int}
    def get_band_width_mbps(self):
        return self.m_band_width_mbps
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {int} v
    # @return {int}
    def set_band_width_mbps(self, v):
        Util.validate_type(v, "int")
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.router.Router#band_width_mbps")
        self.m_band_width_mbps = v
        self.n_band_width_mbps = True
        return self.m_band_width_mbps
    
    ## 帯域幅
    band_width_mbps = property(get_band_width_mbps, set_band_width_mbps, None)
    
    # (instance field) n_swytch_id = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_swytch_id(self):
        return self.m_swytch_id
    
    ## スイッチ
    swytch_id = property(get_swytch_id, None, None)
    
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
        if Util.exists_path(r, "Name"):
            self.m_name = None if Util.get_by_path(r, "Name") is None else str(Util.get_by_path(r, "Name"))
        else:
            self.m_name = None
            self.is_incomplete = True
        self.n_name = False
        if Util.exists_path(r, "Description"):
            self.m_description = None if Util.get_by_path(r, "Description") is None else str(Util.get_by_path(r, "Description"))
        else:
            self.m_description = None
            self.is_incomplete = True
        self.n_description = False
        if Util.exists_path(r, "NetworkMaskLen"):
            self.m_network_mask_len = None if Util.get_by_path(r, "NetworkMaskLen") is None else int(str(Util.get_by_path(r, "NetworkMaskLen")))
        else:
            self.m_network_mask_len = None
            self.is_incomplete = True
        self.n_network_mask_len = False
        if Util.exists_path(r, "BandWidthMbps"):
            self.m_band_width_mbps = None if Util.get_by_path(r, "BandWidthMbps") is None else int(str(Util.get_by_path(r, "BandWidthMbps")))
        else:
            self.m_band_width_mbps = None
            self.is_incomplete = True
        self.n_band_width_mbps = False
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
        if withClean or self.n_name:
            Util.set_by_path(ret, "Name", self.m_name)
        else:
            if self.is_new:
                missing.append("name")
        if withClean or self.n_description:
            Util.set_by_path(ret, "Description", self.m_description)
        if withClean or self.n_network_mask_len:
            Util.set_by_path(ret, "NetworkMaskLen", self.m_network_mask_len)
        else:
            if self.is_new:
                missing.append("network_mask_len")
        if withClean or self.n_band_width_mbps:
            Util.set_by_path(ret, "BandWidthMbps", self.m_band_width_mbps)
        else:
            if self.is_new:
                missing.append("band_width_mbps")
        if withClean or self.n_swytch_id:
            Util.set_by_path(ret, "Switch.ID", self.m_swytch_id)
        if len(missing) > 0:
            raise SaklientException("required_field", "Required fields must be set before the Router creation: " + ", ".join(missing))
        return ret
    
