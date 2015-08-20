# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.ftpinfo

class FtpInfo(object):
    ## FTPサーバのアカウント情報。
    
    # (instance field) _host_name
    
    ## @return {str}
    def get_host_name(self):
        return self._host_name
    
    ## ホスト名
    host_name = property(get_host_name, None, None)
    
    # (instance field) _user
    
    ## @return {str}
    def get_user(self):
        return self._user
    
    ## ユーザ名
    user = property(get_user, None, None)
    
    # (instance field) _password
    
    ## @return {str}
    def get_password(self):
        return self._password
    
    ## パスワード
    password = property(get_password, None, None)
    
    ## @ignore
    # @param {any} obj
    def __init__(self, obj):
        self._host_name = (obj["HostName"] if "HostName" in obj else None)
        self._user = (obj["User"] if "User" in obj else None)
        self._password = (obj["Password"] if "Password" in obj else None)
    
