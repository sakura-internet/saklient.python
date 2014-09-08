# -*- coding:utf-8 -*-

from ...util import Util
from ..client import Client
import re

# module saklient.cloud.resource.resource

class Resource:
    ## @ignore
    
    # (instance field) _client
    
    ## @return {saklient.cloud.client.Client}
    def get_client(self):
        return self._client
    
    ## @ignore
    client = property(get_client, None, None)
    
    # (instance field) _params
    
    ## @ignore
    # @param {str} key
    # @param {any} value
    # @return {void}
    def set_param(self, key, value):
        Util.validate_type(key, "str")
        if isinstance(self._params, dict):
            self._params[key] = value
        else:
            setattr(self._params, key, value)
    
    ## @private
    # @return {str}
    def _api_path(self):
        return None
    
    ## @private
    # @return {str}
    def _root_key(self):
        return None
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return None
    
    ## @private
    # @return {str}
    def _class_name(self):
        return None
    
    ## @private
    # @return {str}
    def _id(self):
        return None
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    def __init__(self, client):
        Util.validate_type(client, "saklient.cloud.client.Client")
        self._client = client
        self._params = {}
    
    # (instance field) is_new
    
    # (instance field) is_incomplete
    
    ## @private
    # @param {any} r
    # @return {void}
    def _on_before_save(self, r):
        {}
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_after_api_deserialize(self, r, root):
        {}
    
    ## @private
    # @param {any} r
    # @param {bool} withClean
    # @return {void}
    def _on_after_api_serialize(self, r, withClean):
        Util.validate_type(withClean, "bool")
    
    ## @ignore
    # @param {any} r
    # @return {void}
    def api_deserialize_impl(self, r):
        {}
    
    ## @ignore
    # @param {any} obj
    # @param {bool} wrapped=False
    # @return {void}
    def api_deserialize(self, obj, wrapped=False):
        Util.validate_type(wrapped, "bool")
        root = None
        record = None
        rkey = self._root_key()
        if obj is not None:
            if not wrapped:
                if rkey is not None:
                    root = {}
                    if isinstance(root, dict):
                        root[rkey] = obj
                    else:
                        setattr(root, rkey, obj)
                record = obj
            else:
                root = obj
                record = ( (obj[rkey] if rkey in obj else None ) if isinstance(obj, dict) else getattr(obj, rkey))
        self.api_deserialize_impl(record)
        self._on_after_api_deserialize(record, root)
    
    ## @ignore
    # @param {bool} withClean=False
    # @return {any}
    def api_serialize_impl(self, withClean=False):
        Util.validate_type(withClean, "bool")
        return None
    
    ## @ignore
    # @param {bool} withClean=False
    # @return {any}
    def api_serialize(self, withClean=False):
        Util.validate_type(withClean, "bool")
        ret = self.api_serialize_impl(withClean)
        self._on_after_api_serialize(ret, withClean)
        return ret
    
    ## @ignore
    # @return {any}
    def api_serialize_id(self):
        id = self._id()
        if id is None:
            return None
        r = {}
        if isinstance(r, dict):
            r["ID"] = id
        else:
            setattr(r, "ID", id)
        return r
    
    ## @ignore
    # @param {str} name
    # @return {str}
    def normalize_field_name(self, name):
        Util.validate_type(name, "str")
        name = re.sub('[A-Z]', lambda m: '_'+m.group(0).lower(), name)
        return name
    
    ## @ignore
    # @param {str} name
    # @param {any} value
    # @return {void}
    def set_property(self, name, value):
        Util.validate_type(name, "str")
        name = self.normalize_field_name(name)
        if isinstance(self, dict):
            self["m_" + name] = value
        else:
            setattr(self, "m_" + name, value)
        if isinstance(self, dict):
            self["n_" + name] = True
        else:
            setattr(self, "n_" + name, True)
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @private
    # @return {saklient.cloud.resource.resource.Resource} this
    def _save(self):
        r = self.api_serialize()
        params = self._params
        self._params = {}
        keys = params.keys()
        for k in keys:
            v = ( (params[k] if k in params else None ) if isinstance(params, dict) else getattr(params, k))
            if isinstance(r, dict):
                r[k] = v
            else:
                setattr(r, k, v)
        self._on_before_save(r)
        method = "POST" if self.is_new else "PUT"
        path = self._api_path()
        if not self.is_new:
            path += "/" + Util.url_encode(self._id())
        q = {}
        if isinstance(q, dict):
            q[self._root_key()] = r
        else:
            setattr(q, self._root_key(), r)
        result = self._client.request(method, path, q)
        self.api_deserialize(result, True)
        return self
    
    ## このローカルオブジェクトのIDと一致するリソースの削除リクエストをAPIに送信します。
    # 
    # @return {void}
    def destroy(self):
        if self.is_new:
            return
        path = self._api_path() + "/" + Util.url_encode(self._id())
        self._client.request("DELETE", path)
    
    ## 最新のリソース情報を再取得します。
    # 
    # @private
    # @return {saklient.cloud.resource.resource.Resource} this
    def _reload(self):
        result = self._client.request("GET", self._api_path() + "/" + Util.url_encode(self._id()))
        self.api_deserialize(result, True)
        return self
    
    ## このリソースが存在するかを調べます。
    # 
    # @return {bool}
    def exists(self):
        params = {}
        Util.set_by_path(params, "Filter.ID", [self._id()])
        Util.set_by_path(params, "Include", ["ID"])
        result = self._client.request("GET", self._api_path(), params)
        return ( (result["Count"] if "Count" in result else None ) if isinstance(result, dict) else getattr(result, "Count")) == 1
    
    ## @ignore
    # @return {any}
    def dump(self):
        return self.api_serialize(True)
    
