#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import sys
# from saklient.cloud.Client import Client
#     
# client = Client(sys.argv[1], sys.argv[2])
# servers = client.request("GET", "/server")
# print(servers['Servers'][0]['Name'])

import sys, os, json, datetime
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from saklient.cloud.api import API

if __name__ == '__main__':

    api = API.authorize(sys.argv[1], sys.argv[2])

    # # 停止中のサーバに接続されているディスクを一覧
    # servers = api.server.with_status("down").find()
    # for server in servers:
    #     # if server.tags:
    #         print("")
    #         print("server [%s] %s at %s" % (server.id, server.instance.status, server.instance.status_changed_at))
    #         print("    tags: %s" % ', '.join(server.tags))
    #         for iface in server.ifaces:
    #             print("    iface [%s] %s %s" % (iface.id, iface.mac_address, iface.ip_address or iface.user_ip_address))
    #         disks = server.find_disks() # same as: disks = api.disk.with_server_id(server.id).find()
    #         #print(json.dumps(server.dump(), sort_keys=True, indent=4, separators=(',', ': ')))
    #         for disk in disks:
    #             print("    disk [%s] %s" % (disk.id, disk.name))

    # now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # servers = api.server.with_tag("abc").find()
    # for server in servers:
    #     print("server [%s] %s" % (server.id, server.name))
    #     server.description += "\n" + now
    #     server.save()
    #     print("%s" % (server.description))
    #     print("")
    # 

    icons = api.icon.with_name_like("ubuntu").limit(1).find()
    assert 0 < len(icons), "icon not found"
    icon = icons[0]
    print("icon [%s] %s" % (icon.id, icon.name))
    print("")
    
    servers = api.server.with_name_like("cent").find()
    for server in servers:
        print("server [%s] %s" % (server.id, server.name))
        server.icon = None
        server.save()
        print("  changed icon to nothing: %s" % ("OK" if server.icon is None else "NG"))
        server.icon = icon
        server.save()
        print("  changed icon to: [%s] %s" % (server.icon.id, server.icon.name))
        print("")

    # plan_from = api.product.server.get_by_spec(2, 4)
    # print("plan from: [%s] %dcore %dGB" % (plan_from.id, plan_from.cpu, plan_from.memory_gib))
    # plan_to   = api.product.server.get_by_spec(4, 8)
    # print("plan to:   [%s] %dcore %dGB" % (plan_to.id, plan_to.cpu, plan_to.memory_gib))
    # print("")
    # 
    # servers = api.server.with_plan(plan_from).find()
    # for server in servers:
    #     print("server [%s] %dcore %dGB '%s'" % (server.id, server.plan.cpu, server.plan.memory_gib, server.name))
    #     server.change_plan(plan_to)
    #     print("    -> [%s] %dcore %dGB" % (server.id, server.plan.cpu, server.plan.memory_gib))
    #     print("")

