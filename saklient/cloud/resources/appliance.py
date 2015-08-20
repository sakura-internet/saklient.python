# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpexception import HttpException
from ...errors.saklientexception import SaklientException
from ..client import Client
from .resource import Resource
from .icon import Icon
from .iface import Iface
from .swytch import Swytch
from ..enums.eapplianceclass import EApplianceClass
from ..enums.eavailability import EAvailability
from ..enums.eserverinstancestatus import EServerInstanceStatus
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.appliance

class Appliance(Resource):
    ## アプライアンスの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_clazz
    
    # (instance field) m_name
    
    # (instance field) m_description
    
    # (instance field) m_tags
    
    # (instance field) m_icon
    
    # (instance field) m_plan_id
    
    # (instance field) m_ifaces
    
    # (instance field) m_raw_annotation
    
    # (instance field) m_raw_settings
    
    # (instance field) m_raw_settings_hash
    
    # (instance field) m_status
    
    # (instance field) m_service_class
    
    # (instance field) m_availability
    
    # (instance field) m_swytch_id
    
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
    # @return {saklient.cloud.resources.appliance.Appliance} this
    def save(self):
        return self._save()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {saklient.cloud.resources.appliance.Appliance} this
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
    
    ## @private
    # @param {any} query
    # @return {void}
    def _on_before_save(self, query):
        Util.set_by_path(query, "OriginalSettingsHash", self.get_raw_settings_hash())
    
    ## このルータが接続されているスイッチを取得します。
    # 
    # @return {saklient.cloud.resources.swytch.Swytch}
    def get_swytch(self):
        model = Util.create_class_instance("saklient.cloud.models.Model_Swytch", [self._client])
        id = self.get_swytch_id()
        return model.get_by_id(id)
    
    ## アプライアンスの設定を反映します。
    # 
    # @return {saklient.cloud.resources.appliance.Appliance} this
    def apply(self):
        self._client.request("PUT", self._api_path() + "/" + Util.url_encode(self._id()) + "/config")
        return self
    
    ## アプライアンスを起動します。
    # 
    # @return {saklient.cloud.resources.appliance.Appliance} this
    def boot(self):
        self._client.request("PUT", self._api_path() + "/" + Util.url_encode(self._id()) + "/power")
        return self
    
    ## アプライアンスをシャットダウンします。
    # 
    # @return {saklient.cloud.resources.appliance.Appliance} this
    def shutdown(self):
        self._client.request("DELETE", self._api_path() + "/" + Util.url_encode(self._id()) + "/power")
        return self
    
    ## アプライアンスを強制停止します。
    # 
    # @return {saklient.cloud.resources.appliance.Appliance} this
    def stop(self):
        self._client.request("DELETE", self._api_path() + "/" + Util.url_encode(self._id()) + "/power", {
            'Force': True
        })
        return self
    
    ## アプライアンスを強制再起動します。
    # 
    # @return {saklient.cloud.resources.appliance.Appliance} this
    def reboot(self):
        self._client.request("PUT", self._api_path() + "/" + Util.url_encode(self._id()) + "/reset")
        return self
    
    ## 作成中のアプライアンスが利用可能になるまで待機します。
    # 
    # @param {int} timeoutSec=600
    # @return {bool} 成功時はtrue、タイムアウトやエラーによる失敗時はfalseを返します。
    def sleep_while_creating(self, timeoutSec=600):
        Util.validate_type(timeoutSec, "int")
        step = 10
        while (0 < timeoutSec):
            try:
                self.reload()
            except saklient.errors.httpexception.HttpException:
                pass
            a = self.get_availability()
            if a == EAvailability.available:
                return True
            if a != EAvailability.migrating:
                timeoutSec = 0
            timeoutSec -= step
            if 0 < timeoutSec:
                Util.sleep(step)
        return False
    
    ## アプライアンスが起動するまで待機します。
    # 
    # @param {int} timeoutSec=600
    # @return {bool}
    def sleep_until_up(self, timeoutSec=600):
        Util.validate_type(timeoutSec, "int")
        return self.sleep_until(EServerInstanceStatus.up, timeoutSec)
    
    ## アプライアンスが停止するまで待機します。
    # 
    # @param {int} timeoutSec=600
    # @return {bool} 成功時はtrue、タイムアウトやエラーによる失敗時はfalseを返します。
    def sleep_until_down(self, timeoutSec=600):
        Util.validate_type(timeoutSec, "int")
        return self.sleep_until(EServerInstanceStatus.down, timeoutSec)
    
    ## アプライアンスが指定のステータスに遷移するまで待機します。
    # 
    # @ignore
    # @param {str} status
    # @param {int} timeoutSec=600
    # @return {bool}
    def sleep_until(self, status, timeoutSec=600):
        Util.validate_type(status, "str")
        Util.validate_type(timeoutSec, "int")
        step = 10
        while (0 < timeoutSec):
            try:
                self.reload()
            except saklient.errors.httpexception.HttpException:
                pass
            s = self.get_status()
            if s is None:
                s = EServerInstanceStatus.down
            if s == status:
                return True
            timeoutSec -= step
            if 0 < timeoutSec:
                Util.sleep(step)
        return False
    
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
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.appliance.Appliance#clazz")
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
        self.n_tags = True
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
    
    ## タグ文字列の配列
    tags = property(get_tags, set_tags, None)
    
    # (instance field) n_icon = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resources.icon.Icon}
    def get_icon(self):
        return self.m_icon
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {saklient.cloud.resources.icon.Icon} v
    # @return {saklient.cloud.resources.icon.Icon}
    def set_icon(self, v):
        Util.validate_type(v, "saklient.cloud.resources.icon.Icon")
        self.m_icon = v
        self.n_icon = True
        return self.m_icon
    
    ## アイコン
    icon = property(get_icon, set_icon, None)
    
    # (instance field) n_plan_id = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {int}
    def get_plan_id(self):
        return self.m_plan_id
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {int} v
    # @return {int}
    def set_plan_id(self, v):
        Util.validate_type(v, "int")
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.appliance.Appliance#plan_id")
        self.m_plan_id = v
        self.n_plan_id = True
        return self.m_plan_id
    
    ## プラン
    plan_id = property(get_plan_id, set_plan_id, None)
    
    # (instance field) n_ifaces = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resources.iface.Iface[]}
    def get_ifaces(self):
        return self.m_ifaces
    
    ## インタフェース {@link Iface} の配列
    ifaces = property(get_ifaces, None, None)
    
    # (instance field) n_raw_annotation = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {any}
    def get_raw_annotation(self):
        return self.m_raw_annotation
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {any} v
    # @return {any}
    def set_raw_annotation(self, v):
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.appliance.Appliance#raw_annotation")
        self.m_raw_annotation = v
        self.n_raw_annotation = True
        return self.m_raw_annotation
    
    ## 注釈
    raw_annotation = property(get_raw_annotation, set_raw_annotation, None)
    
    # (instance field) n_raw_settings = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {any}
    def get_raw_settings(self):
        self.n_raw_settings = True
        return self.m_raw_settings
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {any} v
    # @return {any}
    def set_raw_settings(self, v):
        self.m_raw_settings = v
        self.n_raw_settings = True
        return self.m_raw_settings
    
    ## 設定の生データ
    raw_settings = property(get_raw_settings, set_raw_settings, None)
    
    # (instance field) n_raw_settings_hash = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_raw_settings_hash(self):
        return self.m_raw_settings_hash
    
    ## @ignore
    raw_settings_hash = property(get_raw_settings_hash, None, None)
    
    # (instance field) n_status = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_status(self):
        return self.m_status
    
    ## 起動状態 {@link EServerInstanceStatus}
    status = property(get_status, None, None)
    
    # (instance field) n_service_class = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_service_class(self):
        return self.m_service_class
    
    ## サービスクラス
    service_class = property(get_service_class, None, None)
    
    # (instance field) n_availability = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_availability(self):
        return self.m_availability
    
    ## 有効状態 {@link EAvailability}
    availability = property(get_availability, None, None)
    
    # (instance field) n_swytch_id = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_swytch_id(self):
        return self.m_swytch_id
    
    ## 接続先スイッチID
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
        if Util.exists_path(r, "Plan.ID"):
            self.m_plan_id = None if Util.get_by_path(r, "Plan.ID") is None else int(str(Util.get_by_path(r, "Plan.ID")))
        else:
            self.m_plan_id = None
            self.is_incomplete = True
        self.n_plan_id = False
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
        if Util.exists_path(r, "Remark"):
            self.m_raw_annotation = Util.get_by_path(r, "Remark")
        else:
            self.m_raw_annotation = None
            self.is_incomplete = True
        self.n_raw_annotation = False
        if Util.exists_path(r, "Settings"):
            self.m_raw_settings = Util.get_by_path(r, "Settings")
        else:
            self.m_raw_settings = None
            self.is_incomplete = True
        self.n_raw_settings = False
        if Util.exists_path(r, "SettingsHash"):
            self.m_raw_settings_hash = None if Util.get_by_path(r, "SettingsHash") is None else str(Util.get_by_path(r, "SettingsHash"))
        else:
            self.m_raw_settings_hash = None
            self.is_incomplete = True
        self.n_raw_settings_hash = False
        if Util.exists_path(r, "Instance.Status"):
            self.m_status = None if Util.get_by_path(r, "Instance.Status") is None else str(Util.get_by_path(r, "Instance.Status"))
        else:
            self.m_status = None
            self.is_incomplete = True
        self.n_status = False
        if Util.exists_path(r, "ServiceClass"):
            self.m_service_class = None if Util.get_by_path(r, "ServiceClass") is None else str(Util.get_by_path(r, "ServiceClass"))
        else:
            self.m_service_class = None
            self.is_incomplete = True
        self.n_service_class = False
        if Util.exists_path(r, "Availability"):
            self.m_availability = None if Util.get_by_path(r, "Availability") is None else str(Util.get_by_path(r, "Availability"))
        else:
            self.m_availability = None
            self.is_incomplete = True
        self.n_availability = False
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
                (ret["Tags"] if "Tags" in ret else None).append(v)
        if withClean or self.n_icon:
            Util.set_by_path(ret, "Icon", (None if self.m_icon is None else self.m_icon.api_serialize(withClean)) if withClean else ({
                'ID': "0"
            } if self.m_icon is None else self.m_icon.api_serialize_id()))
        if withClean or self.n_plan_id:
            Util.set_by_path(ret, "Plan.ID", self.m_plan_id)
        else:
            if self.is_new:
                missing.append("plan_id")
        if withClean or self.n_ifaces:
            Util.set_by_path(ret, "Interfaces", [])
            for r2 in self.m_ifaces:
                v = None
                v = (None if r2 is None else r2.api_serialize(withClean)) if withClean else ({
                    'ID': "0"
                } if r2 is None else r2.api_serialize_id())
                (ret["Interfaces"] if "Interfaces" in ret else None).append(v)
        if withClean or self.n_raw_annotation:
            Util.set_by_path(ret, "Remark", self.m_raw_annotation)
        else:
            if self.is_new:
                missing.append("raw_annotation")
        if withClean or self.n_raw_settings:
            Util.set_by_path(ret, "Settings", self.m_raw_settings)
        if withClean or self.n_raw_settings_hash:
            Util.set_by_path(ret, "SettingsHash", self.m_raw_settings_hash)
        if withClean or self.n_status:
            Util.set_by_path(ret, "Instance.Status", self.m_status)
        if withClean or self.n_service_class:
            Util.set_by_path(ret, "ServiceClass", self.m_service_class)
        if withClean or self.n_availability:
            Util.set_by_path(ret, "Availability", self.m_availability)
        if withClean or self.n_swytch_id:
            Util.set_by_path(ret, "Switch.ID", self.m_swytch_id)
        if len(missing) > 0:
            raise SaklientException("required_field", "Required fields must be set before the Appliance creation: " + ", ".join(missing))
        return ret
    
