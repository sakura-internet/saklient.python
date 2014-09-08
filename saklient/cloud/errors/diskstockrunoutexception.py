# -*- coding:utf-8 -*-

from ...errors.httpserviceunavailableexception import HttpServiceUnavailableException

# module saklient.cloud.errors.diskstockrunoutexception

class DiskStockRunOutException(HttpServiceUnavailableException):
    ## サービスが利用できません。作成済みディスクを確保できませんでした。サーバが混雑している可能性があります。
    
    # (class field) default_message = "サービスが利用できません。作成済みディスクを確保できませんでした。サーバが混雑している可能性があります。"
    
    pass
