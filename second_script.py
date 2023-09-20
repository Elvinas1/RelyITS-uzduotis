import logging
import pandas as pd
import mysql.connector
from datetime import datetime

class SalesData:
    def __init__(self, db_config, log_file):
        self.db_config = db_config
        self.log_file = log_file
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            if self.connection.is_connected():
                logger.info("Connected to the MySQL database")
        except mysql.connector.Error as error:
            logger.error(f"Failed to connect to MySQL database: {error}")

    def insert_data(self, store_id, total_items, total_amount, transaction_date):
        try:
            cursor = self.connection.cursor()
            insert_query = """
            INSERT INTO sales_records (store_id, total_items, total_amount, transaction_date)
            VALUES (%s, %s, %s, %s)
            """
            data = (store_id, total_items, total_amount, transaction_date)
            cursor.execute(insert_query, data)
            self.connection.commit()
            logger.info("Data inserted successfully")
        except mysql.connector.Error as error:
            logger.error(f"Failed to insert data: {error}")

    def aggregate_data(self):
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT store_id, SUM(total_amount) AS total_sales, COUNT(*) AS total_receipts, SUM(total_items) AS total_items
            FROM sales_records
            GROUP BY store_id
            """
            cursor.execute(query)
            results = cursor.fetchall()
            df = pd.DataFrame(results, columns=['StoreID', 'TotalAmount', 'TotalReceipts', 'TotalItems'])
            df.to_csv('final_report.csv', index=False)
            logger.info("CSV file created successfully")
        except mysql.connector.Error as error:
            logger.error(f"Failed to fetch data: {error}")

    def close(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            logger.info("Connection closed")

if __name__ == '__main__':
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "database": "sales_data",
    }
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('sales_data.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    sales_data = SalesData(db_config, 'sales_data.log')
    try:
        sales_data.connect()
        sales_data.aggregate_data()
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        sales_data.close()