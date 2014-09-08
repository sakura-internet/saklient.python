# -*- coding:utf-8 -*-

from ...util import Util

# module saklient.cloud.enums.escope

class EScope:
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
        if not (isinstance(lhs, str) and isinstance(rhs, str)): return None
        lhs = lhs.upper()
        rhs = rhs.upper()
        if lhs not in clazz._MAP or rhs not in clazz._MAP: return None
        d = clazz._MAP[lhs] - clazz._MAP[rhs]
        return (0<d) - (d<0)
    
    
