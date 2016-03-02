# -*- coding:utf-8 -*-

import unittest, sys, os
sys.path[:0] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from saklient.cloud.enums.eserverinstancestatus import EServerInstanceStatus

class TestEnum(unittest.TestCase):
    
    def test_should_be_defined(self):
        self.assertEqual(EServerInstanceStatus.UP, "up");
        self.assertEqual(EServerInstanceStatus.DOWN, "down");
     
    def test_should_be_compared(self):
        self.assertEqual(EServerInstanceStatus.compare("up", "up"), 0);
        self.assertEqual(EServerInstanceStatus.compare("up", "down"), 1);
        self.assertEqual(EServerInstanceStatus.compare("down", "up"), -1);
        self.assertEqual(EServerInstanceStatus.compare("UNDEFINED-SYMBOL", "up"), None);
        self.assertEqual(EServerInstanceStatus.compare("up", "UNDEFINED-SYMBOL"), None);
        self.assertEqual(EServerInstanceStatus.compare(None, "up"), None);
        self.assertEqual(EServerInstanceStatus.compare("up", None), None);
        self.assertEqual(EServerInstanceStatus.compare(None, None), None);

if __name__ == '__main__':
    unittest.main()
