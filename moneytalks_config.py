
SOURCE = 'ftp://ftp.phila-records.com/2012 Cycle 1/'
EXTRACT_STORAGE = './data'
DB = './db/db.txt'
CSV_SCHEMA = {
    'contrib.txt': {'ID':'STRING', 'YEAR':'STRING', 'CYCLE':'STRING', 
                    'CODE':'STRING', 'CONTRIBUTOR_NAME':'STRING', 'ADDRESS':'STRING', 
                    'ADDRESS2':'STRING', 'CITY':'STRING', 'STATE':'STRING', 
                    'ZIP':'STRING', 'TBA1':'STRING', 'TBA2':'STRING','TBA3':'STRING', 
                    'TBA4':'STRING', 'TBA5':'STRING', 'TBA6':'STRING', 
                    'TBA7':'STRING', 'DATE1':'STRING', 'AMOUNT':'STRING', 
                    'TBA8':'STRING', 'TBA9':'STRING', 
                    'TBA10':'STRING', 'TBA11':'STRING', 'PURPOSE':'STRING',
                    'FILE_PATH':'STRING'},
    'testing.txt': {'ID':'STRING', 'YEAR':'STRING', 'CYCLE':'STRING', 
                    'CODE':'STRING', 'CONTRIBUTOR_NAME':'STRING', 'ADDRESS':'STRING', 
                    'ADDRESS2':'STRING', 'CITY':'STRING', 'STATE':'STRING', 
                    'ZIP':'STRING', 'TBA1':'STRING', 'TBA2':'STRING','TBA3':'STRING', 
                    'TBA4':'STRING', 'TBA5':'STRING', 'TBA6':'STRING', 
                    'TBA7':'STRING', 'DATE1':'STRING', 'AMOUNT':'STRING', 
                    'TBA8':'STRING', 'TBA9':'STRING', 
                    'TBA10':'STRING', 'TBA11':'STRING', 'PURPOSE':'STRING', 
                    'FILE_PATH':'STRING'},
    'debt.txt': {'ID':'STRING', 'YEAR:':'STRING', 'CYCLE':'STRING', 
                 'DEBT_HOLDER_NAME':'STRING', 'ADDRESS':'STRING', 
                 'ADDRESS2':'STRING', 'CITY':'STRING', 'STATE':'STRING',
                 'ZIP':'STRING', 'DATE1':'STRING', 'AMOUNT':'STRING', 
                 'DESCRIPTION':'STRING',
                 'TBA1':'STRING', 'TBA2':'STRING', 'TBA3':'STRING', 'TBA4':'STRING', 
                 'TBA5':'STRING', 'TBA6':'STRING', 'TBA7':'STRING', 'TBA8':'STRING', 
                 'TBA9':'STRING', 'TBA10':'STRING', 'TBA11':'STRING',
                 'FILE_PATH':'STRING'},
    'expense.txt': {'ID':'STRING', 'YEAR':'STRING', 'CYCLE':'STRING', 
                    'RECIPIENT':'STRING', 
                    'ADDRESS':'STRING', 'ADDRESS2':'STRING', 'CITY:':'STRING', 
                    'STATE':'STRING',
                    'ZIP':'STRING', 'DATE1':'STRING', 'AMOUNT':'STRING', 
                    'DESCRIPTION':'STRING',
                    'TBA1':'STRING', 'TBA2':'STRING', 'TBA3':'STRING', 'TBA4':'STRING', 
                    'TBA5':'STRING', 'TBA6':'STRING', 'TBA7':'STRING', 'TBA8':'STRING', 
                    'TBA9':'STRING', 'TBA10':'STRING', 'TBA11':'STRING', 'FILE_PATH':'STRING'},
    'receipt.txt': {'ID':'STRING', 'YEAR':'STRING', 
                    'CYCLE':'STRING', 'RECIPIENT':'STRING', 
                    'ADDRESS':'STRING', 'ADDRESS2':'STRING', 
                    'CITY':'STRING', 'STATE':'STRING',
                    'ZIP':'STRING', 'DESCRIPTION':'STRING', 
                    'DATE1':'STRING', 'AMOUNT':'STRING', 'FILE_PATH':'STRING'},
    'filer.txt': {'ID':'STRING', 'YEAR':'STRING', 'CYCLE:':'STRING', 'CODE':'STRING', 
                  'CODE2':'STRING', 'CODE3':'STRING', 'PAC_NAME:':'STRING', 
                  'TBA1':'STRING',
                  'TBA2':'STRING', 'PARTY':'STRING', 'ADDRESS':'STRING', 
                  'ADDRESS2':'STRING',
                  'CITY':'STRING', 'STATE:':'STRING', 'ZIP':'STRING', 'TBA3':'STRING', 
                  'TBA4':'STRING', 'AMOUNT1':'STRING', 'AMOUNT2':'STRING', 
                  'TBA8':'STRING', 'FILE_PATH':'STRING'}
}

