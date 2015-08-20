# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.saklientexception import SaklientException
from ...errors.httpexception import HttpException
from ..client import Client
from .resource import Resource
from .icon import Icon
from .diskplan import DiskPlan
from .server import Server
from .diskconfig import DiskConfig
from .diskactivity import DiskActivity
from ..enums.eavailability import EAvailability
from ..enums.ediskconnection import EDiskConnection
from ..enums.estorageclass import EStorageClass
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.disk

class Disk(Resource):
    ## ディスクの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_name
    
    # (instance field) m_description
    
    # (instance field) m_tags
    
    # (instance field) m_icon
    
    # (instance field) m_size_mib
    
    # (instance field) m_service_class
    
    # (instance field) m_plan
    
    # (instance field) m_server
    
    # (instance field) m_availability
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/disk"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "Disk"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "Disks"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "Disk"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @return {saklient.cloud.resources.disk.Disk} this
    def save(self):
        return self._save()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {saklient.cloud.resources.disk.Disk} this
    def reload(self):
        return self._reload()
    
    # (instance field) _activity
    
    ## @return {saklient.cloud.resources.diskactivity.DiskActivity}
    def get_activity(self):
        return self._activity
    
    ## アクティビティ
    activity = property(get_activity, None, None)
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(Disk, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self._activity = DiskActivity(client)
        self.api_deserialize(obj, wrapped)
    
    ## @return {bool}
    def get_is_available(self):
        return self.get_availability() == EAvailability.available
    
    ## ディスクが利用可能なときtrueを返します。
    is_available = property(get_is_available, None, None)
    
    ## @return {int}
    def get_size_gib(self):
        sizeMib = self.get_size_mib()
        return None if sizeMib is None else sizeMib >> 10
    
    ## @param {int} sizeGib
    # @return {int}
    def set_size_gib(self, sizeGib):
        Util.validate_type(sizeGib, "int")
        self.set_size_mib(None if sizeGib is None else sizeGib * 1024)
        return sizeGib
    
    ## サイズ[GiB]
    size_gib = property(get_size_gib, set_size_gib, None)
    
    # (instance field) _source
    
    ## @return {saklient.cloud.resources.resource.Resource}
    def get_source(self):
        return self._source
    
    ## @param {saklient.cloud.resources.resource.Resource} source
    # @return {saklient.cloud.resources.resource.Resource}
    def set_source(self, source):
        Util.validate_type(source, "saklient.cloud.resources.resource.Resource")
        self._source = source
        return source
    
    ## ディスクのコピー元
    source = property(get_source, set_source, None)
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_after_api_deserialize(self, r, root):
        if r is not None:
            self._activity.set_source_id(self._id())
            if ( "SourceDisk" in r if isinstance(r, dict) else hasattr(r, "SourceDisk")):
                s = (r["SourceDisk"] if "SourceDisk" in r else None)
                if s is not None:
                    id = (s["ID"] if "ID" in s else None)
                    if id is not None:
                        self._source = Disk(self._client, s)
            if ( "SourceArchive" in r if isinstance(r, dict) else hasattr(r, "SourceArchive")):
                s = (r["SourceArchive"] if "SourceArchive" in r else None)
                if s is not None:
                    id = (s["ID"] if "ID" in s else None)
                    if id is not None:
                        self._source = Resource.create_with("Archive", self._client, s)
    
    ## @private
    # @param {any} r
    # @param {bool} withClean
    # @return {void}
    def _on_after_api_serialize(self, r, withClean):
        Util.validate_type(withClean, "bool")
        if r is None:
            return
        if self._source is not None:
            if self._source._class_name() == "Disk":
                s = self._source.api_serialize(True) if withClean else {
                    'ID': self._source._id()
                }
                r["SourceDisk"] = s
            else:
                if self._source._class_name() == "Archive":
                    s = self._source.api_serialize(True) if withClean else {
                        'ID': self._source._id()
                    }
                    r["SourceArchive"] = s
                else:
                    self._source = None
                    Util.validate_type(self._source, "Disk or Archive", True)
    
    ## ディスクをサーバに取り付けます。
    # 
    # @param {saklient.cloud.resources.server.Server} server
    # @return {saklient.cloud.resources.disk.Disk} this
    def connect_to(self, server):
        Util.validate_type(server, "saklient.cloud.resources.server.Server")
        self._client.request("PUT", "/disk/" + self._id() + "/to/server/" + server._id())
        return self
    
    ## ディスクをサーバから取り外します。
    # 
    # @return {saklient.cloud.resources.disk.Disk} this
    def disconnect(self):
        self._client.request("DELETE", "/disk/" + self._id() + "/to/server")
        return self
    
    ## ディスク修正を行うためのオブジェクトを用意します。
    # 
    # 返り値のオブジェクトにパラメータを設定し、write() を呼ぶことで修正を行います。
    # 
    # @return {saklient.cloud.resources.diskconfig.DiskConfig}
    def create_config(self):
        return DiskConfig(self._client, self._id())
    
    ## コピー中のディスクが利用可能になるまで待機します。
    # 
    # @param {int} timeoutSec=3600
    # @return {bool} 成功時はtrue、タイムアウトやエラーによる失敗時はfalseを返します。
    def sleep_while_copying(self, timeoutSec=3600):
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
    
    # (instance field) n_size_mib = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {int}
    def get_size_mib(self):
        return self.m_size_mib
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {int} v
    # @return {int}
    def set_size_mib(self, v):
        Util.validate_type(v, "int")
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.disk.Disk#size_mib")
        self.m_size_mib = v
        self.n_size_mib = True
        return self.m_size_mib
    
    ## サイズ[MiB]
    size_mib = property(get_size_mib, set_size_mib, None)
    
    # (instance field) n_service_class = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_service_class(self):
        return self.m_service_class
    
    ## サービスクラス
    service_class = property(get_service_class, None, None)
    
    # (instance field) n_plan = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resources.diskplan.DiskPlan}
    def get_plan(self):
        return self.m_plan
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {saklient.cloud.resources.diskplan.DiskPlan} v
    # @return {saklient.cloud.resources.diskplan.DiskPlan}
    def set_plan(self, v):
        Util.validate_type(v, "saklient.cloud.resources.diskplan.DiskPlan")
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.disk.Disk#plan")
        self.m_plan = v
        self.n_plan = True
        return self.m_plan
    
    ## プラン
    plan = property(get_plan, set_plan, None)
    
    # (instance field) n_server = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resources.server.Server}
    def get_server(self):
        return self.m_server
    
    ## 接続先のサーバ
    server = property(get_server, None, None)
    
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
        if Util.exists_path(r, "SizeMB"):
            self.m_size_mib = None if Util.get_by_path(r, "SizeMB") is None else int(str(Util.get_by_path(r, "SizeMB")))
        else:
            self.m_size_mib = None
            self.is_incomplete = True
        self.n_size_mib = False
        if Util.exists_path(r, "ServiceClass"):
            self.m_service_class = None if Util.get_by_path(r, "ServiceClass") is None else str(Util.get_by_path(r, "ServiceClass"))
        else:
            self.m_service_class = None
            self.is_incomplete = True
        self.n_service_class = False
        if Util.exists_path(r, "Plan"):
            self.m_plan = None if Util.get_by_path(r, "Plan") is None else DiskPlan(self._client, Util.get_by_path(r, "Plan"))
        else:
            self.m_plan = None
            self.is_incomplete = True
        self.n_plan = False
        if Util.exists_path(r, "Server"):
            self.m_server = None if Util.get_by_path(r, "Server") is None else Server(self._client, Util.get_by_path(r, "Server"))
        else:
            self.m_server = None
            self.is_incomplete = True
        self.n_server = False
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
        if withClean or self.n_size_mib:
            Util.set_by_path(ret, "SizeMB", self.m_size_mib)
        if withClean or self.n_service_class:
            Util.set_by_path(ret, "ServiceClass", self.m_service_class)
        if withClean or self.n_plan:
            Util.set_by_path(ret, "Plan", (None if self.m_plan is None else self.m_plan.api_serialize(withClean)) if withClean else ({
                'ID': "0"
            } if self.m_plan is None else self.m_plan.api_serialize_id()))
        else:
            if self.is_new:
                missing.append("plan")
        if withClean or self.n_server:
            Util.set_by_path(ret, "Server", (None if self.m_server is None else self.m_server.api_serialize(withClean)) if withClean else ({
                'ID': "0"
            } if self.m_server is None else self.m_server.api_serialize_id()))
        if withClean or self.n_availability:
            Util.set_by_path(ret, "Availability", self.m_availability)
        if len(missing) > 0:
            raise SaklientException("required_field", "Required fields must be set before the Disk creation: " + ", ".join(missing))
        return ret
    
