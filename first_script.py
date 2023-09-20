import os
import mysql.connector
import xml.etree.ElementTree as ET
import logging

class SalesData:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None
        self.cursor = None
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        file_handler = logging.FileHandler('sales_data.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            self.cursor = self.connection.cursor()
            self.logger.info('Connected to the MySQL database')
        except mysql.connector.Error as e:
            self.logger.error(f'Error connecting to MySQL: {e}')
            raise

    def create_table(self):
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS sales_records (
                id INT AUTO_INCREMENT PRIMARY KEY,
                transaction_date DATE,
                store_id VARCHAR(255),
                total_items INT,
                total_amount DECIMAL(10, 2),
                total_receipts INT
            )
            """
            self.cursor.execute(create_table_query)
            self.connection.commit()
            self.logger.info('Table "sales_records" created or already exists')
        except mysql.connector.Error as e:
            self.logger.error(f'Error creating table: {e}')
            raise

    def insert_data(self, directory_path):
        try:
            ns = {'ixretail': 'http://www.nrf-arts.org/IXRetail/namespace/'}
            xml_files = [file for file in os.listdir(directory_path) if file.endswith('.xml')]
            for xml_file in xml_files:
                file_path = os.path.join(directory_path, xml_file)
                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()
                    transaction_id_element = root.find(".//ixretail:TransactionID", ns)
                    if transaction_id_element is not None:
                        transaction_id = transaction_id_element.text
                        transaction_date = transaction_id[:10]
                    else:
                        transaction_date = None
                    store_id_element = root.find(".//ixretail:UnitID", ns)
                    if store_id_element is not None:
                        store_id = store_id_element.text
                    else:
                        store_id = None
                    total_items_element = root.find(".//ixretail:Quantity", ns)
                    if total_items_element is not None:
                        total_items = total_items_element.text
                    else:
                        total_items = None
                    total_amount_element = root.find(".//ixretail:Total[@TotalType='TransactionNetAmount']", ns)
                    if total_amount_element is not None:
                        total_amount = total_amount_element.text
                    else:
                        total_amount = None
                    total_receipts_element = root.find(".//ixretail:Total[@TotalType='TransactionPurchaseQuantity']", ns)
                    if total_receipts_element is not None:
                        total_receipts = total_receipts_element.text
                    else:
                        total_receipts = None
                    insert_query = "INSERT INTO sales_records (transaction_date, store_id, total_items, total_amount, total_receipts) VALUES (%s, %s, %s, %s, %s)"
                    self.cursor.execute(insert_query, (transaction_date, store_id, total_items, total_amount, total_receipts))
                    self.connection.commit()
                    self.logger.info(f'Inserted data from {xml_file} into the database')
                except Exception as e:
                    self.logger.error(f'Error processing {xml_file}: {str(e)}')
        except mysql.connector.Error as e:
            self.logger.error(f'Error inserting data: {e}')
            raise

    def close(self):
        if self.connection is not None and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            self.logger.info('MySQL connection closed')

if __name__ == '__main__':
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "database": "sales_data",
    }
    sales_data = SalesData(db_config)
    sales_data.connect()
    sales_data.create_table()
    sales_data.insert_data('C:/Users/Admin/Desktop/Uzduotis/main/receipts')
    sales_data.close()
