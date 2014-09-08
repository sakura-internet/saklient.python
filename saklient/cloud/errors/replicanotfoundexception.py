# -*- coding:utf-8 -*-

from ...errors.httpnotfoundexception import HttpNotFoundException

# module saklient.cloud.errors.replicanotfoundexception

class ReplicaNotFoundException(HttpNotFoundException):
    ## 対象が見つかりません。このストレージには指定リソースの複製が存在しません。
    
    # (class field) default_message = "対象が見つかりません。このストレージには指定リソースの複製が存在しません。"
    
    pass
