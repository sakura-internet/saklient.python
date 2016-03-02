# -*- coding:utf-8 -*-

import unittest, sys, os, re, random, string, time, subprocess
sys.path[:0] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from datetime import datetime
from saklient.util import Util
from saklient.cloud.api import API
from saklient.cloud.resources.routerplan import RouterPlan
from saklient.cloud.resources.swytch import Swytch
from saklient.cloud.resources.server import Server
from saklient.cloud.resources.iface import Iface
from saklient.cloud.resources.ipv6net import Ipv6Net
from saklient.cloud.resources.ipv4net import Ipv4Net


class TestRouter(unittest.TestCase):
  
  
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
        mask_len = 28
        mask_len_cnt = 1<<32-mask_len
        sroute_mask_len = 28
        sroute_mask_len_cnt = 1<<32-sroute_mask_len
        
        #
        swytch = None
        if True:
            print('ルータ＋スイッチの帯域プランを検索しています...')
            plans = api.product.router.find()
            min_mbps = 0x7FFFFFFF
            for plan in plans:
                self.assertIsInstance(plan, RouterPlan)
                self.assertTrue(0 < plan.band_width_mbps)
                min_mbps = min(plan.band_width_mbps, min_mbps)
            
            print('ルータ＋スイッチを作成しています...')
            router = api.router.create()
            router.name = name
            router.description = description
            router.band_width_mbps = min_mbps
            router.network_mask_len = mask_len
            router.save()
            
            print('ルータ＋スイッチの作成完了を待機しています...')
            if not router.sleep_while_creating(): fail('ルータが正常に作成されません')
            swytch = router.get_swytch()
        else:
            print('既存のルータ＋スイッチを取得しています...')
            swytches = api.swytch.with_name_like('saklient-static-1').limit(1).find()
            self.assertEqual(len(swytches), 1)
            swytch = swytches[0]
        
        self.assertIsInstance(swytch, Swytch)
        self.assertEqual(len(swytch.ipv4_nets), 1)
        self.assertIsInstance(swytch.ipv4_nets[0], Ipv4Net)
        self.assertEqual(len(swytch.ipv4_nets[0].range.as_array), mask_len_cnt-5)
        self.assertEqual(len(swytch.collect_used_ipv4_addresses()), 0)
        self.assertEqual(len(swytch.collect_unused_ipv4_addresses()), mask_len_cnt-5)
        
        #
        print('サーバを作成しています...')
        server = api.server.create()
        self.assertIsInstance(server, Server)
        server.name = name
        server.description = description
        server.plan = api.product.server.get_by_spec(1, 1)
        server.save()
        self.assertTrue(0 < int(server.id))
         
        #
        print('インタフェースを増設しています...')
        iface = server.add_iface()
        self.assertIsInstance(iface, Iface)
        self.assertTrue(0 < int(iface.id))
        
        #
        print('インタフェースをルータ＋スイッチに接続しています...')
        iface.connect_to_swytch(swytch)
        
        #
        print('インタフェースにIPアドレスを設定しています...')
        iface.user_ip_address = swytch.ipv4_nets[0].range.as_array[1]
        iface.save()
        self.assertEqual(len(swytch.collect_used_ipv4_addresses()), 1)
        self.assertEqual(len(swytch.collect_unused_ipv4_addresses()), mask_len_cnt-6)
        
        #
        print('ルータ＋スイッチの帯域プランを変更しています...')
        router_id_before = swytch.router.id
        swytch.change_plan(500 if swytch.router.band_width_mbps==100 else 100)
        self.assertNotEqual(swytch.router.id, router_id_before)
        
        #
        print('ルータ＋スイッチにIPv6ネットワークを割り当てています...')
        v6net = swytch.add_ipv6_net()
        self.assertIsInstance(v6net, Ipv6Net)
        self.assertEqual(len(swytch.ipv6_nets), 1)
        
        #
        print('ルータ＋スイッチにスタティックルートを割り当てています...')
        net0 = swytch.ipv4_nets[0]
        next_hop = Util.long2ip(Util.ip2long(net0.address) + 4)
        sroute = swytch.add_static_route(28, next_hop)
        self.assertIsInstance(sroute, Ipv4Net)
        self.assertEqual(len(swytch.ipv4_nets), 2)
        self.assertEqual(len(swytch.ipv4_nets[1].range.as_array), sroute_mask_len_cnt)
        
        #
        for i in range(len(swytch.ipv4_nets) - 1, 0, -1):
            print('ルータ＋スイッチからスタティックルートの割当を解除しています...')
            net = swytch.ipv4_nets[i]
            swytch.remove_static_route(net)
        
        #
        if 0 < len(swytch.ipv6_nets):
            print('ルータ＋スイッチからIPv6ネットワークの割当を解除しています...')
            swytch.remove_ipv6_net()
        
        #
        print('サーバを削除しています...')
        server.destroy()



if __name__ == '__main__':
    unittest.main()
