import mysql.connector

# Define the MySQL database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "sales_data",
}

try:
    # Attempt to establish a connection to the MySQL server
    connection = mysql.connector.connect(**db_config)

    # Check if the connection was successful
    if connection.is_connected():
        print("Connected to the MySQL database")

        # You can perform database operations here if needed

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the database connection when done
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed")
