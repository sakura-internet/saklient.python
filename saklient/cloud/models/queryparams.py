# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.models.queryparams

class QueryParams(object):
    ## @ignore
    
    # (instance field) begin
    
    # (instance field) count
    
    # (instance field) filter
    
    # (instance field) sort
    
    def __init__(self):
        self.begin = 0
        self.count = 0
        self.filter = {}
        self.sort = []
    
    ## @return {any}
    def build(self):
        return {
            'From': self.begin,
            'Count': self.count,
            'Filter': self.filter,
            'Sort': self.sort
        }
    
