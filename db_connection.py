import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost', 
            database='mydb',
            user='usuario',    
            password='123456'
                )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return connection
