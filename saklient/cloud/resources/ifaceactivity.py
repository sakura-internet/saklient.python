# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

from .activity import Activity
from .ifaceactivitysample import IfaceActivitySample
from ...util import Util
import saklient

# module saklient.cloud.resources.ifaceactivity

class IfaceActivity(Activity):
    
    # (instance field) _samples
    
    ## @return {saklient.cloud.resources.ifaceactivitysample.IfaceActivitySample[]}
    def get_samples(self):
        return self._samples
    
    ## サンプル列
    samples = property(get_samples, None, None)
    
    ## @private
    # @return {str}
    def _api_path_prefix(self):
        return "/interface"
    
    ## @private
    # @return {str}
    def _api_path_suffix(self):
        return "/monitor"
    
    ## @private
    # @param {str} atStr
    # @param {any} data
    # @return {void}
    def _add_sample(self, atStr, data):
        Util.validate_type(atStr, "str")
        self._samples.append(IfaceActivitySample(atStr, data))
    
    ## 現在の最新のアクティビティ情報を取得し、samplesに格納します。
    #  
    #  	 * @return this
    # 
    # @param {NativeDate} startDate=None
    # @param {NativeDate} endDate=None
    # @return {saklient.cloud.resources.ifaceactivity.IfaceActivity}
    def fetch(self, startDate=None, endDate=None):
        Util.validate_type(startDate, "NativeDate")
        Util.validate_type(endDate, "NativeDate")
        self._samples = []
        return self._fetch(startDate, endDate)
    
