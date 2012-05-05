Summary
=======

Installation and Setup
----------------------

### Install System Pre-requisites

If you virtualenv and pip installed, these steps can be skipped. If
you don't know for sure, run them, it won't hurt.

1. Install virtualenv:

   $ sudo easy_install virtualenv 

2. Install pip:

   $ sudo easy_install pip

### Install Project Pre-requisites

When running this project for the first time, execute the following
steps. 

1. Navigate to the directory you extracted or checked out the
project to.

2. Create your virtualenv environment:

   $ virtualenv --no-site-packages .env 

3. Activate the project's virtualenv:

   $ source .env/bin/activate

4. Install the project's python libraries:

   $ pip install -r pip-requires.txt

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

3. Create the etl.oauth.cfg file if you haven't already. This file is
   used to authenticate you with the project's Google Fusion table
   api.

4. To load data downloaded and parsed:

$ python etl.py 'ftp://ftp.phila-records.com/2012 Cycle 1/' './data' l DEBUG

5. To refresh authentication information:

$ python etl.py 'ftp://ftp.phila-records.com/2012 Cycle 1/' './data' a DEBUG

* Rationale of the script

* Sources 

- [[ftp://ftp.phila-records.com/][Philadelphia Election Data Source]]
- [[https://developers.google.com/fusiontables/][Google: Google Fusion Tables API]]
- [[https://developers.google.com/accounts/docs/AuthForInstalledApps][Google: ClientLogin for Installed Applications]]
- [[https://developers.google.com/maps/articles/election-ratings][Google: Election Ratings and Spatial Data with Fusion Tables]]
- [[http://www.doughellmann.com/PyMOTW/csv/][Python Module of the Week: csv]]
- [[http://ftputil.sschwarzer.net/trac/wiki/Documentation#ftphost-walk][ftputil documentation]]
- OAuth
  - [[https://developers.google.com/fusiontables/docs/articles/oauthfusiontables][Google: Using OAuth 2.0 for Authorization to Fusion Tables in Web Applications]]
  - [[https://developers.google.com/accounts/docs/OAuth2InstalledApp][Google: Using OAuth 2.0 for Installed Applications]]
  - [[https://gmaps-samples.googlecode.com/svn/trunk/fusiontables/oauth_tokens.py][Google: oauth_token generator sample script]]
- [[http://fuzzytolerance.info/updating-google-fusion-table-from-a-csv-file-using-python/][Fuzzy Tolerance: Updating Google Fusion Tables from a CSV File Using Python]]
- [[http://johnkeefe.net/making-ap-election-data-easy-with-fusion-tabl][johnkeefe.net: Making AP Election Data Easy]]
- [[http://stackoverflow.com/questions/101742/how-do-you-access-an-authenticated-google-app-engine-service-from-a-non-web-py][Stack Overflow: How do you access an authenticated Google App Engine service from a (non-web) python client?]]
