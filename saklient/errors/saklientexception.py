# -*- coding:utf-8 -*-


# module saklient.errors.saklientexception

class SaklientException(Exception):
    
    # (instance field) code
    
    # (instance field) message
    
    ## @param {str} code=None
    # @param {str} message=""
    def __init__(self, code=None, message=""):
        super(SaklientException, self).__init__(message)
        self.code = code
        self.message = message
    
