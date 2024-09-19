import mysql.connector
from mysql.connector import Error


db_config = {
    
    'host': 'localhost',
    'user': 'root',
    'password': '', 
    'database': 'secure_db'
}

def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Conectado a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def perform_sql_injection():
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    sql_injection_query = """
    SELECT * FROM users WHERE '1'='1';
    """
    
    try:
        cursor.execute(sql_injection_query)
        results = cursor.fetchall()
        
        print("Resultados de la consulta SQL inyectada:")
        for row in results:
            print(row)
            
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
    
   
    cursor.close()
    connection.close()

if __name__ == "__main__":
    perform_sql_injection()
