""" transform.py

Iterates over a directory of csv files and 
transforms them into a dictionary that is 
suitable for creating SQL statements from.

The dictionary is stored in its own location
for re-use.

"""
from collections import OrderedDict

import logging
import os
import csv
import json


def transform(**kwargs):
    """Transforms text files in the extract_storage directory and
    transforms them into a dictonary of dictionaries. A format that is
    easy to map to SQL statemtents that can upload content to Google's
    Fusion Tables.
    
    Keyword Arguments: 
    extract_storage -- the local directory the csv text files are in 
    db -- the local file to save the generated dictionary to

    """
    extract_storage = kwargs['extract_storage']
    db = kwargs['db']
    csv_schema = kwargs['csv_schema']

    logging.debug('transform %s' % extract_storage)
    data = {}
    for dirname, dirnames, filenames in os.walk(extract_storage):
        for subdirname in dirnames:
            logging.debug('In %s ' % os.path.join(dirname, subdirname))
        for filename in filenames:
            if filename.endswith('.txt'):
                file_path = os.path.join(dirname, filename)
                logging.debug('Parsing %s' % file_path)
                file_obj = open(file_path, 'rb')
                try:
                    table_name = os.path.basename(file_path)
                    reader = None
                    if table_name in csv_schema:
                        reader = csv.DictReader(file_obj, 
                                                fieldnames=csv_schema[table_name].keys())
                    else:
                        logging.warning('Skipping %s - no table definition in csv_schema.')

                    for row in reader:
                        if file_path not in data:
                            data[file_path] = []
                        row['FILE_PATH'] = file_path
                        data[file_path].append(row)

                finally:
                    file_obj.close()

    save_db(data, db)
    return data

def save_db(data, db):
    """Saves the contents of the dictionary in the data argument
    to the db file indicated in the db argument.

    """
    if not os.path.exists(os.path.dirname(db)):
        os.makedirs(os.path.dirname(db))
    output = json.dumps(data)
    f = open(db, 'w')
    f.write(output + '\n')
    f.close()

