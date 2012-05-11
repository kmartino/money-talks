money-talks
===========

Money Talks focuses on local campaign finance data from Philadelphia.
It was initiated by journalists Tom Ferrick and Chris Brennan,
partnered with Karl Martino, Inquirer data visualization specialist
Rob Kandell and Kristen Mosbrucker, and Jared Brey, during 2012's
Barcamp NewsInnovation hackathon event.

The script, as it is currently in Github, downloads header-less CSVs
from ftp://ftp.phila-records.com/, re-structures them, and then
uploads that content to Google Fusion for visualization and searching.
The script is reusable against other header-less CSV's sources over
FTP, and could be quickly repurposed to parse data from other
Web-based locations. The script is written in such a way that it can
be ran repeatidly without unwanted side-effects.

Coming soon:

1. The front end Web-based interface to the data at Google Fusion.

2. Fleshing out a strong set unit tests - big challenge is that the current implementation of the script is mostly a wrapper of pre-existing functionality - which is as it should be.

3. Improved script interface and error handling.

4. A write-up explaining the mechanics of the script, why it is
organized the way it is, to help others who would like to write
similar automated routines.

Installation and Setup
----------------------

### Install System Pre-requisites

Money Talks requires Python 2.6 or higher. In addition, the
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

To download csv files from the source system (overwrites files
locally):

    python moneytalks.py e DEBUG
   
To extract information from them and create the local db file
(overwrites the db file locally):

    python moneytalks.py t DEBUG

To load the db file to your Google Fusion tables (this will prompt for
the credentials you associate with your Google Fusion account):

    python moneytalks l DEBUG

The above will create the target tables indicated in
moneytalks_config.py, with the columns indicated. If those tables
exist, and rows with matching IDs exist, the script will update those
rows. So running this repeatitively will not result in ever more rows
being appended to your target tables.

Links
-------

- Philadelphia Election Data Source
  ftp://ftp.phila-records.com/
- OpenDataPhilly
  http://opendataphilly.org/
- Metropolis
  http://www.phlmetropolis.com/
- Philly Clout
  http://www.philly.com/philly/blogs/cityhall/
- Philadelphia Inquirer and Daily News
  http://www.philly.com/
- WHYY
  http://www.whyy.org/
- Center for Public Interest Journalism
  http://www.cpijournalism.org/
- Google: Google Fusion Tables API
  https://developers.google.com/fusiontables/
- Google: ClientLogin for Installed Applications
  https://developers.google.com/accounts/docs/AuthForInstalledApps
- Google: Election Ratings and Spatial Data with Fusion Tables
  https://developers.google.com/maps/articles/election-ratings
- Fuzzy Tolerance: Updating Google Fusion Tables from a CSV File Using Python
  http://fuzzytolerance.info/updating-google-fusion-table-from-a-csv-file-using-python
- Chris L Keller: Using Python to Send Open States API Data to Fusion
  http://www.chrislkeller.com/using-python-to-send-open-states-api-data-to
- Python Module of the Week: csv
  http://www.doughellmann.com/PyMOTW/csv/
- ftputil documentation
  http://ftputil.sschwarzer.net/trac/wiki/Documentation#ftphost-walk
- MiniMock
  http://pypi.python.org/pypi/MiniMock
- StackOverflow: Python, unit-testing and mocking imports
  http://stackoverflow.com/questions/178458/python-unit-testing-and-mocking-imports
- johnkeefe.net: Making AP Election Data Easy
  http://johnkeefe.net/making-ap-election-data-easy-with-fusion-tabl
- git
  http://git-scm.com/
- Pythom FAQ: Webdeb
  http://me.veekun.com/blog/2012/05/05/python-faq-webdev/
- Learn Python the Hard Way
  https://github.com/chrislkeller/sunlight-ft-map.git
- Python Module of the Week: codecs
  http://www.doughellmann.com/PyMOTW/codecs/
- Stack Overflow: Dealing with utf-like content
  http://stackoverflow.com/questions/5842115/converting-a-string-which-contains-both-utf-8-encoded-bytestrings-and-codepoints
- Google: Python Sample Code with OAuth and Standard Library
  https://google-developers.appspot.com/fusiontables/docs/samples/python
- Python Wiki: Handling Exceptions
  http://wiki.python.org/moin/HandlingExceptions
- Beautiful Soup 
  http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html#Beautiful%20Soup%20Gives%20You%20Unicode,%20Dammit
- fusion-tables-client-python: sqlbuilder
  https://code.google.com/p/fusion-tables-client-python/source/browse/trunk/src/sql/sqlbuilder.py?r=22