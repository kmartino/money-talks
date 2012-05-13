"""load.py

Loads a db file and uploads its contents to Google Fusion Tables.

"""
import logging
import os
import json
import time
import csv
import sys

from fusiontables.authorization.clientlogin import ClientLogin
from fusiontables import ftclient
from fusiontables.sql.sqlbuilder import SQL
from unidecode import unidecode

def load(**kwargs):
    """Loads tables and rows from the db file and uploads
    them to Google Fusion Tables. 

    Will create tables indicated int the csv_schema argument
    if they do not exist as Google Fusion Tables.

    Will update rows, instead of inserting them, 
    if the row currently exists.

    """
    db = kwargs['db']
    csv_schema = kwargs['csv_schema']
    username = kwargs['username']
    password = kwargs['password']

    data = load_db(db)

    token = ClientLogin().authorize(username, password)

    ft_client = ftclient.ClientLoginFTClient(token)

    show_table_output = ft_client.query(SQL().showTables())

    # create tables at Google Fusion if they do not exist
    # for each table in our schema argument
    fusion_tables = {}
    for table_name, table_schema in csv_schema.items():
        table_id = get_table_id_from_result(table_name, show_table_output)
        if not table_id:            
            table = {table_name:table_schema}
            table_id = int(ft_client.query(SQL().createTable(table)).split("\n")[1])
        fusion_tables[table_name] = table_id
        ft_client.query("DELETE FROM %s" % table_id)
    logging.info(fusion_tables)

    # generate sql and execute for each row, in each file,
    # stored in the records argument.
    count = 1
    for file_path, records in data.items():
        table_name = os.path.basename(file_path)
        logging.info('Inserting %s rows for %s' % (len(records), file_path))
        logging.info('Processing %s of %s files' % (count, len(data.items())))
        table_id = fusion_tables[table_name]
        queries = []
        batches = []
        query_count = 0
        num_records = len(records)
        for record in records:
            query = SQL().insert(table_id, record)
            queries.append(query)
            query_count = query_count + 1
            if query_count % 200 == 0 and query_count < num_records:
                batches.append(queries)
                queries[:] = []
            elif query_count == num_records:
                batches.append(queries)

        time.sleep(1)
        try:
            for batch in batches:
                full_query = ";".join(batch)                
                insert_output = ft_client.query(full_query)
                logging.info(insert_output)
        except:
            logging.error(sys.exc_info()[0])
            logging.error(sys.exc_info()[1])
            logging.error(full_query)
            
        count = count + 1

def load_db(file_path):
    json_file=open(file_path)
    json_data = json_file.read()
    json_file.close()
    data = json.loads(json_data, object_hook=_decode_dict)
    return data

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = unidecode(value)
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        if value == None:
            value = ''
        rv[key] = value
        
    return rv

def get_table_id_from_result(table_name, results):
    table_id = None
    csv_data = csv.reader(results.split('\n'))
    for row in csv_data:
        if len(row) > 0:
            if row[1] == table_name:
                table_id = row[0]
    return table_id
