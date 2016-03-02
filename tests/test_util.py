# -*- coding:utf-8 -*-

import unittest, sys, os
sys.path[:0] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from saklient.util import Util
from saklient.cloud.api import API
from saklient.cloud.client import Client
from saklient.errors.saklientexception import SaklientException

class TestUtil(unittest.TestCase):
    
    def test_should_access_objects_by_path(self):
        test = {}
        Util.set_by_path(test, "top", 123)
        self.assertEqual(test["top"], 123)
        Util.set_by_path(test, "first.second", 456)
        self.assertEqual(test["first"]["second"], 456)
        Util.set_by_path(test, ".weird..path", 789)
        self.assertEqual(test["weird"]["path"], 789)
        Util.set_by_path(test, "existing.None", None)
        self.assertIsNotNone(Util.get_by_path(test, "existing"))
        self.assertEqual(Util.get_by_path(test, "existing.None"), None)
        #
        self.assertEqual(Util.get_by_path(test, "top"), 123)
        self.assertEqual(Util.get_by_path(test, "first.second"), 456)
        self.assertEqual(Util.get_by_path(test, ".weird..path"), 789)
        #
        self.assertEqual(Util.get_by_path(test, "nothing"), None)
        self.assertEqual(Util.get_by_path(test, "nothing.child"), None)
        self.assertEqual(Util.get_by_path(test, "top.child"), None)
        #
        self.assertTrue(Util.exists_path(test, "top"))
        self.assertFalse(Util.exists_path(test, "top.child"))
        self.assertTrue(Util.exists_path(test, "first.second"))
        self.assertTrue(Util.exists_path(test, ".weird..path"))
        self.assertFalse(Util.exists_path(test, "nothing"))
        self.assertFalse(Util.exists_path(test, "nothing.child"))
        self.assertTrue(Util.exists_path(test, "existing"))
        self.assertTrue(Util.exists_path(test, "existing.None"))
        #
        test["first"]["second"] *= 10
        self.assertEqual(Util.get_by_path(test, "first.second"), 4560)
        
        #
        Util.validate_type(1, "int")
        Util.validate_type(1.1, "float")
        Util.validate_type(False, "bool")
        Util.validate_type("abc", "str")
        ex = SaklientException("a", "a")
        Util.validate_type(ex, "saklient.errors.saklientexception.SaklientException")
        Util.validate_type(ex, "Exception")
        
        #
        self.assertRaises(SaklientException, lambda: API.authorize("a", []))
        # 引数の型が異なる時は SaklientException がスローされなければなりません
        
        #
        self.assertRaises(TypeError, lambda: API.authorize("a"))
        # 引数の数が足りない時は TypeError がスローされなければなりません
        
        #
        def validation_test():
            server = API.authorize("a", "a").server.create()
            server.name = ["abc"]
        self.assertRaises(SaklientException, validation_test)
        # 引数の型が異なる時は SaklientException がスローされなければなりません
        
        #
        def immutable_test():
            server = API.authorize("a", "a").server.create()
            server.availability = "available"
        self.assertRaises(AttributeError, immutable_test)
        # 未定義または読み取り専用フィールドへのset時は AttributeError がスローされなければなりません
        
        #
        self.assertEqual(Util.ip2long('0.0.0.0'), 0)
        self.assertEqual(Util.ip2long('127.255.255.255'), 0x7FFFFFFF)
        self.assertEqual(Util.ip2long('128.0.0.0'), 0x80000000)
        self.assertEqual(Util.ip2long('255.255.255.255'), 0xFFFFFFFF)
        self.assertEqual(Util.ip2long('222.173.190.239'), 0xDEADBEEF)
        #
        self.assertEqual(Util.long2ip(0), '0.0.0.0')
        self.assertEqual(Util.long2ip(0x7FFFFFFF), '127.255.255.255')
        self.assertEqual(Util.long2ip(0x80000000), '128.0.0.0')
        self.assertEqual(Util.long2ip(0xFFFFFFFF), '255.255.255.255')
        self.assertEqual(Util.long2ip(0xDEADBEEF), '222.173.190.239')
        self.assertEqual(Util.long2ip(Util.ip2long('127.255.255.255') + 1), '128.0.0.0')
        #
        self.assertIsNone(Util.ip2long(None))
        self.assertIsNone(Util.ip2long(0))
        self.assertIsNone(Util.ip2long(''))
        self.assertIsNone(Util.ip2long('x'))
        self.assertIsNone(Util.ip2long('0.0.0'))
        self.assertIsNone(Util.ip2long('0.0.0.x'))
        self.assertIsNone(Util.ip2long('0.0.0.0.0'))
        self.assertIsNone(Util.ip2long('255.255.255.256'))
        self.assertIsNone(Util.ip2long('256.255.255.255'))
        self.assertIsNone(Util.long2ip(None))
        self.assertEqual(Util.long2ip('0'), '0.0.0.0')
        self.assertEqual(Util.long2ip(Util.ip2long('0.0.0.0') - 1), '255.255.255.255')
        self.assertIsNone(Util.long2ip(Util.ip2long('255.255.255.255') + 1))
        

if __name__ == '__main__':
    unittest.main()
