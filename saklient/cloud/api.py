# -*- coding:utf-8 -*-

from ..util import Util
from .client import Client
from .product import Product
from .model.model_icon import Model_Icon
from .model.model_server import Model_Server
from .model.model_disk import Model_Disk
from .model.model_appliance import Model_Appliance
from .model.model_archive import Model_Archive
from .model.model_isoimage import Model_IsoImage
from .model.model_iface import Model_Iface
from .model.model_swytch import Model_Swytch
from .model.model_router import Model_Router
from .model.model_ipv6net import Model_Ipv6Net
from .model.model_script import Model_Script

# module saklient.cloud.api

class API:
    ## さくらのクラウドAPIクライアントを利用する際、最初にアクセスすべきルートとなるクラス。
    # 
    # @see API.authorize
    
    # (instance field) _client
    
    ## @return {saklient.cloud.client.Client}
    def get_client(self):
        return self._client
    
    ## @ignore
    client = property(get_client, None, None)
    
    # (instance field) _product
    
    ## @return {saklient.cloud.product.Product}
    def get_product(self):
        return self._product
    
    ## 商品情報にアクセスするためのモデルを集めたオブジェクト。
    product = property(get_product, None, None)
    
    # (instance field) _icon
    
    ## @return {saklient.cloud.model.model_icon.Model_Icon}
    def get_icon(self):
        return self._icon
    
    ## アイコンにアクセスするためのモデル。
    icon = property(get_icon, None, None)
    
    # (instance field) _server
    
    ## @return {saklient.cloud.model.model_server.Model_Server}
    def get_server(self):
        return self._server
    
    ## サーバにアクセスするためのモデル。
    server = property(get_server, None, None)
    
    # (instance field) _disk
    
    ## @return {saklient.cloud.model.model_disk.Model_Disk}
    def get_disk(self):
        return self._disk
    
    ## ディスクにアクセスするためのモデル。
    disk = property(get_disk, None, None)
    
    # (instance field) _appliance
    
    ## @return {saklient.cloud.model.model_appliance.Model_Appliance}
    def get_appliance(self):
        return self._appliance
    
    ## アプライアンスにアクセスするためのモデル。
    appliance = property(get_appliance, None, None)
    
    # (instance field) _archive
    
    ## @return {saklient.cloud.model.model_archive.Model_Archive}
    def get_archive(self):
        return self._archive
    
    ## アーカイブにアクセスするためのモデル。
    archive = property(get_archive, None, None)
    
    # (instance field) _iso_image
    
    ## @return {saklient.cloud.model.model_isoimage.Model_IsoImage}
    def get_iso_image(self):
        return self._iso_image
    
    ## ISOイメージにアクセスするためのモデル。
    iso_image = property(get_iso_image, None, None)
    
    # (instance field) _iface
    
    ## @return {saklient.cloud.model.model_iface.Model_Iface}
    def get_iface(self):
        return self._iface
    
    ## インタフェースにアクセスするためのモデル。
    iface = property(get_iface, None, None)
    
    # (instance field) _swytch
    
    ## @return {saklient.cloud.model.model_swytch.Model_Swytch}
    def get_swytch(self):
        return self._swytch
    
    ## スイッチにアクセスするためのモデル。
    swytch = property(get_swytch, None, None)
    
    # (instance field) _router
    
    ## @return {saklient.cloud.model.model_router.Model_Router}
    def get_router(self):
        return self._router
    
    ## ルータにアクセスするためのモデル。
    router = property(get_router, None, None)
    
    # (instance field) _ipv6_net
    
    ## @return {saklient.cloud.model.model_ipv6net.Model_Ipv6Net}
    def get_ipv6_net(self):
        return self._ipv6_net
    
    ## IPv6ネットワークにアクセスするためのモデル。
    ipv6_net = property(get_ipv6_net, None, None)
    
    # (instance field) _script
    
    ## @return {saklient.cloud.model.model_script.Model_Script}
    def get_script(self):
        return self._script
    
    ## スクリプトにアクセスするためのモデル。
    script = property(get_script, None, None)
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    def __init__(self, client):
        Util.validate_type(client, "saklient.cloud.client.Client")
        self._client = client
        self._product = Product(client)
        self._icon = Model_Icon(client)
        self._server = Model_Server(client)
        self._disk = Model_Disk(client)
        self._appliance = Model_Appliance(client)
        self._archive = Model_Archive(client)
        self._iso_image = Model_IsoImage(client)
        self._iface = Model_Iface(client)
        self._swytch = Model_Swytch(client)
        self._router = Model_Router(client)
        self._ipv6_net = Model_Ipv6Net(client)
        self._script = Model_Script(client)
    
    ## 指定した認証情報を用いてアクセスを行うAPIクライアントを作成します。
    # 
    # 必要な認証情報は、コントロールパネル右上にあるアカウントのプルダウンから
    # 「設定」を選択し、「APIキー」のページにて作成できます。
    # 
    # @static
    # @param {str} token ACCESS TOKEN
    # @param {str} secret ACCESS TOKEN SECRET
    # @return {saklient.cloud.api.API} APIクライアント
    @staticmethod
    def authorize(token, secret):
        Util.validate_type(token, "str")
        Util.validate_type(secret, "str")
        c = Client(token, secret)
        return API(c)
    
    ## 認証情報を引き継ぎ、指定したゾーンへのアクセスを行うAPIクライアントを作成します。
    # 
    # @param {str} name ゾーン名
    # @return {saklient.cloud.api.API} APIクライアント
    def in_zone(self, name):
        Util.validate_type(name, "str")
        ret = API(self._client.clone_instance())
        ret._client.set_api_root_suffix("zone/" + name)
        return ret
    
