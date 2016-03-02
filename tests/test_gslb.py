# -*- coding:utf-8 -*-

import unittest, sys, os, re, random, string, time, subprocess
sys.path[:0] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import socket, struct
from datetime import datetime
from saklient.util import Util
from saklient.cloud.api import API
from saklient.cloud.resources.gslb import Gslb
from saklient.errors.httpnotfoundexception import HttpNotFoundException


def ip2long(ip):
    return struct.unpack("!L", socket.inet_aton(ip))[0]

def long2ip(num):
    return socket.inet_ntoa(struct.pack('!L', num))

class TestGslb(unittest.TestCase):
    
    
    
    TESTS_CONFIG_READYMADE_LB_ID = None
    
    def test_should_be_cruded(self):
        
        # load config file
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        test_ok_file = root + '/testok'
        if not os.path.exists(test_ok_file):
            print("詳細テストを行うには " + test_ok_file + " をtouchしてください。")
            sys.exit(0)
        
        config_file = root + '/config.sh'
        self.assertTrue(os.path.exists(config_file)) # config_file を作成してください。
        
        config = {}
        fh = open(config_file, "r")
        for line in fh:
            m = re.search("^\\s*export\\s+(\\w+)\\s*=\\s*(.+?)\\s*$", line)
            if m is None: continue
            key = m.group(1)
            value = m.group(2)
            value = re.sub("'([^']*)'|\"([^\"]*)\"|\\\\(.)|(.)", lambda m: m.group(1) or m.group(2) or m.group(3) or m.group(4), value)
            config[key] = value
        fh.close()
        
        self.assertIn('SACLOUD_TOKEN', config)
        self.assertIn('SACLOUD_SECRET', config)
        self.assertIn('SACLOUD_ZONE', config)
        
        # authorize
        api = API.authorize(config['SACLOUD_TOKEN'], config['SACLOUD_SECRET'], config['SACLOUD_ZONE'])
        self.assertIsInstance(api, API)
        
        
        
        # should be CRUDed
        name = '!python_test-' + datetime.now().strftime('%Y%m%d_%H%M%S') + '-' + ''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
        
        
        
        # create a LB
        print('GSLBを作成しています...')
        gslb = api.common_service_item.create_gslb("http", 10, True)
        self.assertIsInstance(gslb, Gslb)
        gslb.path_to_check = '/index.html'
        gslb.response_expected = 200
        gslb.name = name
        gslb.description = 'This is a test'
        gslb.save()
        id = gslb.id
        self.assertTrue(int(id) > 0)
        self.assertEqual(gslb.name, name)
        self.assertEqual(len(gslb.servers), 0)
        
        gslb = api.common_service_item.get_by_id(id)
        self.assertEqual(gslb.id, id)
        self.assertEqual(gslb.path_to_check, '/index.html')
        self.assertEqual(gslb.response_expected, 200)
        self.assertEqual(gslb.name, name)
        self.assertEqual(len(gslb.servers), 0)
        
        server = gslb.add_server()
        server.enabled = True
        server.weight = 10
        server.ip_address = "49.212.82.90"
        gslb.save()
        self.assertEqual(len(gslb.servers), 1)
        
        gslb = api.common_service_item.get_by_id(id)
        self.assertEqual(len(gslb.servers), 1)
        
        print('GSLBを削除しています...')
        gslb.destroy()
        
        self.assertRaises(HttpNotFoundException, lambda: api.common_service_item.get_by_id(id))
        # GSLBが正しく削除されていません



if __name__ == '__main__':
    unittest.main()
