# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from .models.model_serverplan import Model_ServerPlan
from .models.model_diskplan import Model_DiskPlan
from .models.model_routerplan import Model_RouterPlan
from .models.model_licenseinfo import Model_LicenseInfo
from .client import Client
from ..util import Util
import saklient

str = six.text_type
# module saklient.cloud.product

class Product(object):
    ## 商品情報にアクセスするためのモデルを集めたクラス。
    
    # (instance field) _server
    
    ## @return {saklient.cloud.models.model_serverplan.Model_ServerPlan}
    def get_server(self):
        return self._server
    
    ## サーバプラン情報。
    server = property(get_server, None, None)
    
    # (instance field) _disk
    
    ## @return {saklient.cloud.models.model_diskplan.Model_DiskPlan}
    def get_disk(self):
        return self._disk
    
    ## ディスクプラン情報。
    disk = property(get_disk, None, None)
    
    # (instance field) _router
    
    ## @return {saklient.cloud.models.model_routerplan.Model_RouterPlan}
    def get_router(self):
        return self._router
    
    ## ルータ帯域プラン情報。
    router = property(get_router, None, None)
    
    # (instance field) _license
    
    ## @return {saklient.cloud.models.model_licenseinfo.Model_LicenseInfo}
    def get_license(self):
        return self._license
    
    ## ライセンス種別情報。
    license = property(get_license, None, None)
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    def __init__(self, client):
        Util.validate_type(client, "saklient.cloud.client.Client")
        self._server = Model_ServerPlan(client)
        self._disk = Model_DiskPlan(client)
        self._router = Model_RouterPlan(client)
        self._license = Model_LicenseInfo(client)
    
