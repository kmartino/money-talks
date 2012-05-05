import unittest
import logging
import sys

class MoneyTalksTest(unittest.TestCase):
    def setUp(self):
        self.instance = MetricsDashboard()
        
    def tearDown(self):
        pass

    def test_hello_world(self):
        self.assertEquals('Hello World', self.instance.hello_world())

if '__main__' == __name__:
    unittest.main()

