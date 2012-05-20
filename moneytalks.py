""" moneytalks.py

Downloads header-less csv files from a an ftp server, transforms them into 
dictionaries, and uploads the records to Google Fusion tables.

Specifically works with data from ftp://ftp.phila-records.com/ but with
little work new sources of data and table schemas can be added.

"""
import sys
import os
import logging
import getpass

from etl import extract
from etl import transform
from etl import load

if __name__ == "__main__":
    # Get the client configuration
    import moneytalks_config
    source = moneytalks_config.SOURCE
    extract_storage = moneytalks_config.EXTRACT_STORAGE
    db = moneytalks_config.DB
    csv_schema = moneytalks_config.CSV_SCHEMA

    # Get command line arguments
    if len(sys.argv) >=2:
        run_cmds = sys.argv[1]
        if len(sys.argv) == 3:
            log_level = sys.argv[2]
            if log_level == 'DEBUG':
                logging.basicConfig(level=logging.DEBUG)
            else:
                logging.basicConfig(level=logging.INFO)
        else:
            logging.basicConfig(level=logging.INFO)
    else:
        print 'Indicate what commands you want to execute (e Extract, t Tranform, l Load), in addition to logging level.'
        print 'Example to do all three: python moneytalks.py etl DEBUG'
        print 'Example to excute Extract: python moneytalks.py e DEBUG'
        sys.exit()

    # Lets get to work...
    downloaded_count = None
    data = None
    output = None
    
    if run_cmds.find('e') > -1:
        # Extract files from ftp location and download them
        downloaded_count = extract.extract(source = source, 
                                           extract_storage = extract_storage)
        print 'Downloaded %s files ' % downloaded_count

    if run_cmds.find('t') > -1:
        # Transform downloaded files
        data = transform.transform(extract_storage = extract_storage,
                                 db = db,
                                 csv_schema = csv_schema)
        print 'Processed and stored %s files in %s' % (len(data), db)

    if run_cmds.find('l') > -1:
        # Load to processed content to Google Fusion
        username = raw_input('Google user: ')
        password = getpass.getpass('Google password: ')
        output = load.load(db=db, 
                           csv_schema = csv_schema,
                           username = username,
                           password = password)
        
    print 
    print 'Done'

        

