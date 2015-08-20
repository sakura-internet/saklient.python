# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.saklientexception import SaklientException
from ..client import Client
from .resource import Resource
from ..enums.escope import EScope
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.icon

class Icon(Resource):
    ## アイコンの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_scope
    
    # (instance field) m_name
    
    # (instance field) m_url
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/icon"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "Icon"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "Icons"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "Icon"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @return {saklient.cloud.resources.icon.Icon} this
    def save(self):
        return self._save()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {saklient.cloud.resources.icon.Icon} this
    def reload(self):
        return self._reload()
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(Icon, self).__init__(client)
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
    
    # (instance field) n_scope = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_scope(self):
        return self.m_scope
    
    ## スコープ {@link EScope}
    scope = property(get_scope, None, None)
    
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
    
    # (instance field) n_url = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_url(self):
        return self.m_url
    
    ## URL
    url = property(get_url, None, None)
    
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
        if Util.exists_path(r, "Scope"):
            self.m_scope = None if Util.get_by_path(r, "Scope") is None else str(Util.get_by_path(r, "Scope"))
        else:
            self.m_scope = None
            self.is_incomplete = True
        self.n_scope = False
        if Util.exists_path(r, "Name"):
            self.m_name = None if Util.get_by_path(r, "Name") is None else str(Util.get_by_path(r, "Name"))
        else:
            self.m_name = None
            self.is_incomplete = True
        self.n_name = False
        if Util.exists_path(r, "URL"):
            self.m_url = None if Util.get_by_path(r, "URL") is None else str(Util.get_by_path(r, "URL"))
        else:
            self.m_url = None
            self.is_incomplete = True
        self.n_url = False
    
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
        if withClean or self.n_scope:
            Util.set_by_path(ret, "Scope", self.m_scope)
        if withClean or self.n_name:
            Util.set_by_path(ret, "Name", self.m_name)
        else:
            if self.is_new:
                missing.append("name")
        if withClean or self.n_url:
            Util.set_by_path(ret, "URL", self.m_url)
        if len(missing) > 0:
            raise SaklientException("required_field", "Required fields must be set before the Icon creation: " + ", ".join(missing))
        return ret
    
