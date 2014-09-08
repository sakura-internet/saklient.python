# -*- coding:utf-8 -*-

from ...util import Util

# module saklient.cloud.enums.ediskconnection

class EDiskConnection:
    ## ディスクの接続方式を表す列挙子。
    
    IDE = "ide"
    ide = "ide"
    
    VIRTIO = "virtio"
    virtio = "virtio"
    
    ## @ignore
    _MAP = {
        "IDE": 100,
        "VIRTIO": 300
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
    
    
