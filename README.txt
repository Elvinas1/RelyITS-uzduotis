------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
README
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Data base importing(MySql):


To import the "sales_data.sql" database into phpMyAdmin, follow these steps:

Access phpMyAdmin: Open your web browser and navigate to your phpMyAdmin interface. If you are using cPanel, you can access phpMyAdmin through the cPanel dashboard.

Log in to phpMyAdmin: Enter your username and password to log in to phpMyAdmin. The default username is "root," and the password is "root".

Go to the Import tab: Once you have logged into phpMyAdmin, click on the "Import" tab in the top menu.

And Voila!!!!!!!


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. First Script(first_script.py) Python script reads sales data from receipt XML files and inserts it into a MySQL database. It also aggregates the data grouped by store and creates a CSV file with the results.

First Script(first_script.py) requires the following dependencies:

Python 3.x:				Install Python 3.x from the official website
mysql-connector-python:       pip install mysql-connector-python
xml.etree.ElementTree:		It's in the stdlib: http://docs.python.org/2/library/xml.etree.elementtree.html. No need to install it with pip!!!


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Usage:

Provide the correct connection to MySql. In this situation:
db_config = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "database": "sales_data",
    }



Provide the path to the directory containing the XML files that you want to process.


Run the script.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Explanation of what code does:


The script will create a table called "sales_records" in your MySQL database if it doesn't exist.

The script will insert the sales data from the XML files into the "sales_records" table.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Logging:


The script uses the logging module to log messages to a file called "sales_data.log". The log file will be created in the same directory as the script. The log messages include information about the script's progress, such as when it connects to the database, when it creates the table, when it inserts data into the table, and when it creates the CSV file.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


3. Second Script(second_script.py) requires the following dependencies:

Prerequisites:

Python 3.x:				Install Python 3.x from the official website
mysql-connector-python:       pip install mysql-connector-python
pandas:				pip install pandas

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This Python script connects to a MySQL database, creates a table for sales records, and aggregates data grouped by store. The aggregated data is then saved as a CSV file. The script also logs various events using the Python logging module.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Provide the correct connection to MySql. In this situation:

db_config = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "database": "sales_data",
    }

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Explanation of what code does:

The script will get information about sales from table called "sales_records" in our MySQL database.
The script will aggregate data grouped by store.
The script will provide a final CSV file.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Logging:

The script uses the logging module to log messages to a file called "sales_data.log". The log file will be created in the same directory as the script. The log messages include information about the script's progress, such as when it connects to the database and when it creates the CSV file.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
