
SOURCE = 'ftp://ftp.phila-records.com/2012 Cycle 1/'
EXTRACT_STORAGE = './data'
DB = './db/db.txt'
CSV_SCHEMA = {
    'contrib.txt': ['ID', 'YEAR', 'CYCLE', 'CODE', 
                    'CONTRIBUTOR_NAME', 'ADDRESS', 'ADDRESS2', 'CITY',
                    'STATE', 'ZIP', 'TBA1', 'TBA2','TBA3', 
                    'TBA4', 'TBA5', 'TBA6', 'TBA7', 
                    'DATE1', 'AMOUNT', 'TBA8', 'TBA9', 
                    'TBA10', 'TBA11', 'PURPOSE'],
    'debt.txt': ['ID', 'YEAR', 'CYCLE', 'DEBT_HOLDER_NAME', 
                 'ADDRESS', 'ADDRESS2', 'CITY', 'STATE',
                 'ZIP', 'DATE1', 'AMOUNT', 'DESCRIPTION',
                 'TBA1', 'TBA2', 'TBA3', 'TBA4', 
                 'TBA5', 'TBA6', 'TBA7', 'TBA8', 
                 'TBA9', 'TBA10', 'TBA11'],
    'expense.txt': ['ID', 'YEAR', 'CYCLE', 'RECIPIENT', 
                    'ADDRESS', 'ADDRESS2', 'CITY', 'STATE',
                    'ZIP', 'DATE1', 'AMOUNT', 'DESCRIPTION',
                    'TBA1', 'TBA2', 'TBA3', 'TBA4', 
                    'TBA5', 'TBA6', 'TBA7', 'TBA8', 
                    'TBA9', 'TBA10', 'TBA11'],
    'receipt.txt': ['ID', 'YEAR', 'CYCLE', 'RECIPIENT', 
                    'ADDRESS', 'ADDRESS2', 'CITY', 'STATE',
                    'ZIP', 'DESCRIPTION', 'DATE1', 'AMOUNT'],
    'filer.txt': ['ID', 'YEAR', 'CYCLE', 'CODE', 
                  'CODE2', 'CODE3', 'PAC_NAME', 'TBA1',
                  'TBA2', 'PARTY', 'ADDRESS', 'ADDRESS2',
                  'CITY', 'STATE', 'ZIP', 'TBA3', 
                  'TBA4', 'AMOUNT1', 'AMOUNT2', 'TBA8']
}

