"""load.py

Loads a db file and uploads its contents to Google Fusion Tables.

"""
import logging
import os
import json
import time
import fusion 

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

    auth_token = fusion.get_auth(username, password)

    # create tables at Google Fusion if they do not exist
    # for each table in our schema argument
    fusion_tables = {}
    for table_name, table_schema in csv_schema.items():
        table_id = fusion.create_table(table_name, 
                                       table_schema,
                                       auth_token)
        fusion_tables[table_name] = table_id
        fusion.delete_all_rows(table_id, auth_token)
        
    # generate sql and execute for each row, in each file,
    # stored in the records argument.
    count = 1
    for file_path, records in data.items():
        table_name = os.path.basename(file_path)
        logging.info('Inserting %s rows for %s' % (len(records), file_path))
        logging.info('Processing %s of %s files' % (count, len(data.items())))
        table_id = fusion_tables[table_name]
        output = fusion.insert_rows(table_id, auth_token, records, file_path)

        count = count + 1

def load_db(file_path):
    json_data=open(file_path)
    data = json.load(json_data)
    json_data.close()
    return data
