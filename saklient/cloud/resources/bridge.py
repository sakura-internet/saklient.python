# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.saklientexception import SaklientException
from ..client import Client
from .resource import Resource
from .region import Region
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.bridge

class Bridge(Resource):
    ## ブリッジの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_name
    
    # (instance field) m_description
    
    # (instance field) m_region
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/bridge"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "Bridge"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "Bridges"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "Bridge"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @return {saklient.cloud.resources.bridge.Bridge} this
    def save(self):
        return self._save()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {saklient.cloud.resources.bridge.Bridge} this
    def reload(self):
        return self._reload()
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(Bridge, self).__init__(client)
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
    
    # (instance field) n_region = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resources.region.Region}
    def get_region(self):
        return self.m_region
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {saklient.cloud.resources.region.Region} v
    # @return {saklient.cloud.resources.region.Region}
    def set_region(self, v):
        Util.validate_type(v, "saklient.cloud.resources.region.Region")
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.bridge.Bridge#region")
        self.m_region = v
        self.n_region = True
        return self.m_region
    
    ## リージョン
    region = property(get_region, set_region, None)
    
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
        if Util.exists_path(r, "Region"):
            self.m_region = None if Util.get_by_path(r, "Region") is None else Region(self._client, Util.get_by_path(r, "Region"))
        else:
            self.m_region = None
            self.is_incomplete = True
        self.n_region = False
    
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
        if withClean or self.n_region:
            Util.set_by_path(ret, "Region", (None if self.m_region is None else self.m_region.api_serialize(withClean)) if withClean else ({
                'ID': "0"
            } if self.m_region is None else self.m_region.api_serialize_id()))
        if len(missing) > 0:
            raise SaklientException("required_field", "Required fields must be set before the Bridge creation: " + ", ".join(missing))
        return ret
    
