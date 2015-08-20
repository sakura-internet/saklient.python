# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.enums.eapplianceclass

class EApplianceClass(object):
    ## アプライアンスのクラスを表す列挙子。
    
    LOADBALANCER = "loadbalancer"
    loadbalancer = "loadbalancer"
    
    VPCROUTER = "vpcrouter"
    vpcrouter = "vpcrouter"
    
    ## @ignore
    _MAP = {
        "LOADBALANCER": 10,
        "VPCROUTER": 20
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
    
    
