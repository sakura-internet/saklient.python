# -*- coding:utf-8 -*-

import unittest, sys, os, re, random, string, time, subprocess
sys.path[:0] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import socket, struct
from datetime import datetime
from saklient.cloud.api import API
from saklient.cloud.resources.license import License
from saklient.errors.saklientexception import SaklientException
from saklient.errors.httpconflictexception import HttpConflictException


class TestLicense(unittest.TestCase):
    
    
    
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
        
        
        
        # search a info
        print('searching a license info...')
        infos = api.product.license.find()
        self.assertTrue(len(infos) > 0)
        
        # create a license
        print('creating a license...')
        license = api.license.create()
        license.name = name
        license.info = infos[0]
        license.save()
        
        # delete the license
        print('deleting the license...')
        license.destroy()



if __name__ == '__main__':
    unittest.main()
