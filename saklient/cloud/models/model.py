# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ..client import Client
from ..resources.resource import Resource
from .queryparams import QueryParams
from ...errors.saklientexception import SaklientException
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.models.model

class Model(object):
    ## @ignore
    
    # (instance field) _client
    
    ## @return {saklient.cloud.client.Client}
    def get_client(self):
        return self._client
    
    client = property(get_client, None, None)
    
    # (instance field) _query
    
    ## @return {saklient.cloud.models.queryparams.QueryParams}
    def get_query(self):
        return self._query
    
    query = property(get_query, None, None)
    
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
    # @return {saklient.cloud.models.model.Model} this
    def _offset(self, offset):
        Util.validate_type(offset, "int")
        self._query.begin = offset
        return self
    
    ## 次に取得するリストの上限レコード数を指定します。
    # 
    # @private
    # @param {int} count 上限レコード数
    # @return {saklient.cloud.models.model.Model} this
    def _limit(self, count):
        Util.validate_type(count, "int")
        self._query.count = count
        return self
    
    ## 次に取得するリストのソートカラムを指定します。
    # 
    # @private
    # @param {str} column カラム名
    # @param {bool} reverse=False
    # @return {saklient.cloud.models.model.Model} this
    def _sort(self, column, reverse=False):
        Util.validate_type(column, "str")
        Util.validate_type(reverse, "bool")
        op = "-" if reverse else ""
        self._query.sort.append(op + column)
        return self
    
    ## Web APIのフィルタリング設定を直接指定します。
    # 
    # @private
    # @param {str} key キー
    # @param {any} value 値
    # @param {bool} multiple=False valueに配列を与え、OR条件で完全一致検索する場合にtrueを指定します。通常、valueはスカラ値であいまい検索されます。
    # @return {saklient.cloud.models.model.Model}
    def _filter_by(self, key, value, multiple=False):
        Util.validate_type(key, "str")
        Util.validate_type(multiple, "bool")
        filter = self._query.filter
        if multiple:
            if not ( key in filter if isinstance(filter, dict) else hasattr(filter, key)):
                filter[key] = []
            values = (filter[key] if key in filter else None)
            values.append(value)
        else:
            if ( key in filter if isinstance(filter, dict) else hasattr(filter, key)):
                raise SaklientException("filter_duplicated", "The same filter key can be specified only once (by calling the same method 'withFooBar')")
            filter[key] = value
        return self
    
    ## 次のリクエストのために設定されているステートをすべて破棄します。
    # 
    # @private
    # @return {saklient.cloud.models.model.Model} this
    def _reset(self):
        self._query = QueryParams()
        self._total = 0
        self._count = 0
        return self
    
    ## @private
    # @ignore
    # @param {any} obj
    # @param {bool} wrapped=False
    # @return {saklient.cloud.resources.resource.Resource}
    def _create_resource_impl(self, obj, wrapped=False):
        Util.validate_type(wrapped, "bool")
        return None
    
    ## 新規リソース作成用のオブジェクトを用意します。
    # 
    # 返り値のオブジェクトにパラメータを設定し、save() を呼ぶことで実際のリソースが作成されます。
    # 
    # @private
    # @return {saklient.cloud.resources.resource.Resource} リソースオブジェクト
    def _create(self):
        return self._create_resource_impl(None)
    
    ## 指定したIDを持つ唯一のリソースを取得します。
    # 
    # @private
    # @param {str} id
    # @return {saklient.cloud.resources.resource.Resource} リソースオブジェクト
    def _get_by_id(self, id):
        Util.validate_type(id, "str")
        query = self._query.build()
        self._reset()
        result = self._client.request("GET", self._api_path() + "/" + Util.url_encode(id), query)
        self._total = 1
        self._count = 1
        return self._create_resource_impl(result, True)
    
    ## リソースの検索リクエストを実行し、結果をリストで取得します。
    # 
    # @private
    # @return {saklient.cloud.resources.resource.Resource[]} リソースオブジェクトの配列
    def _find(self):
        query = self._query.build()
        self._reset()
        result = self._client.request("GET", self._api_path(), query)
        self._total = (result["Total"] if "Total" in result else None)
        self._count = (result["Count"] if "Count" in result else None)
        data = []
        records = (result[self._root_key_m()] if self._root_key_m() in result else None)
        for record in records:
            data.append(self._create_resource_impl(record))
        return Client.haxe2native(data, 1)
    
    ## リソースの検索リクエストを実行し、唯一のリソースを取得します。
    # 
    # @private
    # @return {saklient.cloud.resources.resource.Resource} リソースオブジェクト
    def _find_one(self):
        query = self._query.build()
        self._reset()
        result = self._client.request("GET", self._api_path(), query)
        self._total = (result["Total"] if "Total" in result else None)
        self._count = (result["Count"] if "Count" in result else None)
        if self._total == 0:
            return None
        records = (result[self._root_key_m()] if self._root_key_m() in result else None)
        return self._create_resource_impl(records[0])
    
    ## 指定した文字列を名前に含むリソースに絞り込みます。
    # 
    # 大文字・小文字は区別されません。
    # 半角スペースで区切られた複数の文字列は、それらをすべて含むことが条件とみなされます。
    # 
    # @private
    # @todo Implement test case
    # @param {str} name
    # @return {saklient.cloud.models.model.Model}
    def _with_name_like(self, name):
        Util.validate_type(name, "str")
        return self._filter_by("Name", name)
    
    ## 指定したタグを持つリソースに絞り込みます。
    # 
    # 複数のタグを指定する場合は withTags() を利用してください。
    # 
    # @private
    # @todo Implement test case
    # @param {str} tag
    # @return {saklient.cloud.models.model.Model}
    def _with_tag(self, tag):
        Util.validate_type(tag, "str")
        return self._filter_by("Tags.Name", [tag])
    
    ## 指定したすべてのタグを持つリソースに絞り込みます。
    # 
    # @private
    # @todo Implement test case
    # @param {str[]} tags
    # @return {saklient.cloud.models.model.Model}
    def _with_tags(self, tags):
        Util.validate_type(tags, "list")
        return self._filter_by("Tags.Name", [tags])
    
    ## 指定したDNFに合致するタグを持つリソースに絞り込みます。
    # 
    # @private
    # @todo Implement test case
    # @param {str[][]} dnf
    # @return {saklient.cloud.models.model.Model}
    def _with_tag_dnf(self, dnf):
        Util.validate_type(dnf, "list")
        return self._filter_by("Tags.Name", dnf)
    
    ## 名前でソートします。
    # 
    # @private
    # @todo Implement test case
    # @param {bool} reverse=False
    # @return {saklient.cloud.models.model.Model}
    def _sort_by_name(self, reverse=False):
        Util.validate_type(reverse, "bool")
        return self._sort("Name", reverse)
    
