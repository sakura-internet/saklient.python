# -*- coding:utf-8 -*-

from .model import Model
from ..resource.serverplan import ServerPlan
from ...util import Util

# module saklient.cloud.model.model_serverplan

class Model_ServerPlan(Model):
    ## サーバプランを検索するための機能を備えたクラス。
    
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
    
    ## 次に取得するリストの開始オフセットを指定します。
    # 
    # @param {int} offset オフセット
    # @return {saklient.cloud.model.model_serverplan.Model_ServerPlan} this
    def offset(self, offset):
        Util.validate_type(offset, "int")
        return self._offset(offset)
    
    ## 次に取得するリストの上限レコード数を指定します。
    # 
    # @param {int} count 上限レコード数
    # @return {saklient.cloud.model.model_serverplan.Model_ServerPlan} this
    def limit(self, count):
        Util.validate_type(count, "int")
        return self._limit(count)
    
    ## Web APIのフィルタリング設定を直接指定します。
    # 
    # @param {str} key キー
    # @param {any} value 値
    # @param {bool} multiple=False valueに配列を与え、OR条件で完全一致検索する場合にtrueを指定します。通常、valueはスカラ値であいまい検索されます。
    # @return {saklient.cloud.model.model_serverplan.Model_ServerPlan}
    def filter_by(self, key, value, multiple=False):
        Util.validate_type(key, "str")
        Util.validate_type(multiple, "bool")
        return self._filter_by(key, value, multiple)
    
    ## 次のリクエストのために設定されているステートをすべて破棄します。
    # 
    # @return {saklient.cloud.model.model_serverplan.Model_ServerPlan} this
    def reset(self):
        return self._reset()
    
    ## 指定したIDを持つ唯一のリソースを取得します。
    # 
    # @param {str} id
    # @return {saklient.cloud.resource.serverplan.ServerPlan} リソースオブジェクト
    def get_by_id(self, id):
        Util.validate_type(id, "str")
        return self._get_by_id(id)
    
    ## リソースの検索リクエストを実行し、結果をリストで取得します。
    # 
    # @return {saklient.cloud.resource.serverplan.ServerPlan[]} リソースオブジェクトの配列
    def find(self):
        return self._find()
    
    ## 指定したスペックのプランを取得します。
    # 
    # @param {int} cores
    # @param {int} memoryGib
    # @return {saklient.cloud.resource.serverplan.ServerPlan}
    def get_by_spec(self, cores, memoryGib):
        Util.validate_type(cores, "int")
        Util.validate_type(memoryGib, "int")
        self._filter_by("CPU", cores, True)
        self._filter_by("MemoryMB", memoryGib * 1024, True)
        return self._find_one()
    
