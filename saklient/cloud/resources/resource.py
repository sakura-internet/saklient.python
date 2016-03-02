# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
from ..client import Client
from ...errors.httpexception import HttpException
import re
import saklient

str = six.text_type
# module saklient.cloud.resources.resource

class Resource(object):
    ## @ignore
    
    # (instance field) _client
    
    ## @return {saklient.cloud.client.Client}
    def get_client(self):
        return self._client
    
    ## @ignore
    client = property(get_client, None, None)
    
    # (instance field) _query
    
    ## @ignore
    # @param {str} key
    # @param {any} value
    # @return {void}
    def set_param(self, key, value):
        Util.validate_type(key, "str")
        self._query[key] = value
    
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
        self._query = {}
    
    # (instance field) is_new
    
    # (instance field) is_incomplete
    
    ## @private
    # @param {any} query
    # @return {void}
    def _on_before_save(self, query):
        {}
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_before_api_deserialize(self, r, root):
        {}
    
    ## @private
    # @param {any} r
    # @param {any} root
    # @return {void}
    def _on_after_api_deserialize(self, r, root):
        {}
    
    ## @private
    # @param {bool} withClean
    # @return {void}
    def _on_before_api_serialize(self, withClean):
        Util.validate_type(withClean, "bool")
    
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
                    root[rkey] = obj
                record = obj
            else:
                root = obj
                record = (obj[rkey] if rkey in obj else None)
        self._on_before_api_deserialize(record, root)
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
        self._on_before_api_serialize(withClean)
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
        r["ID"] = id
        return r
    
    ## @ignore
    # @param {str} name
    # @return {str}
    def normalize_field_name(self, name):
        Util.validate_type(name, "str")
        name = re.sub('[A-Z]', lambda m: '_'+m.group(0).lower(), name)
        return name
    
    ## このローカルオブジェクトに現在設定されているリソース情報をAPIに送信し、新規作成または上書き保存します。
    # 
    # @private
    # @return {saklient.cloud.resources.resource.Resource} this
    def _save(self):
        r = self.api_serialize()
        query = self._query
        self._query = {}
        keys = query.keys()
        for k in keys:
            v = (query[k] if k in query else None)
            r[k] = v
        method = "POST" if self.is_new else "PUT"
        path = self._api_path()
        if not self.is_new:
            path += "/" + Util.url_encode(self._id())
        q = {}
        q[self._root_key()] = r
        self._on_before_save(q)
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
        self.request_retry("DELETE", path)
    
    ## 最新のリソース情報を再取得します。
    # 
    # @private
    # @return {saklient.cloud.resources.resource.Resource} this
    def _reload(self):
        id = self._id()
        if id is not None:
            result = self.request_retry("GET", self._api_path() + "/" + Util.url_encode(id))
            self.api_deserialize(result, True)
        return self
    
    ## このリソースが存在するかを調べます。
    # 
    # @return {bool}
    def exists(self):
        query = {}
        Util.set_by_path(query, "Filter.ID", [self._id()])
        Util.set_by_path(query, "Include", ["ID"])
        result = self.request_retry("GET", self._api_path(), query)
        cnt = (result["Count"] if "Count" in result else None)
        return cnt == 1
    
    ## @ignore
    # @return {any}
    def dump(self):
        return self.api_serialize(True)
    
    ## @ignore
    # @static
    # @param {str} className
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    # @return {saklient.cloud.resources.resource.Resource}
    @staticmethod
    def create_with(className, client, obj, wrapped=False):
        Util.validate_type(className, "str")
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        a = [client, obj, wrapped]
        return Util.create_class_instance("saklient.cloud.resources." + className, a)
    
    ## @param {str} method
    # @param {str} path
    # @param {any} query=None
    # @param {int} retryCount=5
    # @param {int} retrySleep=5
    # @return {any}
    def request_retry(self, method, path, query=None, retryCount=5, retrySleep=5):
        Util.validate_type(method, "str")
        Util.validate_type(path, "str")
        Util.validate_type(retryCount, "int")
        Util.validate_type(retrySleep, "int")
        ret = None
        while (1 < retryCount):
            isOk = False
            try:
                ret = self._client.request(method, path, query)
                isOk = True
            except saklient.errors.httpexception.HttpException:
                isOk = False
            if isOk:
                retryCount = -1
            else:
                retryCount -= 1
                Util.sleep(retrySleep)
        if retryCount == 0:
            ret = self._client.request(method, path, query)
        return ret
    
