# -*- coding:utf-8 -*-

import unittest, sys, os
sys.path[:0] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from saklient.errors.exceptionfactory import ExceptionFactory
from saklient.errors.httpexception import HttpException
from saklient.errors.httpnotfoundexception import HttpNotFoundException
from saklient.cloud.errors.serverpowermustbeupexception import ServerPowerMustBeUpException

class TestException(unittest.TestCase):
    
    def test_should_be_created(self):
        
        x = ExceptionFactory.create(404)
        self.assertIsInstance(x, HttpNotFoundException)
        
        x = ExceptionFactory.create(409, 'server_power_must_be_up')
        self.assertIsInstance(x, ServerPowerMustBeUpException)
        
        x = ExceptionFactory.create(666, 'nameless_http_error', 'Ia! Cthulhu Fthagn!')
        self.assertIsInstance(x, HttpException)
        self.assertEqual(str(x), 'Ia! Cthulhu Fthagn!')

if __name__ == '__main__':
    unittest.main()
