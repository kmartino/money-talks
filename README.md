money-talks
===========

Summary: TODO

Installation and Setup
----------------------

### Install System Pre-requisites

This project requires Python 2.6 or higher. In addition, the
following pre-requisites need to be installed. If you already have
them, skip this:

Install virtualenv:

    sudo easy_install virtualenv 

Install pip:

    sudo easy_install pip

### Install Project Pre-requisites

When running the project for the first time, execute the following
steps. 

Navigate to the directory you extracted or checked out the
project to.

Create your virtualenv environment:

    virtualenv --no-site-packages .env 

Activate the project's virtualenv:

    source .env/bin/activate

Install the project's python libraries:

    pip install -r pip-requires.txt

Now you can run the project!!!!

Running the script
------------------

### Runing unit tests

Navigate to the directory you extractred, or checked out the project
to.

Activate the project's virtualenv if you haven't already:

    source .env/bin/activate

Run the unit test script:

    python -m unittest moneytalks_test

### Running the script

Navigate to the directory you extracted, or checked out the project
to.

Activate the project's virtualenv if you haven't already:

    source .env/bin/activate

To download csv files from the source system (overwrites files locally):

    python moneytalks.py e DEBUG
   
To extract information from them and create the local db file (overwrites the db file locally):

    python moneytalks.py t DEBUG

To load the db file to your Google Fusion tables (this will prompt for the credentials you associate with your Google Fusion account): 

    python moneytalks l DEBUG

The above will create the target tables indicated in moneytalks_config.py, with the columns indicated. If those tables exist, and rows with matching IDs exist, the script will update those rows. So running this repeatitively will not result in ever more rows being appended to your target tables.

Sources 
-------

- Philadelphia Election Data Source
  ftp://ftp.phila-records.com/
- OpenDataPhilly
  http://opendataphilly.org/
- Google: Google Fusion Tables API
  https://developers.google.com/fusiontables/
- Google: ClientLogin for Installed Applications
  https://developers.google.com/accounts/docs/AuthForInstalledApps
- Google: Election Ratings and Spatial Data with Fusion Tables
  https://developers.google.com/maps/articles/election-ratings
- Fuzzy Tolerance: Updating Google Fusion Tables from a CSV File Using Python
  http://fuzzytolerance.info/updating-google-fusion-table-from-a-csv-file-using-python/ 
- Python Module of the Week: csv
  http://www.doughellmann.com/PyMOTW/csv/
- ftputil documentation
  http://ftputil.sschwarzer.net/trac/wiki/Documentation#ftphost-walk
- johnkeefe.net: Making AP Election Data Easy
  http://johnkeefe.net/making-ap-election-data-easy-with-fusion-tabl