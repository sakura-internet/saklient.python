# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
from ..client import Client
import saklient

str = six.text_type
# module saklient.cloud.resources.activity

class Activity(object):
    
    # (instance field) _client
    
    # (instance field) _source_id
    
    ## @private
    # @return {str}
    def _api_path_prefix(self):
        return None
    
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
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    def __init__(self, client):
        Util.validate_type(client, "saklient.cloud.client.Client")
        self._client = client
    
    ## @ignore
    # @param {str} id
    # @return {void}
    def set_source_id(self, id):
        Util.validate_type(id, "str")
        self._source_id = id
    
    ## 現在の最新のアクティビティ情報を取得し、samplesに格納します。
    #  
    #  	 * @return this
    # 
    # @private
    # @param {NativeDate} startDate=None
    # @param {NativeDate} endDate=None
    # @return {saklient.cloud.resources.activity.Activity}
    def _fetch(self, startDate=None, endDate=None):
        Util.validate_type(startDate, "NativeDate")
        Util.validate_type(endDate, "NativeDate")
        query = {}
        if startDate is not None:
            query["Start"] = Util.date2str(startDate)
        if endDate is not None:
            query["End"] = Util.date2str(endDate)
        path = self._api_path_prefix() + "/" + Util.url_encode(self._source_id) + self._api_path_suffix()
        data = self._client.request("GET", path)
        if data is None:
            return None
        data = (data["Data"] if "Data" in data else None)
        if data is None:
            return None
        dates = data.keys()
        dates = Util.sort_array(dates)
        for date in dates:
            self._add_sample(date, (data[date] if date in data else None))
        return self
    
