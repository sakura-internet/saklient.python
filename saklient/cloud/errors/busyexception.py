# -*- coding:utf-8 -*-

from ...errors.httpserviceunavailableexception import HttpServiceUnavailableException

# module saklient.cloud.errors.busyexception

class BusyException(HttpServiceUnavailableException):
    ## サービスが利用できません。サーバが混雑しています。しばらく時間をおいてから再度お試しください。
    
    # (class field) default_message = "サービスが利用できません。サーバが混雑しています。しばらく時間をおいてから再度お試しください。"
    
    pass
