# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.enums.escriptclass

class EScriptClass(object):
    ## スクリプトのクラスを表す列挙子。
    
    SHELL = "shell"
    shell = "shell"
    
    ANSIBLE = "ansible"
    ansible = "ansible"
    
    ## @ignore
    _MAP = {
        "SHELL": 200,
        "ANSIBLE": 300
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
    
    
