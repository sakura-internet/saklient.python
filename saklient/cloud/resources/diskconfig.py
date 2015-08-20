# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...util import Util
from ..client import Client
from .script import Script
import saklient

str = six.text_type
# module saklient.cloud.resources.diskconfig

class DiskConfig(object):
    ## ディスク修正のパラメータ。
    
    # (instance field) _client
    
    ## @return {saklient.cloud.client.Client}
    def get_client(self):
        return self._client
    
    ## @ignore
    client = property(get_client, None, None)
    
    # (instance field) _disk_id
    
    ## @return {str}
    def get_disk_id(self):
        return self._disk_id
    
    ## @ignore
    disk_id = property(get_disk_id, None, None)
    
    # (instance field) _host_name
    
    ## @return {str}
    def get_host_name(self):
        return self._host_name
    
    ## @param {str} v
    # @return {str}
    def set_host_name(self, v):
        Util.validate_type(v, "str")
        self._host_name = v
        return v
    
    ## ホスト名
    host_name = property(get_host_name, set_host_name, None)
    
    # (instance field) _password
    
    ## @return {str}
    def get_password(self):
        return self._password
    
    ## @param {str} v
    # @return {str}
    def set_password(self, v):
        Util.validate_type(v, "str")
        self._password = v
        return v
    
    ## ログインパスワード
    password = property(get_password, set_password, None)
    
    # (instance field) _ssh_keys
    
    ## @return {str[]}
    def get_ssh_keys(self):
        return self._ssh_keys
    
    ## @return {str}
    def get_ssh_key(self):
        if len(self._ssh_keys) < 1:
            return None
        return self._ssh_keys[0]
    
    ## @param {str} v
    # @return {str}
    def set_ssh_key(self, v):
        Util.validate_type(v, "str")
        if len(self._ssh_keys) < 1:
            self._ssh_keys.append(v)
        else:
            self._ssh_keys[0] = v
        return v
    
    ## SSHキー
    ssh_key = property(get_ssh_key, set_ssh_key, None)
    
    ## SSHキー
    ssh_keys = property(get_ssh_keys, None, None)
    
    # (instance field) _ip_address
    
    ## @return {str}
    def get_ip_address(self):
        return self._ip_address
    
    ## @param {str} v
    # @return {str}
    def set_ip_address(self, v):
        Util.validate_type(v, "str")
        self._ip_address = v
        return v
    
    ## IPアドレス
    ip_address = property(get_ip_address, set_ip_address, None)
    
    # (instance field) _default_route
    
    ## @return {str}
    def get_default_route(self):
        return self._default_route
    
    ## @param {str} v
    # @return {str}
    def set_default_route(self, v):
        Util.validate_type(v, "str")
        self._default_route = v
        return v
    
    ## デフォルトルート
    default_route = property(get_default_route, set_default_route, None)
    
    # (instance field) _network_mask_len
    
    ## @return {int}
    def get_network_mask_len(self):
        return self._network_mask_len
    
    ## @param {int} v
    # @return {int}
    def set_network_mask_len(self, v):
        Util.validate_type(v, "int")
        self._network_mask_len = v
        return v
    
    ## ネットワークマスク長
    network_mask_len = property(get_network_mask_len, set_network_mask_len, None)
    
    # (instance field) _scripts
    
    ## @return {saklient.cloud.resources.script.Script[]}
    def get_scripts(self):
        return self._scripts
    
    ## スタートアップスクリプト {@link Script} の配列（pushによりスクリプトを追加できます）
    scripts = property(get_scripts, None, None)
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {str} diskId
    def __init__(self, client, diskId):
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(diskId, "str")
        self._client = client
        self._disk_id = diskId
        self._host_name = None
        self._password = None
        self._ssh_keys = []
        self._ip_address = None
        self._default_route = None
        self._network_mask_len = None
        self._scripts = []
    
    ## スタートアップスクリプトを追加します。
    # 
    # diskConfig.addScript(script) と diskConfig.scripts.push(script) の効果は同等です。
    # 
    # @param {saklient.cloud.resources.script.Script} script
    # @return {saklient.cloud.resources.diskconfig.DiskConfig} this
    def add_script(self, script):
        Util.validate_type(script, "saklient.cloud.resources.script.Script")
        self._scripts.append(script)
        return self
    
    ## 修正内容を実際のディスクに書き込みます。
    # 
    # @return {saklient.cloud.resources.diskconfig.DiskConfig} this
    def write(self):
        q = {}
        if self._host_name is not None:
            Util.set_by_path(q, "HostName", self._host_name)
        if self._password is not None:
            Util.set_by_path(q, "Password", self._password)
        if len(self._ssh_keys) > 0:
            Util.set_by_path(q, "SSHKey.PublicKey", "\n".join(self._ssh_keys))
        if self._ip_address is not None:
            Util.set_by_path(q, "UserIPAddress", self._ip_address)
        if self._default_route is not None:
            Util.set_by_path(q, "UserSubnet.DefaultRoute", self._default_route)
        if self._network_mask_len is not None:
            Util.set_by_path(q, "UserSubnet.NetworkMaskLen", self._network_mask_len)
        if 0 < len(self._scripts):
            notes = []
            for script in self._scripts:
                notes.append({
                    'ID': script._id()
                })
            Util.set_by_path(q, "Notes", notes)
        path = "/disk/" + self._disk_id + "/config"
        self._client.request("PUT", path, q)
        return self
    
