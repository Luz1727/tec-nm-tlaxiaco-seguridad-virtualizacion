import pandas as pd
import mysql.connector
from mysql.connector import Error

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Asegúrate de ingresar la contraseña si es necesario
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

def insert_data_from_csv(csv_file_path):
    connection = connect_to_database()
    if connection is None:
        return

    cursor = connection.cursor()

    # Leer el archivo CSV usando pandas
    data = pd.read_csv(csv_file_path)

    # Mostrar los nombres de las columnas
    print("Columnas en el archivo CSV:", data.columns)

    # Preparar las consultas SQL para insertar datos
    insert_customers_query = """
    INSERT INTO customers (customer_id, first_name, last_name, subscription_date, website)
    VALUES (%s, %s, %s, %s, %s)
    """

    insert_address_query = """
    INSERT INTO address (customer_id, company, city, country, phone_1, phone_2)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    insert_users_query = """
    INSERT INTO users (customer_id, email, password)
    VALUES (%s, %s, 'default_password')  # Puedes cambiar 'default_password' por la lógica que necesites
    """

    # Iterar sobre las filas del DataFrame y ejecutar las inserciones
    for index, row in data.iterrows():
        try:
            # Insertar en la tabla 'customers'
            customer_tuple = (
                row['customer_id'], 
                row['first_name'], 
                row['last_name'], 
                row['subscription_date'], 
                row['website']
            )
            cursor.execute(insert_customers_query, customer_tuple)

            # Insertar en la tabla 'address'
            address_tuple = (
                row['customer_id'], 
                row['Company'], 
                row['City'], 
                row['Country'], 
                row['Phone 1'], 
                row['Phone 2']
            )
            cursor.execute(insert_address_query, address_tuple)

            # Insertar en la tabla 'users'
            users_tuple = (
                row['customer_id'], 
                row['Email']
            )
            cursor.execute(insert_users_query, users_tuple)

        except KeyError as e:
            print(f"Error de clave en la fila {index}: {e}")
        except Error as e:
            print(f"Error al insertar los datos en la fila {index}: {e}")

    # Confirmar los cambios y cerrar la conexión
    connection.commit()
    cursor.close()
    connection.close()
    print("Datos insertados exitosamente")

# Ruta del archivo CSV (ajusta esta ruta a la ubicación real del archivo)
csv_file_path = 'C:/xampp/mysql/data/secure_db/customers-2000000.csv'
insert_data_from_csv(csv_file_path)




