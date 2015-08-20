# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.enums.escope

class EScope(object):
    ## リソースの公開範囲を表す列挙子。
    
    USER = "user"
    user = "user"
    
    SHARED = "shared"
    shared = "shared"
    
    ## @ignore
    _MAP = {
        "USER": 100,
        "SHARED": 200
    }
    
    ## @ignore
    @classmethod
    def compare(clazz, lhs, rhs):
        if not (isinstance(lhs, (six.text_type, six.string_types)) and isinstance(rhs, (six.text_type, six.string_types))): return None
        lhs = lhs.upper()
        rhs = rhs.upper()
        if lhs not in clazz._MAP or rhs not in clazz._MAP: return None
        d = clazz._MAP[lhs] - clazz._MAP[rhs]
        return (0<d) - (d<0)
    
    
