# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httpexception import HttpException
from ...errors.saklientexception import SaklientException
from ..client import Client
from .resource import Resource
from .icon import Icon
from .iface import Iface
from .serverplan import ServerPlan
from .serverinstance import ServerInstance
from .isoimage import IsoImage
from .serveractivity import ServerActivity
from ..enums.eserverinstancestatus import EServerInstanceStatus
from ..enums.eavailability import EAvailability
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.server

class Server(Resource):
    ## サーバの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_name
    
    # (instance field) m_description
    
    # (instance field) m_tags
    
    # (instance field) m_icon
    
    # (instance field) m_plan
    
    # (instance field) m_ifaces
    
    # (instance field) m_instance
    
    # (instance field) m_availability
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/server"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "Server"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "Servers"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "Server"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @return {saklient.cloud.resources.server.Server} this
    def save(self):
        return self._save()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {saklient.cloud.resources.server.Server} this
    def reload(self):
        return self._reload()
    
    # (instance field) _activity
    
    ## @return {saklient.cloud.resources.serveractivity.ServerActivity}
    def get_activity(self):
        return self._activity
    
    ## アクティビティ
    activity = property(get_activity, None, None)
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(Server, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self._activity = ServerActivity(client)
        self.api_deserialize(obj, wrapped)
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_before_api_deserialize(self, r, root):
        if r is None:
            return
        id = (r["ID"] if "ID" in r else None)
        ifaces = (r["Interfaces"] if "Interfaces" in r else None)
        if ifaces is not None:
            for iface in ifaces:
                server = None
                if ( "Server" in iface if isinstance(iface, dict) else hasattr(iface, "Server")):
                    server = (iface["Server"] if "Server" in iface else None)
                else:
                    server = {}
                    iface["Server"] = server
                server["ID"] = id
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_after_api_deserialize(self, r, root):
        if r is not None:
            self._activity.set_source_id(self._id())
    
    ## サーバが起動しているときtrueを返します。
    # 
    # @return {bool}
    def is_up(self):
        return self.get_instance().is_up()
    
    ## サーバが停止しているときtrueを返します。
    # 
    # @return {bool}
    def is_down(self):
        return self.get_instance().is_down()
    
    ## サーバを起動します。
    # 
    # @return {saklient.cloud.resources.server.Server} this
    def boot(self):
        self._client.request("PUT", self._api_path() + "/" + Util.url_encode(self._id()) + "/power")
        return self.reload()
    
    ## サーバをシャットダウンします。
    # 
    # @return {saklient.cloud.resources.server.Server} this
    def shutdown(self):
        self._client.request("DELETE", self._api_path() + "/" + Util.url_encode(self._id()) + "/power")
        return self.reload()
    
    ## サーバを強制停止します。
    # 
    # @return {saklient.cloud.resources.server.Server} this
    def stop(self):
        self._client.request("DELETE", self._api_path() + "/" + Util.url_encode(self._id()) + "/power", {
            'Force': True
        })
        return self.reload()
    
    ## サーバを強制再起動します。
    # 
    # @return {saklient.cloud.resources.server.Server} this
    def reboot(self):
        self._client.request("PUT", self._api_path() + "/" + Util.url_encode(self._id()) + "/reset")
        return self.reload()
    
    ## サーバが起動するまで待機します。
    # 
    # @param {int} timeoutSec=180
    # @return {bool}
    def sleep_until_up(self, timeoutSec=180):
        Util.validate_type(timeoutSec, "int")
        return self.sleep_until(EServerInstanceStatus.up, timeoutSec)
    
    ## サーバが停止するまで待機します。
    # 
    # @param {int} timeoutSec=180
    # @return {bool} 成功時はtrue、タイムアウトやエラーによる失敗時はfalseを返します。
    def sleep_until_down(self, timeoutSec=180):
        Util.validate_type(timeoutSec, "int")
        return self.sleep_until(EServerInstanceStatus.down, timeoutSec)
    
    ## サーバが指定のステータスに遷移するまで待機します。
    # 
    # @ignore
    # @param {str} status
    # @param {int} timeoutSec=180
    # @return {bool}
    def sleep_until(self, status, timeoutSec=180):
        Util.validate_type(status, "str")
        Util.validate_type(timeoutSec, "int")
        step = 10
        while (0 < timeoutSec):
            try:
                self.reload()
            except saklient.errors.httpexception.HttpException:
                pass
            s = None
            inst = self.instance
            if inst is not None:
                s = inst.status
            if s is None:
                s = EServerInstanceStatus.down
            if s == status:
                return True
            timeoutSec -= step
            if 0 < timeoutSec:
                Util.sleep(step)
        return False
    
    ## サーバプランを変更します。
    # 
    # 成功時はリソースIDが変わることにご注意ください。
    # 
    # @param {saklient.cloud.resources.serverplan.ServerPlan} planTo
    # @return {saklient.cloud.resources.server.Server} this
    def change_plan(self, planTo):
        Util.validate_type(planTo, "saklient.cloud.resources.serverplan.ServerPlan")
        path = self._api_path() + "/" + Util.url_encode(self._id()) + "/to/plan/" + Util.url_encode(planTo._id())
        result = self._client.request("PUT", path)
        self.api_deserialize(result, True)
        return self
    
    ## サーバにインタフェースを1つ増設し、それを取得します。
    # 
    # @return {saklient.cloud.resources.iface.Iface} 増設されたインタフェース
    def add_iface(self):
        model = Util.create_class_instance("saklient.cloud.models.Model_Iface", [self._client])
        res = model.create()
        res.server_id = self._id()
        return res.save()
    
    ## サーバにISOイメージを挿入します。
    # 
    # @param {saklient.cloud.resources.isoimage.IsoImage} iso
    # @return {saklient.cloud.resources.server.Server} this
    def insert_iso_image(self, iso):
        Util.validate_type(iso, "saklient.cloud.resources.isoimage.IsoImage")
        path = self._api_path() + "/" + Util.url_encode(self._id()) + "/cdrom"
        q = {
            'CDROM': {
                'ID': iso._id()
            }
        }
        self._client.request("PUT", path, q)
        self.reload()
        return self
    
    ## サーバに挿入されているISOイメージを排出します。
    # 
    # @return {saklient.cloud.resources.server.Server} this
    def eject_iso_image(self):
        path = self._api_path() + "/" + Util.url_encode(self._id()) + "/cdrom"
        self._client.request("DELETE", path)
        self.reload()
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
    
    # (instance field) n_plan = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resources.serverplan.ServerPlan}
    def get_plan(self):
        return self.m_plan
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {saklient.cloud.resources.serverplan.ServerPlan} v
    # @return {saklient.cloud.resources.serverplan.ServerPlan}
    def set_plan(self, v):
        Util.validate_type(v, "saklient.cloud.resources.serverplan.ServerPlan")
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.server.Server#plan")
        self.m_plan = v
        self.n_plan = True
        return self.m_plan
    
    ## プラン
    plan = property(get_plan, set_plan, None)
    
    # (instance field) n_ifaces = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resources.iface.Iface[]}
    def get_ifaces(self):
        return self.m_ifaces
    
    ## インタフェース
    ifaces = property(get_ifaces, None, None)
    
    # (instance field) n_instance = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resources.serverinstance.ServerInstance}
    def get_instance(self):
        return self.m_instance
    
    ## インスタンス情報
    instance = property(get_instance, None, None)
    
    # (instance field) n_availability = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_availability(self):
        return self.m_availability
    
    ## 有効状態 {@link EAvailability}
    availability = property(get_availability, None, None)
    
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
        if Util.exists_path(r, "ServerPlan"):
            self.m_plan = None if Util.get_by_path(r, "ServerPlan") is None else ServerPlan(self._client, Util.get_by_path(r, "ServerPlan"))
        else:
            self.m_plan = None
            self.is_incomplete = True
        self.n_plan = False
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
        if Util.exists_path(r, "Instance"):
            self.m_instance = None if Util.get_by_path(r, "Instance") is None else ServerInstance(self._client, Util.get_by_path(r, "Instance"))
        else:
            self.m_instance = None
            self.is_incomplete = True
        self.n_instance = False
        if Util.exists_path(r, "Availability"):
            self.m_availability = None if Util.get_by_path(r, "Availability") is None else str(Util.get_by_path(r, "Availability"))
        else:
            self.m_availability = None
            self.is_incomplete = True
        self.n_availability = False
    
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
        if withClean or self.n_plan:
            Util.set_by_path(ret, "ServerPlan", (None if self.m_plan is None else self.m_plan.api_serialize(withClean)) if withClean else ({
                'ID': "0"
            } if self.m_plan is None else self.m_plan.api_serialize_id()))
        else:
            if self.is_new:
                missing.append("plan")
        if withClean or self.n_ifaces:
            Util.set_by_path(ret, "Interfaces", [])
            for r2 in self.m_ifaces:
                v = None
                v = (None if r2 is None else r2.api_serialize(withClean)) if withClean else ({
                    'ID': "0"
                } if r2 is None else r2.api_serialize_id())
                (ret["Interfaces"] if "Interfaces" in ret else None).append(v)
        if withClean or self.n_instance:
            Util.set_by_path(ret, "Instance", (None if self.m_instance is None else self.m_instance.api_serialize(withClean)) if withClean else ({
                'ID': "0"
            } if self.m_instance is None else self.m_instance.api_serialize_id()))
        if withClean or self.n_availability:
            Util.set_by_path(ret, "Availability", self.m_availability)
        if len(missing) > 0:
            raise SaklientException("required_field", "Required fields must be set before the Server creation: " + ", ".join(missing))
        return ret
    
