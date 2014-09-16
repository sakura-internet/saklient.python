# -*- coding:utf-8 -*-

from ...util import Util

# module saklient.cloud.models.queryparams

class QueryParams:
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
    
