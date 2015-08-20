# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ..client import Client
from .resource import Resource
from .icon import Icon
from .ftpinfo import FtpInfo
from ..enums.escope import EScope
from ...errors.saklientexception import SaklientException
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.isoimage

class IsoImage(Resource):
    ## ISOイメージの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    # (instance field) m_id
    
    # (instance field) m_scope
    
    # (instance field) m_name
    
    # (instance field) m_description
    
    # (instance field) m_tags
    
    # (instance field) m_icon
    
    # (instance field) m_display_order
    
    # (instance field) m_size_mib
    
    # (instance field) m_service_class
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/cdrom"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "CDROM"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "CDROMs"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "IsoImage"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @return {saklient.cloud.resources.isoimage.IsoImage} this
    def save(self):
        return self._save()
    
    ## 最新のリソース情報を再取得します。
    # 
    # @return {saklient.cloud.resources.isoimage.IsoImage} this
    def reload(self):
        return self._reload()
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(IsoImage, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self.api_deserialize(obj, wrapped)
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_after_api_deserialize(self, r, root):
        if root is None:
            return
        if ( "FTPServer" in root if isinstance(root, dict) else hasattr(root, "FTPServer")):
            ftp = (root["FTPServer"] if "FTPServer" in root else None)
            if ftp is not None:
                self._ftp_info = FtpInfo(ftp)
    
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
    
    # (instance field) _ftp_info
    
    ## @return {saklient.cloud.resources.ftpinfo.FtpInfo}
    def get_ftp_info(self):
        return self._ftp_info
    
    ## FTP情報
    ftp_info = property(get_ftp_info, None, None)
    
    ## FTPSを開始し、イメージファイルをアップロード・ダウンロードできる状態にします。
    # 
    # アカウント情報は、ftpInfo プロパティから取得することができます。
    # 
    # @param {bool} reset=False 既にFTPSが開始されているとき、trueを指定してこのメソッドを呼ぶことでパスワードを再設定します。
    # @return {saklient.cloud.resources.isoimage.IsoImage} this
    def open_ftp(self, reset=False):
        Util.validate_type(reset, "bool")
        path = self._api_path() + "/" + Util.url_encode(self._id()) + "/ftp"
        q = {}
        Util.set_by_path(q, "ChangePassword", reset)
        result = self._client.request("PUT", path, q)
        self._on_after_api_deserialize(None, result)
        return self
    
    ## FTPSを終了し、ISOイメージを利用可能な状態にします。
    # 
    # @return {saklient.cloud.resources.isoimage.IsoImage} this
    def close_ftp(self):
        path = self._api_path() + "/" + Util.url_encode(self._id()) + "/ftp"
        self._client.request("DELETE", path)
        self._ftp_info = None
        return self
    
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
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {str} v
    # @return {str}
    def set_scope(self, v):
        Util.validate_type(v, "str")
        self.m_scope = v
        self.n_scope = True
        return self.m_scope
    
    ## スコープ {@link EScope}
    scope = property(get_scope, set_scope, None)
    
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
    
    # (instance field) n_display_order = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {int}
    def get_display_order(self):
        return self.m_display_order
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {int} v
    # @return {int}
    def set_display_order(self, v):
        Util.validate_type(v, "int")
        self.m_display_order = v
        self.n_display_order = True
        return self.m_display_order
    
    ## 表示順序
    display_order = property(get_display_order, set_display_order, None)
    
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
            raise SaklientException("immutable_field", "Immutable fields cannot be modified after the resource creation: " + "saklient.cloud.resources.isoimage.IsoImage#size_mib")
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
        if Util.exists_path(r, "DisplayOrder"):
            self.m_display_order = None if Util.get_by_path(r, "DisplayOrder") is None else int(str(Util.get_by_path(r, "DisplayOrder")))
        else:
            self.m_display_order = None
            self.is_incomplete = True
        self.n_display_order = False
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
        if withClean or self.n_display_order:
            Util.set_by_path(ret, "DisplayOrder", self.m_display_order)
        if withClean or self.n_size_mib:
            Util.set_by_path(ret, "SizeMB", self.m_size_mib)
        else:
            if self.is_new:
                missing.append("size_mib")
        if withClean or self.n_service_class:
            Util.set_by_path(ret, "ServiceClass", self.m_service_class)
        if len(missing) > 0:
            raise SaklientException("required_field", "Required fields must be set before the IsoImage creation: " + ", ".join(missing))
        return ret
    
