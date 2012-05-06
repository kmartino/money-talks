import unittest
import logging
import sys

from mock import MagicMock

import moneytalks
import moneytalks_config
from etl import extract
from etl import transform
from etl import load

class MoneyTalksTest(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_money_talks_config(self):
        self.assertIsNotNone(moneytalks_config.DB)
        self.assertIsNotNone(moneytalks_config.CSV_SCHEMA)
        self.assertIsNotNone(moneytalks_config.EXTRACT_STORAGE)        
        self.assertIsNotNone(moneytalks_config.SOURCE)

if '__main__' == __name__:
    unittest.main()

