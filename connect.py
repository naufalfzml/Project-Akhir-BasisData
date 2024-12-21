import pyodbc
import os

# function to create a connection to the database
def create_connection():

    server = 'NAUFAL\SQLEXPRESS'      # Ubah sesuai dengan nama server kalian     #
    database = 'Database_Hotel'       # Ubah sesuai dengan nama database kalian   #

    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

    # try to connect to the database
    try:
        # create the connection
        conn = pyodbc.connect(connection_string)
        return conn
    except pyodbc.Error as e:
        # print the error if there is one
        print(f'Error: {e}')
        return None