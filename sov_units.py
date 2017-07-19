#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import sov_engines
import unittest

class SovEnginesTests(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_responseEngine(self):
        self.assertEqual( sov_engines.responseEngine(3, ['.*find.*','.*answer.*','.*need.*','.*know.*','.*aquire.*','.*get.*'], "get"), True)
 
 
if __name__ == '__main__':
    unittest.main()