# -*- coding: utf-8 -*-

from six.moves import urllib
from six.moves.urllib.error import URLError, HTTPError
import json, re, base64
import contextlib
from ..errors.exceptionfactory import ExceptionFactory

class Client(object):
    
    def __init__(self, token, secret):
        self.config = {
            'api_root': 'https://secure.sakura.ad.jp/cloud/',
            'api_root_suffix': None
        }
        self.set_access_key(token, secret)
    
    @staticmethod
    def native2haxe(r, depth):
        return r
    
    @staticmethod
    def haxe2native(r, depth):
        return r

    def clone_instance(self):
      instance = self.__class__(self.config['token'], self.config['secret'])
      instance.set_api_root(self.config['api_root'])
      instance.set_api_root_suffix(self.config['api_root_suffix'])
      return instance

    def set_api_root(self, url):
        self.config['api_root'] = url

    def set_api_root_suffix(self, suffix):
        self.config['api_root_suffix'] = suffix

    def set_access_key(self, token, secret):
        self.config['token']  = token
        self.config['secret'] = secret
        auth_bytes = (token+':'+secret).encode('utf-8')
        self.config['authorization'] = 'Basic ' + base64.b64encode(auth_bytes).decode("utf-8")
    
    def request(self, method, path, params={}):
        method = method.upper()
        if path[0] != '/':
            path = '/' + path
        params_json = json.dumps(params).encode(encoding='ascii')
        if method == 'GET':
            if params_json is not None:
                path += '?' + urllib.parse.quote(params_json)
            params_json = None
        if path[0:4] != 'http':
            url_root = self.config['api_root']
            if self.config['api_root_suffix'] is not None:
                if re.compile('is1[v-z]').match(self.config['api_root_suffix']):
                    url_root = re.compile('/cloud/$').sub('/cloud-test/', url_root)
                url_root += self.config['api_root_suffix'];
                url_root = re.compile('/?$').sub('/', url_root)
                if url_root[-1:] != '/':
                    url_root += '/'
            path = url_root + 'api/cloud/1.1' + path
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': self.config['authorization'],
            'User-Agent': 'saklient.python ver-0.0.6 rev-705e6fc541c30cec41e72e5e531418d64f196863',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Sakura-No-Authenticate-Header': '1',
            'X-Sakura-HTTP-Method': method,
            'X-Sakura-Request-Format': 'json',
            'X-Sakura-Response-Format': 'json',
            'X-Sakura-Error-Level': 'warning'
        }
        
        res = ''
        try:
            req = urllib.request.Request(path, params_json, headers)
            with contextlib.closing(urllib.request.urlopen(req)) as page:
                for line in page.readlines():
                    res += line.decode('utf-8')
        except HTTPError as ex:
            res = ex.read().decode('utf8', 'ignore')
            ret = None
            try:
                ret = json.loads(res)
            except Exception as ex2:
                pass
            if not isinstance(ret, dict):
                ret = {"error_code":None, "error_msg":None}
            raise ExceptionFactory.create(ex.code, ret["error_code"], ret["error_msg"]);
        
        return json.loads(res)
    
