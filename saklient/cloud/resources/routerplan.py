# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ..client import Client
from .resource import Resource
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.routerplan

class RouterPlan(Resource):
    ## ルータ帯域プラン情報の1レコードに対応するクラス。
    
    # (instance field) m_id
    
    # (instance field) m_name
    
    # (instance field) m_band_width_mbps
    
    # (instance field) m_service_class
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/product/internet"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "InternetPlan"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "InternetPlans"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "RouterPlan"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(RouterPlan, self).__init__(client)
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
    
    ## 名前
    name = property(get_name, None, None)
    
    # (instance field) n_band_width_mbps = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {int}
    def get_band_width_mbps(self):
        return self.m_band_width_mbps
    
    ## 帯域幅
    band_width_mbps = property(get_band_width_mbps, None, None)
    
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
        if Util.exists_path(r, "Name"):
            self.m_name = None if Util.get_by_path(r, "Name") is None else str(Util.get_by_path(r, "Name"))
        else:
            self.m_name = None
            self.is_incomplete = True
        self.n_name = False
        if Util.exists_path(r, "BandWidthMbps"):
            self.m_band_width_mbps = None if Util.get_by_path(r, "BandWidthMbps") is None else int(str(Util.get_by_path(r, "BandWidthMbps")))
        else:
            self.m_band_width_mbps = None
            self.is_incomplete = True
        self.n_band_width_mbps = False
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
        ret = {
            
        }
        if withClean or self.n_id:
            Util.set_by_path(ret, "ID", self.m_id)
        if withClean or self.n_name:
            Util.set_by_path(ret, "Name", self.m_name)
        if withClean or self.n_band_width_mbps:
            Util.set_by_path(ret, "BandWidthMbps", self.m_band_width_mbps)
        if withClean or self.n_service_class:
            Util.set_by_path(ret, "ServiceClass", self.m_service_class)
        return ret
    
