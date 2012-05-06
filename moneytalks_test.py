import unittest
import logging
import sys

from mock import MagicMock

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

    def test_create_table_sql(self):
        table_name = 'contrib'
        table_schema = ['ID', 'YEAR', 'CYCLE', 'CODE', 
                    'CONTRIBUTOR_NAME']
        sql = fusion.create_table_sql(table_name, table_schema)
        expected_sql = '''CREATE TABLE 'contrib' (ID: STRING, YEAR: STRING, CYCLE: STRING, CODE: STRING, CONTRIBUTOR_NAME: STRING)'''
        self.assertEquals(expected_sql, sql)

    def test_insert_row_sql(self):
        table_id = '123456'
        row = {'ID':'123', 'YEAR':'2011', 'CYCLE':'1'}
        sql = fusion.insert_row_sql(table_id, row)
        expected_sql = '''INSERT INTO 123456 (CYCLE, ID, YEAR) VALUES ('1', '123', '2011')'''
        self.assertEquals(expected_sql, sql)

if '__main__' == __name__:
    unittest.main()

