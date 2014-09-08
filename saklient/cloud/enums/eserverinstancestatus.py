# -*- coding:utf-8 -*-

from ...util import Util

# module saklient.cloud.enums.eserverinstancestatus

class EServerInstanceStatus:
    ## サーバの起動状態を表す列挙子。
    
    DOWN = "down"
    down = "down"
    
    CLEANING = "cleaning"
    cleaning = "cleaning"
    
    UP = "up"
    up = "up"
    
    ## @ignore
    _MAP = {
        "DOWN": 0,
        "CLEANING": 5,
        "UP": 100
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
    
    
