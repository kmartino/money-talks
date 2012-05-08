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

    def test_create_table_sql(self):
        fake_table_name = 'contrib'
        fake_table_schema = ['ID', 'YEAR', 'CYCLE', 'CODE', 
                    'CONTRIBUTOR_NAME']
        sql = fusion.create_table_sql(fake_table_name, fake_table_schema)
        expected_sql = '''CREATE TABLE 'contrib' (ID: STRING, YEAR: STRING, CYCLE: STRING, CODE: STRING, CONTRIBUTOR_NAME: STRING)'''
        self.assertEquals(expected_sql, sql)

    def test_insert_row_sql(self):

        fake_table_id = '123456'
        fake_row = {'ID':'123', 'YEAR':'2011', 'CYCLE':'1'}
        sql = fusion.create_insert_row_sql(fake_table_id, fake_row)
        expected_sql = '''INSERT INTO 123456 (CYCLE, ID, YEAR) VALUES ('1', '123', '2011')'''
        self.assertEquals(expected_sql, sql)

    def test_get_table_id(self):

        # set up mock results from Google Fusion SQL
        fusion.send_query = Mock('fusion.send_query')
        fusion.send_query.mock_returns = [['123','table1'], 
                                          ['245','contrib']]
        expected_table_id = '245'

        fake_table_name ='contrib'
        fake_auth_token = '123'
        table_id = fusion.get_table_id(fake_table_name, fake_auth_token)
        self.assertEquals(expected_table_id, table_id)

    def test_get_row_id(self):
        # fusion.send_query = Mock('fusion.send_query')
        # fusion.send_query.mock_returns = ['ROWID', '2456']

        # expected_row_id = '2456'

        # fake_table_id = '245'
        # fake_auth_token = '123'
        # fake_primary_key_column = 'ID'
        # fake_primary_key_value = '546'
        # row_id = fusion.get_row_id(fake_table_id, fake_auth_token,
        #                            fake_primary_key_column,
        #                            fake_primary_key_value)
        # self.assertEquals(expected_row_id, row_id)
        pass

        
if '__main__' == __name__:
    unittest.main()

