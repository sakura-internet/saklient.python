# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ..client import Client
from .model import Model
from ..resources.resource import Resource
from ..resources.commonserviceitem import CommonServiceItem
from ..resources.gslb import Gslb
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.models.model_commonserviceitem

class Model_CommonServiceItem(Model):
    ## 共通サービス契約を検索・作成するための機能を備えたクラス。
    
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
    # @param {any} obj
    # @param {bool} wrapped=False
    # @return {saklient.cloud.resources.resource.Resource}
    def _create_resource_impl(self, obj, wrapped=False):
        Util.validate_type(wrapped, "bool")
        clazz = Util.get_by_path(obj, "CommonServiceItem.Provider.Class")
        if clazz == "gslb":
            return Gslb(self._client, obj, wrapped)
        return CommonServiceItem(self._client, obj, wrapped)
    
    ## 次に取得するリストの開始オフセットを指定します。
    # 
    # @param {int} offset オフセット
    # @return {saklient.cloud.models.model_commonserviceitem.Model_CommonServiceItem} this
    def offset(self, offset):
        Util.validate_type(offset, "int")
        return self._offset(offset)
    
    ## 次に取得するリストの上限レコード数を指定します。
    # 
    # @param {int} count 上限レコード数
    # @return {saklient.cloud.models.model_commonserviceitem.Model_CommonServiceItem} this
    def limit(self, count):
        Util.validate_type(count, "int")
        return self._limit(count)
    
    ## Web APIのフィルタリング設定を直接指定します。
    # 
    # @param {str} key キー
    # @param {any} value 値
    # @param {bool} multiple=False valueに配列を与え、OR条件で完全一致検索する場合にtrueを指定します。通常、valueはスカラ値であいまい検索されます。
    # @return {saklient.cloud.models.model_commonserviceitem.Model_CommonServiceItem}
    def filter_by(self, key, value, multiple=False):
        Util.validate_type(key, "str")
        Util.validate_type(multiple, "bool")
        return self._filter_by(key, value, multiple)
    
    ## 次のリクエストのために設定されているステートをすべて破棄します。
    # 
    # @return {saklient.cloud.models.model_commonserviceitem.Model_CommonServiceItem} this
    def reset(self):
        return self._reset()
    
    ## @param {str} protocol
    # @param {int} delayLoop=10
    # @param {bool} weighted=True
    # @return {saklient.cloud.resources.gslb.Gslb}
    def create_gslb(self, protocol, delayLoop=10, weighted=True):
        Util.validate_type(protocol, "str")
        Util.validate_type(delayLoop, "int")
        Util.validate_type(weighted, "bool")
        ret = Gslb(self._client, None)
        ret.set_initial_params(protocol, delayLoop, weighted)
        return ret
    
    ## 指定したIDを持つ唯一のリソースを取得します。
    # 
    # @param {str} id
    # @return {saklient.cloud.resources.commonserviceitem.CommonServiceItem} リソースオブジェクト
    def get_by_id(self, id):
        Util.validate_type(id, "str")
        return self._get_by_id(id)
    
    ## リソースの検索リクエストを実行し、結果をリストで取得します。
    # 
    # @return {saklient.cloud.resources.commonserviceitem.CommonServiceItem[]} リソースオブジェクトの配列
    def find(self):
        return self._find()
    
    ## 指定した文字列を名前に含むリソースに絞り込みます。
    # 
    # 大文字・小文字は区別されません。
    # 半角スペースで区切られた複数の文字列は、それらをすべて含むことが条件とみなされます。
    # 
    # @todo Implement test case
    # @param {str} name
    # @return {saklient.cloud.models.model_commonserviceitem.Model_CommonServiceItem}
    def with_name_like(self, name):
        Util.validate_type(name, "str")
        return self._with_name_like(name)
    
    ## 名前でソートします。
    # 
    # @todo Implement test case
    # @param {bool} reverse=False
    # @return {saklient.cloud.models.model_commonserviceitem.Model_CommonServiceItem}
    def sort_by_name(self, reverse=False):
        Util.validate_type(reverse, "bool")
        return self._sort_by_name(reverse)
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    def __init__(self, client):
        super(Model_CommonServiceItem, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
    
