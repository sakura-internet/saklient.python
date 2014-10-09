# -*- coding:utf-8 -*-

import unittest, sys, os, re, random, string, time, subprocess
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datetime import datetime
from saklient.cloud.api import API
from saklient.cloud.resources.swytch import Swytch
from saklient.cloud.enums.eserverinstancestatus import EServerInstanceStatus
from saklient.errors.saklientexception import SaklientException
from saklient.errors.httpconflictexception import HttpConflictException

class TestLoadbalancer(unittest.TestCase):
    
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
        tag = 'saklient-test'
        
        # search a switch
        print('searching a swytch...')
        swytches = api.swytch.with_tag('lb-attached').limit(1).find()
        self.assertTrue(len(swytches) > 0)
        swytch = swytches[0]
        self.assertIsInstance(swytch, Swytch)
        self.assertTrue(len(swytch.ipv4_nets) > 0)
        net = swytch.ipv4_nets[0]
        print('%s/%d -> %s' % (net.address, net.mask_len, net.default_route))
        
        # create a loadbalancer
        print('creating a LB...')
        vrid = 123
        lb = api.appliance.create_load_balancer(swytch, vrid, ['133.242.255.244', '133.242.255.245'], True)
        
        def test_required():
            lb.save()
        self.assertRaises(SaklientException, test_required)
        # Requiredフィールドが未set時は SaklientException がスローされなければなりません
        lb.name = name
        lb.description = ''
        lb.tags = [tag]
        lb.save()
        
        lb.reload()
        self.assertEqual(lb.default_route, net.default_route)
        self.assertEqual(lb.mask_len, net.mask_len)
        self.assertEqual(lb.vrid, vrid)
        self.assertEqual(lb.swytch_id, swytch.id)
        
        # wait the LB becomes up
        print('waiting the LB becomes up...')
        if not lb.sleep_until_up(): fail('ロードバランサが正常に起動しません')
        
        # stop the LB
        time.sleep(1)
        print('stopping the LB...')
        if not lb.stop().sleep_until_down(): fail('ロードバランサが正常に停止しません')
        
        # delete the LB
        print('deleting the LB...')
        lb.destroy()



if __name__ == '__main__':
    unittest.main()
