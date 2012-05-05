money-talks
===========

Summary: TODO

Installation and Setup
----------------------

### Install System Pre-requisites

This is a project that requires Python 2.6 or higher. In addition, the
following pre-requisites need to be installed. If you already have
them, skip this:

1. Install virtualenv:

    sudo easy_install virtualenv 

2. Install pip:

    sudo easy_install pip

### Install Project Pre-requisites

When running this project for the first time, execute the following
steps. 

Navigate to the directory you extracted or checked out the
project to.

Create your virtualenv environment:

    virtualenv --no-site-packages .env 

Activate the project's virtualenv:

    source .env/bin/activate

Install the project's python libraries:

    pip install -r pip-requires.txt

5. Now you can run the project!!!!

Running the script
------------------

### Running Unit Tests

$ python -m unittest moneytalks_test

### Running the script

1. Navigate to the directory you extracted, or checked out the project
   to, if you haven't already:

2. Activate the project's virtualenv if you haven't already:

   $ source .env/bin/activate

3. To downloaded csv files:

   $ python moneytalks.py e DEBUG
   
4. To extract information from them and create the local db file:

   $ python moneytalks.py t DEBUG

5. To load the db file to Google's Fusion tables (this will prompt you
for your username and password. Beware - if you have a table there
with the names indicated in moneytalks_config.py - THEY WILL BE
OVERWRITTEN!):

   $ python moneytalks l DEBUG

Rationale of the script
-----------------------

TODO

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