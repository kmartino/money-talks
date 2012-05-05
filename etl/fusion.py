import logging 
import urllib
import urllib2
import subprocess
import csv
import json

def create_table(table_name, table_schema, auth_token):
    table_id = get_table_id(table_name, auth_token)
    if not table_id:
        logging.info('Creating %s' % table_name)
        sql = generate_create_table_sql(table_name, table_schema)
        output = send_query(sql, auth_token)
        for row in output:
            if output.line_num == 2:
                table_id = row[0]
                logging.info('Created table id %s for %s' % 
                             (table_id, table_name))
    else:
        logging.info('Found table id %s for %s' % (table_id, table_name))
    return table_id

def get_table_id(table_name, auth_token):
    table_output = send_query('SHOW TABLES', auth_token)
    table_id = None
    for row in table_output:
        if len(row) >= 2:
            if row[1] == table_name:
                table_id = row[0]
                break
    return table_id

def create_table_sql(table_name, table_schema):
    sql = "CREATE TABLE '%s' " % table_name
    sql = sql + '(' + ', '.join("%s: STRING" % x for x in table_schema) 
    sql = sql + ')'
    return sql

def insert_row_sql(table_id, row):
    columns_values = row.items()
    for index in range(len(columns_values)):
        print columns_values[index]
        if columns_values[index][1] == None:
            columns_values[index] = (columns_values[index][0], '')
    print columns_values
    sql = 'INSERT INTO %s ' % table_id
    sql = sql + '(' + ', '.join("%s" % x for x, y in columns_values) 
    sql = sql + ') VALUES '
    sql = sql + '(' + ', '.join("'%s'" % y.replace("'", "\\'") for x, y in columns_values) 
    sql = sql + ')'
    return sql

def get_row_id(table_id, auth_token,
               primary_key_column, primary_key_value):
    table_output = send_query("SELECT ROWID FROM %s WHERE %s='%s'" % 
                              (table_id, primary_key_column, 
                               primary_key_value),
                              auth_token)
    row_id = None
    for row in table_output:
        if table_output.line_num == 2:
            if len(row) > 0:
                row_id = row[0]
                logging.info('Found row id %s for %s in table %s' %
                             (row_id, primary_key_value, table_id))
                break
    return row_id
        

def insert_row(table_id, auth_token, row, primary_key_column):
    row_id = None
    if table_id:
        row_id = get_row_id(table_id, auth_token, 
                            primary_key_column,
                            row[primary_key_column])        
        if row_id:
            pass
        else:
            sql = generate_insert_row_sql(table_id, row)
            output = send_query(sql, auth_token)
            for row in output:
                if output.line_num == 2:
                    row_id = row[0]
                    logging.info('Inserted row id %s in %s' % 
                                 (row_id, table_name))
                    
    else:
        logging.error('Something is wrong')
    return row_id


def get_auth(username, password):
    """ Retrieves an authorization token, 
    using Google's ClientLogin.

    """
    req_data = urllib.urlencode({'Email': username,
                                 'Passwd': password,
                                 'service': 'fusiontables'})
    logging.info('Asking for authorization token...')
    req = urllib2.Request(
        url='https://www.google.com/accounts/ClientLogin', 
        data=req_data)
    resp = urllib2.urlopen(req)
    resp_body = resp.read()
    auth_resp_dict = dict(x.split("=")
                          for x in resp_body.split("\n") if x)
    resp.close()
    
    return auth_resp_dict['Auth']

def send_query(sql, authtoken):
    """ Sends query to Fusion Tables with a ClientLogin
    authorization token.
    """
    req_data = urllib.urlencode({
            'sql': sql
            })
    req_headers = {
        'Authorization': 'GoogleLogin auth=%s' % (authtoken)
        }
    logging.info('Sending sql %s' % sql)
    req = urllib2.Request(
        url='https://www.google.com/fusiontables/api/query',
        data=req_data, headers=req_headers)  
    resp = urllib2.urlopen(req)
    resp_body = resp.read()
    resp.close()
    csv_data = csv.reader(resp_body.split('\n'))
    return csv_data
