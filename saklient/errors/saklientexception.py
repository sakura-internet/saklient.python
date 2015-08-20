# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
import saklient

str = six.text_type
# module saklient.errors.saklientexception

class SaklientException(Exception):
    
    # (instance field) code
    
    ## @param {str} code=None
    # @param {str} message=""
    def __init__(self, code=None, message=""):
        super(SaklientException, self).__init__(message)
        self.code = code
    
