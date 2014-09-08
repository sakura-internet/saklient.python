# -*- coding:utf-8 -*-

from ...errors.saklientexception import SaklientException
from ..client import Client
from .resource import Resource
from .icon import Icon
from .iface import Iface
from ..enums.eapplianceclass import EApplianceClass
from ...util import Util

# module saklient.cloud.resource.appliance

class Appliance(Resource):
    ## アプライアンスの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_clazz
    
    # (instance field) m_name
    
    # (instance field) m_description
    
    # (instance field) m_tags
    
    # (instance field) m_icon
    
    # (instance field) m_ifaces
    
    # (instance field) m_service_class
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/appliance"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "Appliance"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "Appliances"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "Appliance"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @return {saklient.cloud.resource.appliance.Appliance} this
    def save(self):
        return self._save()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {saklient.cloud.resource.appliance.Appliance} this
    def reload(self):
        return self._reload()
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(Appliance, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self.api_deserialize(obj, wrapped)
    
    ## アプライアンスを起動します。
    # 
    # @return {saklient.cloud.resource.appliance.Appliance} this
    def boot(self):
        self._client.request("PUT", self._api_path() + "/" + Util.url_encode(self._id()) + "/power")
        return self
    
    ## アプライアンスをシャットダウンします。
    # 
    # @return {saklient.cloud.resource.appliance.Appliance} this
    def shutdown(self):
        self._client.request("DELETE", self._api_path() + "/" + Util.url_encode(self._id()) + "/power")
        return self
    
    ## アプライアンスを強制停止します。
    # 
    # @return {saklient.cloud.resource.appliance.Appliance} this
    def stop(self):
        self._client.request("DELETE", self._api_path() + "/" + Util.url_encode(self._id()) + "/power", {
            'Force': True
        })
        return self
    
    ## アプライアンスを強制再起動します。
    # 
    # @return {saklient.cloud.resource.appliance.Appliance} this
    def reboot(self):
        self._client.request("PUT", self._api_path() + "/" + Util.url_encode(self._id()) + "/reset")
        return self
    
    # (instance field) n_id = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_id(self):
        return self.m_id
    
    ## ID
    id = property(get_id, None, None)
    
    # (instance field) n_clazz = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_clazz(self):
        return self.m_clazz
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {str} v
    # @return {str}
    def set_clazz(self, v):
        Util.validate_type(v, "str")
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resource.appliance.Appliance#clazz")
        self.m_clazz = v
        self.n_clazz = True
        return self.m_clazz
    
    ## クラス {@link EApplianceClass}
    clazz = property(get_clazz, set_clazz, None)
    
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
    
    # (instance field) n_tags = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str[]}
    def get_tags(self):
        return self.m_tags
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {str[]} v
    # @return {str[]}
    def set_tags(self, v):
        Util.validate_type(v, "list")
        self.m_tags = v
        self.n_tags = True
        return self.m_tags
    
    ## タグ
    tags = property(get_tags, set_tags, None)
    
    # (instance field) n_icon = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resource.icon.Icon}
    def get_icon(self):
        return self.m_icon
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {saklient.cloud.resource.icon.Icon} v
    # @return {saklient.cloud.resource.icon.Icon}
    def set_icon(self, v):
        Util.validate_type(v, "saklient.cloud.resource.icon.Icon")
        self.m_icon = v
        self.n_icon = True
        return self.m_icon
    
    ## アイコン
    icon = property(get_icon, set_icon, None)
    
    # (instance field) n_ifaces = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resource.iface.Iface[]}
    def get_ifaces(self):
        return self.m_ifaces
    
    ## プラン
    ifaces = property(get_ifaces, None, None)
    
    # (instance field) n_service_class = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_service_class(self):
        return self.m_service_class
    
    ## サービスクラス
    service_class = property(get_service_class, None, None)
    
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
        if Util.exists_path(r, "Class"):
            self.m_clazz = None if Util.get_by_path(r, "Class") is None else str(Util.get_by_path(r, "Class"))
        else:
            self.m_clazz = None
            self.is_incomplete = True
        self.n_clazz = False
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
        if Util.exists_path(r, "Tags"):
            if Util.get_by_path(r, "Tags") is None:
                self.m_tags = []
            else:
                self.m_tags = []
                for t in Util.get_by_path(r, "Tags"):
                    v1 = None
                    v1 = None if t is None else str(t)
                    self.m_tags.append(v1)
        else:
            self.m_tags = None
            self.is_incomplete = True
        self.n_tags = False
        if Util.exists_path(r, "Icon"):
            self.m_icon = None if Util.get_by_path(r, "Icon") is None else Icon(self._client, Util.get_by_path(r, "Icon"))
        else:
            self.m_icon = None
            self.is_incomplete = True
        self.n_icon = False
        if Util.exists_path(r, "Interfaces"):
            if Util.get_by_path(r, "Interfaces") is None:
                self.m_ifaces = []
            else:
                self.m_ifaces = []
                for t in Util.get_by_path(r, "Interfaces"):
                    v2 = None
                    v2 = None if t is None else Iface(self._client, t)
                    self.m_ifaces.append(v2)
        else:
            self.m_ifaces = None
            self.is_incomplete = True
        self.n_ifaces = False
        if Util.exists_path(r, "ServiceClass"):
            self.m_service_class = None if Util.get_by_path(r, "ServiceClass") is None else str(Util.get_by_path(r, "ServiceClass"))
        else:
            self.m_service_class = None
            self.is_incomplete = True
        self.n_service_class = False
    
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
        if withClean or self.n_clazz:
            Util.set_by_path(ret, "Class", self.m_clazz)
        else:
            if self.is_new:
                missing.append("clazz")
        if withClean or self.n_name:
            Util.set_by_path(ret, "Name", self.m_name)
        else:
            if self.is_new:
                missing.append("name")
        if withClean or self.n_description:
            Util.set_by_path(ret, "Description", self.m_description)
        if withClean or self.n_tags:
            Util.set_by_path(ret, "Tags", [])
            for r1 in self.m_tags:
                v = None
                v = r1
                ( (ret["Tags"] if "Tags" in ret else None ) if isinstance(ret, dict) else getattr(ret, "Tags")).append(v)
        if withClean or self.n_icon:
            Util.set_by_path(ret, "Icon", (None if self.m_icon is None else self.m_icon.api_serialize(withClean)) if withClean else ({
                'ID': "0"
            } if self.m_icon is None else self.m_icon.api_serialize_id()))
        if withClean or self.n_ifaces:
            Util.set_by_path(ret, "Interfaces", [])
            for r2 in self.m_ifaces:
                v = None
                v = (None if r2 is None else r2.api_serialize(withClean)) if withClean else ({
                    'ID': "0"
                } if r2 is None else r2.api_serialize_id())
                ( (ret["Interfaces"] if "Interfaces" in ret else None ) if isinstance(ret, dict) else getattr(ret, "Interfaces")).append(v)
        if withClean or self.n_service_class:
            Util.set_by_path(ret, "ServiceClass", self.m_service_class)
        if len(missing) > 0:
            raise SaklientException("required_field", "Required fields must be set before the Appliance creation: " + ", ".join(missing))
        return ret
    
