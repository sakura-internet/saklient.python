# -*- coding:utf-8 -*-

import unittest, sys, os, re, random, string, time, subprocess
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datetime import datetime
from saklient.cloud.api import API
from saklient.cloud.resources.server import Server
from saklient.cloud.resources.serverplan import ServerPlan
from saklient.cloud.resources.iface import Iface
from saklient.cloud.resources.archive import Archive
from saklient.cloud.resources.disk import Disk
from saklient.cloud.enums.eserverinstancestatus import EServerInstanceStatus
from saklient.errors.saklientexception import SaklientException
from saklient.errors.httpconflictexception import HttpConflictException

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
        
        
        
        # should be found
        servers = api.server.sort_by_memory().find()
        self.assertIsInstance(servers, list)
        self.assertTrue(0 < len(servers))
        
        mem = 0
        for server in servers:
            self.assertIsInstance(server, Server)
            self.assertIsInstance(server.plan, ServerPlan)
            self.assertTrue(0 < server.plan.cpu)
            self.assertTrue(0 < server.plan.memory_mib)
            self.assertTrue(0 < server.plan.memory_gib)
            self.assertEqual(server.plan.memory_mib / server.plan.memory_gib, 1024)
            self.assertIsInstance(server.tags, list)
            for tag in server.tags:
                self.assertIsInstance(tag, str)
            self.assertTrue(mem <= server.plan.memory_gib)
            mem = server.plan.memory_gib
        
        # should be limited
        servers = api.server.limit(1).find()
        self.assertEqual(len(servers), 1)
        
        
        
        # should be CRUDed
        name = '!python_test-' + datetime.now().strftime('%Y%m%d_%H%M%S') + '-' + ''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
        description = 'This instance was created by saklient.python test'
        tag = 'saklient-test'
        cpu = 1
        mem = 2
        host_name = 'saklient-test'
        ssh_public_key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3sSg8Vfxrs3eFTx3G//wMRlgqmFGxh5Ia8DZSSf2YrkZGqKbL1t2AsiUtIMwxGiEVVBc0K89lORzra7qoHQj5v5Xlcdqodgcs9nwuSeS38XWO6tXNF4a8LvKnfGS55+uzmBmVUwAztr3TIJR5TTWxZXpcxSsSEHx7nIcr31zcvosjgdxqvSokAsIgJyPQyxCxsPK8SFIsUV+aATqBCWNyp+R1jECPkd74ipEBoccnA0pYZnRhIsKNWR9phBRXIVd5jx/gK5jHqouhFWvCucUs0gwilEGwpng3b/YxrinNskpfOpMhOD9zjNU58OCoMS8MA17yqoZv59l3u16CrnrD saklient-test@local'
        ssh_private_key_file = root + '/test-sshkey.txt'
        
        # search archives
        print('searching archives...')
        archives = api.archive \
            .with_name_like('CentOS 6. 64bit') \
            .with_size_gib(20) \
            .with_shared_scope() \
            .limit(1) \
            .find()
        self.assertTrue(0 < len(archives))
        archive = archives[0]
        
        # search scripts
        print('searching scripts...')
        scripts = api.script \
            .with_name_like('WordPress') \
            .with_shared_scope() \
            .limit(1) \
            .find()
        self.assertTrue(0 < len(scripts))
        script = scripts[0]
        
        # create a disk
        print('creating a disk...')
        disk = api.disk.create()
        self.assertRaises(SaklientException, lambda: disk.save())
        # Requiredフィールドが未set時は SaklientException がスローされなければなりません
        disk.name = name
        disk.description = description
        disk.tags = [tag]
        disk.plan = api.product.disk.ssd
        disk.source = archive
        disk.save()
        self.assertEqual(disk.size_gib, 20)
        
        # check an immutable field
        print('updating the disk...')
        def immutable_test():
            disk.size_mib = 20480
            disk.save()
        self.assertRaises(SaklientException, immutable_test)
        # Immutableフィールドの再set時は SaklientException がスローされなければなりません
        
        # create a server
        print('creating a server...')
        server = api.server.create()
        self.assertIsInstance(server, Server)
        server.name = name
        server.description = description
        server.tags = [tag]
        server.plan = api.product.server.get_by_spec(cpu, mem)
        server.save()
        
        # check the server properties
        self.assertTrue(0 < int(server.id))
        self.assertEqual(server.name, name)
        self.assertEqual(server.description, description)
        self.assertIsInstance(server.tags, list)
        self.assertEqual(len(server.tags), 1)
        self.assertEqual(server.tags[0], tag)
        self.assertEqual(server.plan.cpu, cpu)
        self.assertEqual(server.plan.memory_gib, mem)
        
        # connect to shared segment
        print('connecting the server to shared segment...')
        iface = server.add_iface()
        self.assertIsInstance(iface, Iface)
        self.assertTrue(0 < int(iface.id))
        iface.connect_to_shared_segment()
        
        # wait disk copy
        print('waiting disk copy...')
        self.assertTrue(disk.sleep_while_copying())
        # アーカイブからディスクへのコピーがタイムアウトしました
        disk.source = None
        disk.reload()
        self.assertIsInstance(disk.source, Archive)
        self.assertEqual(disk.source.id, archive.id)
        self.assertEqual(disk.size_gib, archive.size_gib)
        
        # connect the disk to the server
        print('connecting the disk to the server...')
        disk.connect_to(server)
        
        # config the disk
        print('writing configuration to the disk...')
        passwd = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(8)])
        diskcfg = disk.create_config()
        diskcfg.host_name = host_name
        diskcfg.password = passwd
        diskcfg.ssh_key = ssh_public_key
        diskcfg.add_script = script
        diskcfg.write()
        
        # boot
        print('booting the server...')
        server.boot()
        time.sleep(1)
        server.reload()
        self.assertEqual(server.instance.status, EServerInstanceStatus.UP)
        
        # boot conflict
        print('checking the server power conflicts...')
        self.assertRaises(HttpConflictException, lambda: server.boot())
        # サーバ起動中の起動試行時は HttpConflictException がスローされなければなりません
        
        # ssh
        ip_address = server.ifaces[0].ip_address
        self.assertIsNotNone(ip_address)
        cmd = "ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -i"+ssh_private_key_file+" root@"+ip_address+" hostname"
        ssh_success = False
        print('trying to SSH to the server...')
        for i in range(10):
            time.sleep(5)
            ph = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
            host_name_got = "".join([l.decode("utf-8") for l in ph.stdout.readlines()]).rstrip()
            err = "".join([l.decode("utf-8") for l in ph.stderr.readlines()]).rstrip()
            ph.stdout.close()
            ph.stderr.close()
            if err != "": print(err)
            if host_name != host_name_got: continue
            ssh_success = True
            break
        self.assertTrue(ssh_success)
        # 作成したサーバへ正常にSSHできません
        
        # stop
        time.sleep(3)
        print('stopping the server...')
        server.stop()
        self.assertTrue(server.sleep_until_down())
        # サーバが正常に停止しません
        
        # disconnect the disk from the server
        print('disconnecting the disk from the server...')
        disk.disconnect()
        
        # delete the server
        print('deleting the server...')
        server.destroy()
        
        # duplicate the disk
        print('duplicating the disk (expanding to 40GiB)...')
        disk2 = api.disk.create()
        disk2.name = name + "-copy"
        disk2.description = description
        disk2.tags = [tag]
        disk2.plan = api.product.disk.hdd
        disk2.source = disk
        disk2.size_gib = 40
        disk2.save()
        
        # wait disk duplication
        print('waiting disk duplication...')
        self.assertTrue(disk2.sleep_while_copying())
        # ディスクの複製がタイムアウトしました 
        disk2.source = None
        disk2.reload()
        self.assertIsInstance(disk2.source, Disk)
        self.assertEqual(disk2.source.id, disk.id)
        self.assertEqual(disk2.size_gib, 40)
        
        # delete the disks
        print('deleting the disks...')
        disk2.destroy()
        disk.destroy()
        

if __name__ == '__main__':
    unittest.main()
