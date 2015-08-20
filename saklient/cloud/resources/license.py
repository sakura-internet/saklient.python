# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.saklientexception import SaklientException
from ..client import Client
from .resource import Resource
from .licenseinfo import LicenseInfo
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.license

class License(Resource):
    ## ライセンスの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_name
    
    # (instance field) m_info
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/license"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "License"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "Licenses"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "License"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @return {saklient.cloud.resources.license.License} this
    def save(self):
        return self._save()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {saklient.cloud.resources.license.License} this
    def reload(self):
        return self._reload()
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(License, self).__init__(client)
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
    
    # (instance field) n_info = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resources.licenseinfo.LicenseInfo}
    def get_info(self):
        return self.m_info
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {saklient.cloud.resources.licenseinfo.LicenseInfo} v
    # @return {saklient.cloud.resources.licenseinfo.LicenseInfo}
    def set_info(self, v):
        Util.validate_type(v, "saklient.cloud.resources.licenseinfo.LicenseInfo")
        if not self.is_new:
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.license.License#info")
        self.m_info = v
        self.n_info = True
        return self.m_info
    
    ## ライセンス種別情報
    info = property(get_info, set_info, None)
    
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
        if Util.exists_path(r, "LicenseInfo"):
            self.m_info = None if Util.get_by_path(r, "LicenseInfo") is None else LicenseInfo(self._client, Util.get_by_path(r, "LicenseInfo"))
        else:
            self.m_info = None
            self.is_incomplete = True
        self.n_info = False
    
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
        if withClean or self.n_info:
            Util.set_by_path(ret, "LicenseInfo", (None if self.m_info is None else self.m_info.api_serialize(withClean)) if withClean else ({
                'ID': "0"
            } if self.m_info is None else self.m_info.api_serialize_id()))
        else:
            if self.is_new:
                missing.append("info")
        if len(missing) > 0:
            raise SaklientException("required_field", "Required fields must be set before the License creation: " + ", ".join(missing))
        return ret
    
