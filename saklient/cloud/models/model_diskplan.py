# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ..client import Client
from .model import Model
from ..resources.resource import Resource
from ..resources.diskplan import DiskPlan
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.models.model_diskplan

class Model_DiskPlan(Model):
    ## ディスクプランを検索するための機能を備えたクラス。
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/product/disk"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "DiskPlan"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "DiskPlans"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "DiskPlan"
    
    ## @private
    # @param {any} obj
    # @param {bool} wrapped=False
    # @return {saklient.cloud.resources.resource.Resource}
    def _create_resource_impl(self, obj, wrapped=False):
        Util.validate_type(wrapped, "bool")
        return DiskPlan(self._client, obj, wrapped)
    
    ## 次に取得するリストの開始オフセットを指定します。
    # 
    # @param {int} offset オフセット
    # @return {saklient.cloud.models.model_diskplan.Model_DiskPlan} this
    def offset(self, offset):
        Util.validate_type(offset, "int")
        return self._offset(offset)
    
    ## 次に取得するリストの上限レコード数を指定します。
    # 
    # @param {int} count 上限レコード数
    # @return {saklient.cloud.models.model_diskplan.Model_DiskPlan} this
    def limit(self, count):
        Util.validate_type(count, "int")
        return self._limit(count)
    
    ## Web APIのフィルタリング設定を直接指定します。
    # 
    # @param {str} key キー
    # @param {any} value 値
    # @param {bool} multiple=False valueに配列を与え、OR条件で完全一致検索する場合にtrueを指定します。通常、valueはスカラ値であいまい検索されます。
    # @return {saklient.cloud.models.model_diskplan.Model_DiskPlan}
    def filter_by(self, key, value, multiple=False):
        Util.validate_type(key, "str")
        Util.validate_type(multiple, "bool")
        return self._filter_by(key, value, multiple)
    
    ## 次のリクエストのために設定されているステートをすべて破棄します。
    # 
    # @return {saklient.cloud.models.model_diskplan.Model_DiskPlan} this
    def reset(self):
        return self._reset()
    
    ## 指定したIDを持つ唯一のリソースを取得します。
    # 
    # @param {str} id
    # @return {saklient.cloud.resources.diskplan.DiskPlan} リソースオブジェクト
    def get_by_id(self, id):
        Util.validate_type(id, "str")
        return self._get_by_id(id)
    
    ## リソースの検索リクエストを実行し、結果をリストで取得します。
    # 
    # @return {saklient.cloud.resources.diskplan.DiskPlan[]} リソースオブジェクトの配列
    def find(self):
        return self._find()
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    def __init__(self, client):
        super(Model_DiskPlan, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        self._hdd = None
        self._ssd = None
    
    # (instance field) _hdd
    
    ## @return {saklient.cloud.resources.diskplan.DiskPlan}
    def get_hdd(self):
        if self._hdd is None:
            self._hdd = self.get_by_id("2")
        return self._hdd
    
    ## 標準プラン
    hdd = property(get_hdd, None, None)
    
    # (instance field) _ssd
    
    ## @return {saklient.cloud.resources.diskplan.DiskPlan}
    def get_ssd(self):
        if self._ssd is None:
            self._ssd = self.get_by_id("4")
        return self._ssd
    
    ## SSDプラン
    ssd = property(get_ssd, None, None)
    
