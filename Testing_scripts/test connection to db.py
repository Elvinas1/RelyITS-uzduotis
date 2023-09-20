import mysql.connector

# Define the MySQL database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "sales_data",
}

# SQL statement to create the "sales_records" table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS sales_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_date DATE,
    store_id VARCHAR(255),
    items_sold INT,
    total_paid DECIMAL(10, 2),
    total_receipts INT
)
"""

# Initialize the connection object to None
connection = None

try:
    # Attempt to establish a connection to the MySQL server
    connection = mysql.connector.connect(**db_config)

    # Check if the connection was successful
    if connection.is_connected():
        print("Connected to the MySQL database")

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Execute the SQL statement to create the table
        cursor.execute(create_table_query)

        # Commit the changes to the database
        connection.commit()

        print("Table 'sales_records' created or already exists")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
