# -*- coding:utf-8 -*-

from ...errors.saklientexception import SaklientException
from ..client import Client
from .appliance import Appliance
from ...util import Util

# module saklient.cloud.resources.vpcrouter

class VpcRouter(Appliance):
    ## ロードバランサの実体1つに対応し、属性の取得や操作を行うためのクラス。
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(VpcRouter, self).__init__(client, obj, wrapped)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
    
