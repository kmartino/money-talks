import logging
import os
import json

import fusion 

def load(**kwargs):
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
        
    # generate sql and execute for each row, in each file,
    # stored in the records argument.
    for file_path, records in data.items():
        table_name = os.path.basename(file_path)
        if table_name in fusion_tables:
            table_id = fusion_tables[table_name]
            for row in records:
                fusion.insert_row(table_id, auth_token, row, 'ID')
        else:
            logging.warning('Rows for %s but not table definition in data')

def load_db(file_path):
    json_data=open(file_path)
    data = json.load(json_data)
    json_data.close()
    return data
