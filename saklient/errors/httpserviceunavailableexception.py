# -*- coding:utf-8 -*-

from .httpexception import HttpException

# module saklient.errors.httpserviceunavailableexception

class HttpServiceUnavailableException(HttpException):
    ## サービスが利用できません。対象は利用できない、またはサーバが混雑しています。このエラーが繰り返し発生する場合は、メンテナンス情報、サポートサイトをご確認ください。
    
    # (class field) default_message = "サービスが利用できません。対象は利用できない、またはサーバが混雑しています。このエラーが繰り返し発生する場合は、メンテナンス情報、サポートサイトをご確認ください。"
    
    pass
