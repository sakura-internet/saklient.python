# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

from .activity import Activity
from .serveractivitysample import ServerActivitySample
from ...util import Util
import saklient

# module saklient.cloud.resources.serveractivity

class ServerActivity(Activity):
    
    # (instance field) _samples
    
    ## @return {saklient.cloud.resources.serveractivitysample.ServerActivitySample[]}
    def get_samples(self):
        return self._samples
    
    ## サンプル列
    samples = property(get_samples, None, None)
    
    ## @private
    # @return {str}
    def _api_path_prefix(self):
        return "/server"
    
    ## @private
    # @param {str} atStr
    # @param {any} data
    # @return {void}
    def _add_sample(self, atStr, data):
        Util.validate_type(atStr, "str")
        self._samples.append(ServerActivitySample(atStr, data))
    
    ## 現在の最新のアクティビティ情報を取得し、samplesに格納します。
    #  
    #  	 * @return this
    # 
    # @param {NativeDate} startDate=None
    # @param {NativeDate} endDate=None
    # @return {saklient.cloud.resources.serveractivity.ServerActivity}
    def fetch(self, startDate=None, endDate=None):
        Util.validate_type(startDate, "NativeDate")
        Util.validate_type(endDate, "NativeDate")
        self._samples = []
        return self._fetch(startDate, endDate)
    
