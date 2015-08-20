# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ..client import Client
from .resource import Resource
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.serverplan

class ServerPlan(Resource):
    ## サーバプラン情報の1レコードに対応するクラス。
    
    # (instance field) m_id
    
    # (instance field) m_name
    
    # (instance field) m_cpu
    
    # (instance field) m_memory_mib
    
    # (instance field) m_service_class
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/product/server"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "ServerPlan"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "ServerPlans"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "ServerPlan"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(ServerPlan, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self.api_deserialize(obj, wrapped)
    
    ## @return {int}
    def get_memory_gib(self):
        memoryMib = self.get_memory_mib()
        return None if memoryMib is None else memoryMib >> 10
    
    memory_gib = property(get_memory_gib, None, None)
    
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
    
    # (instance field) n_cpu = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {int}
    def get_cpu(self):
        return self.m_cpu
    
    ## 仮想コア数
    cpu = property(get_cpu, None, None)
    
    # (instance field) n_memory_mib = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {int}
    def get_memory_mib(self):
        return self.m_memory_mib
    
    ## メモリ容量[MiB]
    memory_mib = property(get_memory_mib, None, None)
    
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
        if Util.exists_path(r, "CPU"):
            self.m_cpu = None if Util.get_by_path(r, "CPU") is None else int(str(Util.get_by_path(r, "CPU")))
        else:
            self.m_cpu = None
            self.is_incomplete = True
        self.n_cpu = False
        if Util.exists_path(r, "MemoryMB"):
            self.m_memory_mib = None if Util.get_by_path(r, "MemoryMB") is None else int(str(Util.get_by_path(r, "MemoryMB")))
        else:
            self.m_memory_mib = None
            self.is_incomplete = True
        self.n_memory_mib = False
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
        if withClean or self.n_cpu:
            Util.set_by_path(ret, "CPU", self.m_cpu)
        if withClean or self.n_memory_mib:
            Util.set_by_path(ret, "MemoryMB", self.m_memory_mib)
        if withClean or self.n_service_class:
            Util.set_by_path(ret, "ServiceClass", self.m_service_class)
        return ret
    
