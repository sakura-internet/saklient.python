# -*- coding:utf-8 -*-

import unittest, sys, os, re, random, string, time, subprocess
sys.path[:0] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from datetime import datetime
from saklient.cloud.api import API
from saklient.cloud.resources.server import Server
from saklient.cloud.resources.serverplan import ServerPlan
from saklient.cloud.resources.iface import Iface
from saklient.cloud.resources.swytch import Swytch

class TestServer(unittest.TestCase):
    
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
        description = 'This instance was created by saklient.python test'
        
        #
        print('creating a swytch...')
        swytch = api.swytch.create()
        self.assertIsInstance(swytch, Swytch)
        swytch.name = name
        swytch.description = description
        swytch.save()
        self.assertTrue(0 < int(swytch.id))
        
        #
        print('creating a server...')
        server = api.server.create()
        self.assertIsInstance(server, Server)
        server.name = name
        server.description = description
        server.plan = api.product.server.get_by_spec(1, 1)
        server.save()
        self.assertTrue(0 < int(server.id))
        
        #
        print('adding an interface to the server...')
        iface = server.add_iface()
        self.assertIsInstance(iface, Iface)
        self.assertTrue(0 < int(iface.id))
        self.assertEqual(iface.server_id, server.id)
        server.reload()
        self.assertEqual(server.ifaces[0].id, iface.id)
        self.assertEqual(server.ifaces[0].server_id, server.id)
        iface.reload()
        self.assertEqual(iface.swytch_id, None)
        
        #
        print('connecting the interface to the swytch...')
        iface.connect_to_swytch(swytch)
        self.assertEqual(iface.swytch_id, swytch.id)
        self.assertEqual(api.swytch.get_by_id(iface.swytch_id).id, swytch.id)
        
        #
        print('disconnecting the interface from the swytch...')
        iface.disconnect_from_swytch()
        
        # delete the server
        print('deleting the server...')
        server.destroy()
        
        # delete the swytch
        print('deleting the swytch...')
        swytch.destroy()
        

if __name__ == '__main__':
    unittest.main()
