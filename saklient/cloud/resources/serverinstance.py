# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
from ..client import Client
from .resource import Resource
from .isoimage import IsoImage
from ..enums.eserverinstancestatus import EServerInstanceStatus
import saklient

str = six.text_type
# module saklient.cloud.resources.serverinstance

class ServerInstance(Resource):
    ## サーバインスタンスの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_status
    
    # (instance field) m_before_status
    
    # (instance field) m_status_changed_at
    
    # (instance field) m_iso_image
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(ServerInstance, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self.api_deserialize(obj, wrapped)
    
    ## サーバが起動しているときtrueを返します。
    # 
    # @return {bool}
    def is_up(self):
        return self.get_status() is not None and EServerInstanceStatus.compare(self.get_status(), EServerInstanceStatus.up) == 0
    
    ## サーバが停止しているときtrueを返します。
    # 
    # @return {bool}
    def is_down(self):
        return self.get_status() is None or EServerInstanceStatus.compare(self.get_status(), EServerInstanceStatus.down) == 0
    
    # (instance field) n_status = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_status(self):
        return self.m_status
    
    ## 起動状態 {@link EServerInstanceStatus}
    status = property(get_status, None, None)
    
    # (instance field) n_before_status = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_before_status(self):
        return self.m_before_status
    
    ## 前回の起動状態 {@link EServerInstanceStatus}
    before_status = property(get_before_status, None, None)
    
    # (instance field) n_status_changed_at = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {NativeDate}
    def get_status_changed_at(self):
        return self.m_status_changed_at
    
    ## 現在の起動状態に変化した日時
    status_changed_at = property(get_status_changed_at, None, None)
    
    # (instance field) n_iso_image = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {saklient.cloud.resources.isoimage.IsoImage}
    def get_iso_image(self):
        return self.m_iso_image
    
    ## 挿入されているISOイメージ
    iso_image = property(get_iso_image, None, None)
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {any} r
    def api_deserialize_impl(self, r):
        self.is_new = r is None
        if self.is_new:
            r = {
                
            }
        self.is_incomplete = False
        if Util.exists_path(r, "Status"):
            self.m_status = None if Util.get_by_path(r, "Status") is None else str(Util.get_by_path(r, "Status"))
        else:
            self.m_status = None
            self.is_incomplete = True
        self.n_status = False
        if Util.exists_path(r, "BeforeStatus"):
            self.m_before_status = None if Util.get_by_path(r, "BeforeStatus") is None else str(Util.get_by_path(r, "BeforeStatus"))
        else:
            self.m_before_status = None
            self.is_incomplete = True
        self.n_before_status = False
        if Util.exists_path(r, "StatusChangedAt"):
            self.m_status_changed_at = None if Util.get_by_path(r, "StatusChangedAt") is None else Util.str2date(str(Util.get_by_path(r, "StatusChangedAt")))
        else:
            self.m_status_changed_at = None
            self.is_incomplete = True
        self.n_status_changed_at = False
        if Util.exists_path(r, "CDROM"):
            self.m_iso_image = None if Util.get_by_path(r, "CDROM") is None else IsoImage(self._client, Util.get_by_path(r, "CDROM"))
        else:
            self.m_iso_image = None
            self.is_incomplete = True
        self.n_iso_image = False
    
    ## @ignore
    # @param {bool} withClean=False
    # @return {any}
    def api_serialize_impl(self, withClean=False):
        Util.validate_type(withClean, "bool")
        ret = {
            
        }
        if withClean or self.n_status:
            Util.set_by_path(ret, "Status", self.m_status)
        if withClean or self.n_before_status:
            Util.set_by_path(ret, "BeforeStatus", self.m_before_status)
        if withClean or self.n_status_changed_at:
            Util.set_by_path(ret, "StatusChangedAt", None if self.m_status_changed_at is None else Util.date2str(self.m_status_changed_at))
        if withClean or self.n_iso_image:
            Util.set_by_path(ret, "CDROM", (None if self.m_iso_image is None else self.m_iso_image.api_serialize(withClean)) if withClean else ({
                'ID': "0"
            } if self.m_iso_image is None else self.m_iso_image.api_serialize_id()))
        return ret
    
