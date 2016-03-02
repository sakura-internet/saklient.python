# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.saklientexception import SaklientException
from ..client import Client
from .resource import Resource
from .commonserviceprovider import CommonServiceProvider
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.commonserviceitem

class CommonServiceItem(Resource):
    ## 共通サービス契約の実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_name
    
    # (instance field) m_description
    
    # (instance field) m_tags
    
    # (instance field) m_icon
    
    # (instance field) m_provider
    
    # (instance field) m_raw_settings
    
    # (instance field) m_raw_status
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/commonserviceitem"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "CommonServiceItem"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "CommonServiceItems"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "CommonServiceItem"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @return {saklient.cloud.resources.commonserviceitem.CommonServiceItem} this
    def save(self):
        return self._save()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {saklient.cloud.resources.commonserviceitem.CommonServiceItem} this
    def reload(self):
        return self._reload()
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(CommonServiceItem, self).__init__(client)
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
    # @return {Icon}
    def get_icon(self):
        return self.m_icon
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {Icon} v
    # @return {Icon}
    def set_icon(self, v):
        Util.validate_type(v, "Icon")
        self.m_icon = v
        self.n_icon = True
        return self.m_icon
    
    ## アイコン
    icon = property(get_icon, set_icon, None)
    
    # (instance field) n_provider = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resources.commonserviceprovider.CommonServiceProvider}
    def get_provider(self):
        return self.m_provider
    
    ## 共通サービスプロバイダ情報
    provider = property(get_provider, None, None)
    
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
    
    # (instance field) n_raw_status = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {any}
    def get_raw_status(self):
        return self.m_raw_status
    
    ## ステータスの生データ
    raw_status = property(get_raw_status, None, None)
    
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
        if Util.exists_path(r, "CommonServiceProvider"):
            self.m_provider = None if Util.get_by_path(r, "CommonServiceProvider") is None else CommonServiceProvider(self._client, Util.get_by_path(r, "CommonServiceProvider"))
        else:
            self.m_provider = None
            self.is_incomplete = True
        self.n_provider = False
        if Util.exists_path(r, "Settings"):
            self.m_raw_settings = Util.get_by_path(r, "Settings")
        else:
            self.m_raw_settings = None
            self.is_incomplete = True
        self.n_raw_settings = False
        if Util.exists_path(r, "Status"):
            self.m_raw_status = Util.get_by_path(r, "Status")
        else:
            self.m_raw_status = None
            self.is_incomplete = True
        self.n_raw_status = False
    
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
        if withClean or self.n_provider:
            Util.set_by_path(ret, "CommonServiceProvider", (None if self.m_provider is None else self.m_provider.api_serialize(withClean)) if withClean else ({
                'ID': "0"
            } if self.m_provider is None else self.m_provider.api_serialize_id()))
        if withClean or self.n_raw_settings:
            Util.set_by_path(ret, "Settings", self.m_raw_settings)
        if withClean or self.n_raw_status:
            Util.set_by_path(ret, "Status", self.m_raw_status)
        if len(missing) > 0:
            raise SaklientException("required_field", "Required fields must be set before the CommonServiceItem creation: " + ", ".join(missing))
        return ret
    
