# iot_simulator.py
import pyodbc
import random

def insert_random_data():
    # Connection parameters (modify them to match your SQL Server setup)
    server = 'your_server_address'
    database = 'your_database_name'
    username = 'your_username'
    password = 'your_password'
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    connection = pyodbc.connect(conn_str)
    cursor = connection.cursor()

    # Generate random data
    device_id = random.randint(1, 100)  # Simulates 100 different devices
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(50.0, 60.0)

    # Insert data into the SQL Server
    query = "INSERT INTO IoTData (device_id, temperature, humidity) VALUES (?, ?, ?)"
    cursor.execute(query, device_id, temperature, humidity)
    connection.commit()

    cursor.close()
    connection.close()

if __name__ == "__main__":
    insert_random_data()
