import unittest
import logging
import sys

from minimock import Mock

import moneytalks
import moneytalks_config
from etl import extract
from etl import transform
from etl import load
from etl import fusion 

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

    def test_get_table_id(self):

        results = '123,"table1"\n245,"contrib"'

        expected_table_id = '245'
        fake_table_name ='contrib'
        table_id = load.get_table_id(fake_table_name, results)

        self.assertEquals(expected_table_id, table_id)

        
if '__main__' == __name__:
    unittest.main()

