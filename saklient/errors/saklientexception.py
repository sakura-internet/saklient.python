# -*- coding:utf-8 -*-

import saklient

# module saklient.errors.saklientexception

class SaklientException(Exception):
    
    # (instance field) code
    
    ## @param {str} code=None
    # @param {str} message=""
    def __init__(self, code=None, message=""):
        super(SaklientException, self).__init__(message)
        self.code = code
    
