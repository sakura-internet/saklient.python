# -*- coding:utf-8 -*-

from ..client import Client
from ..resource.resource import Resource
from ...util import Util

# module saklient.cloud.model.model

class Model:
    ## @ignore
    
    # (instance field) _client
    
    ## @return {saklient.cloud.client.Client}
    def get_client(self):
        return self._client
    
    client = property(get_client, None, None)
    
    # (instance field) _params
    
    ## @return {TQueryParams}
    def get_params(self):
        return self._params
    
    params = property(get_params, None, None)
    
    # (instance field) _total
    
    ## @return {int}
    def get_total(self):
        return self._total
    
    total = property(get_total, None, None)
    
    # (instance field) _count
    
    ## @return {int}
    def get_count(self):
        return self._count
    
    count = property(get_count, None, None)
    
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
    
    ## @param {saklient.cloud.client.Client} client
    def __init__(self, client):
        Util.validate_type(client, "saklient.cloud.client.Client")
        self._client = client
        self._reset()
    
    ## 次に取得するリストの開始オフセットを指定します。
    # 
    # @private
    # @param {int} offset オフセット
    # @return {saklient.cloud.model.model.Model} this
    def _offset(self, offset):
        Util.validate_type(offset, "int")
        if isinstance(self._params, dict):
            self._params["Begin"] = offset
        else:
            setattr(self._params, "Begin", offset)
        return self
    
    ## 次に取得するリストの上限レコード数を指定します。
    # 
    # @private
    # @param {int} count 上限レコード数
    # @return {saklient.cloud.model.model.Model} this
    def _limit(self, count):
        Util.validate_type(count, "int")
        if isinstance(self._params, dict):
            self._params["Count"] = count
        else:
            setattr(self._params, "Count", count)
        return self
    
    ## 次に取得するリストのソートカラムを指定します。
    # 
    # @private
    # @param {str} column カラム名
    # @param {bool} reverse=False
    # @return {saklient.cloud.model.model.Model} this
    def _sort(self, column, reverse=False):
        Util.validate_type(column, "str")
        Util.validate_type(reverse, "bool")
        if not ( "Sort" in self._params if isinstance(self._params, dict) else hasattr(self._params, "Sort")):
            if isinstance(self._params, dict):
                self._params["Sort"] = []
            else:
                setattr(self._params, "Sort", [])
        sort = ( (self._params["Sort"] if "Sort" in self._params else None ) if isinstance(self._params, dict) else getattr(self._params, "Sort"))
        op = "-" if reverse else ""
        sort.append(op + column)
        return self
    
    ## Web APIのフィルタリング設定を直接指定します。
    # 
    # @private
    # @param {str} key キー
    # @param {any} value 値
    # @param {bool} multiple=False valueに配列を与え、OR条件で完全一致検索する場合にtrueを指定します。通常、valueはスカラ値であいまい検索されます。
    # @return {saklient.cloud.model.model.Model}
    def _filter_by(self, key, value, multiple=False):
        Util.validate_type(key, "str")
        Util.validate_type(multiple, "bool")
        if not ( "Filter" in self._params if isinstance(self._params, dict) else hasattr(self._params, "Filter")):
            if isinstance(self._params, dict):
                self._params["Filter"] = {}
            else:
                setattr(self._params, "Filter", {})
        filter = ( (self._params["Filter"] if "Filter" in self._params else None ) if isinstance(self._params, dict) else getattr(self._params, "Filter"))
        if multiple:
            if not ( key in filter if isinstance(filter, dict) else hasattr(filter, key)):
                if isinstance(filter, dict):
                    filter[key] = []
                else:
                    setattr(filter, key, [])
            values = ( (filter[key] if key in filter else None ) if isinstance(filter, dict) else getattr(filter, key))
            values.append(value)
        else:
            if isinstance(filter, dict):
                filter[key] = value
            else:
                setattr(filter, key, value)
        return self
    
    ## 次のリクエストのために設定されているステートをすべて破棄します。
    # 
    # @private
    # @return {saklient.cloud.model.model.Model} this
    def _reset(self):
        self._params = {
            'Count': 0
        }
        self._total = 0
        self._count = 0
        return self
    
    ## 新規リソース作成用のオブジェクトを用意します。
    # 
    # 返り値のオブジェクトにパラメータを設定し、save() を呼ぶことで実際のリソースが作成されます。
    # 
    # @private
    # @return {saklient.cloud.resource.resource.Resource} リソースオブジェクト
    def _create(self):
        return Util.create_class_instance("saklient.cloud.resource." + self._class_name(), [self._client, None])
    
    ## 指定したIDを持つ唯一のリソースを取得します。
    # 
    # @private
    # @param {str} id
    # @return {saklient.cloud.resource.resource.Resource} リソースオブジェクト
    def _get_by_id(self, id):
        Util.validate_type(id, "str")
        params = self._params
        self._reset()
        result = self._client.request("GET", self._api_path() + "/" + Util.url_encode(id), params)
        self._total = 1
        self._count = 1
        return Util.create_class_instance("saklient.cloud.resource." + self._class_name(), [self._client, result, True])
    
    ## リソースの検索リクエストを実行し、結果をリストで取得します。
    # 
    # @private
    # @return {saklient.cloud.resource.resource.Resource[]} リソースオブジェクトの配列
    def _find(self):
        params = self._params
        self._reset()
        result = self._client.request("GET", self._api_path(), params)
        self._total = ( (result["Total"] if "Total" in result else None ) if isinstance(result, dict) else getattr(result, "Total"))
        self._count = ( (result["Count"] if "Count" in result else None ) if isinstance(result, dict) else getattr(result, "Count"))
        records = ( (result[self._root_key_m()] if self._root_key_m() in result else None ) if isinstance(result, dict) else getattr(result, self._root_key_m()))
        data = []
        for record in records:
            i = Util.create_class_instance("saklient.cloud.resource." + self._class_name(), [self._client, record])
            data.append(i)
        return Client.haxe2native(data, 1)
    
    ## リソースの検索リクエストを実行し、唯一のリソースを取得します。
    # 
    # @private
    # @return {saklient.cloud.resource.resource.Resource} リソースオブジェクト
    def _find_one(self):
        params = self._params
        self._reset()
        result = self._client.request("GET", self._api_path(), params)
        self._total = ( (result["Total"] if "Total" in result else None ) if isinstance(result, dict) else getattr(result, "Total"))
        self._count = ( (result["Count"] if "Count" in result else None ) if isinstance(result, dict) else getattr(result, "Count"))
        if self._total == 0:
            return None
        records = ( (result[self._root_key_m()] if self._root_key_m() in result else None ) if isinstance(result, dict) else getattr(result, self._root_key_m()))
        return Util.create_class_instance("saklient.cloud.resource." + self._class_name(), [self._client, records[0]])
    
    ## 指定した文字列を名前に含むリソースに絞り込みます。
    # 
    # 大文字・小文字は区別されません。
    # 半角スペースで区切られた複数の文字列は、それらをすべて含むことが条件とみなされます。
    # 
    # @private
    # @param {str} name
    # @return {saklient.cloud.model.model.Model}
    def _with_name_like(self, name):
        Util.validate_type(name, "str")
        return self._filter_by("Name", name)
    
    ## 指定したタグを持つリソースに絞り込みます。
    # 
    # 複数のタグを指定する場合は withTags() を利用してください。
    # 
    # @private
    # @param {str} tag
    # @return {saklient.cloud.model.model.Model}
    def _with_tag(self, tag):
        Util.validate_type(tag, "str")
        return self._filter_by("Tags.Name", tag, True)
    
    ## 指定したすべてのタグを持つリソースに絞り込みます。
    # 
    # @private
    # @param {str[]} tags
    # @return {saklient.cloud.model.model.Model}
    def _with_tags(self, tags):
        Util.validate_type(tags, "list")
        return self._filter_by("Tags.Name", tags, True)
    
    ## 名前でソートします。
    # 
    # @private
    # @param {bool} reverse=False
    # @return {saklient.cloud.model.model.Model}
    def _sort_by_name(self, reverse=False):
        Util.validate_type(reverse, "bool")
        return self._sort("Name", reverse)
    
