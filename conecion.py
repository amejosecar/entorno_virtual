# import os
# import logging
# import mysql.connector
# from mysql.connector import pooling
# import pandas as pd
# from sqlalchemy import create_engine
# from dotenv import load_dotenv

# # Cargar credenciales desde un archivo .env
# load_dotenv()

# DB_CONFIG = {
#     'user': os.getenv("DB_USER"),
#     'password': os.getenv("DB_PASSWORD"),
#     'host': os.getenv("DB_HOST"),
#     'database': os.getenv("DB_NAME"),
#     'port': os.getenv("DB_PORT"),
# }

# # Configurar logging
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Crear pool de conexiones
# pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **DB_CONFIG)

# def ejecutar_sql(sql, parametros=()):
#     """Ejecuta una consulta SQL con manejo de errores y logging."""
#     connection = None
#     try:
#         connection = pool.get_connection()
#         cursor = connection.cursor()
#         cursor.execute(sql, parametros)
#         connection.commit()
#         logging.info("✅ SQL ejecutado correctamente")
#         return True
#     except mysql.connector.Error as e:
#         logging.error(f"❌ Error SQL: {e}")
#         return False
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()

# def leer_tabla(tabla):
#     """Lee una tabla de la base de datos usando SQLAlchemy."""
#     try:
#         db_url = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
#         engine = create_engine(db_url)
#         connection = engine.connect()
#         contenido = pd.read_sql(f"SELECT * FROM {tabla}", connection)
#         connection.close()
#         return contenido
#     except Exception as e:
#         logging.error(f"❌ Error al leer la tabla {tabla}: {e}")
#         return None

# def validar_conexion_bd():
#     """Valida la conexión a la base de datos con manejo de errores."""
#     connection = None
#     try:
#         connection = pool.get_connection()
#         logging.info("✅ Conexión a la base de datos OK")
#     except mysql.connector.Error as e:
#         logging.error(f"❌ Error de conexión a la base de datos: {e}")
#     finally:
#         if connection:
#             connection.close()
#             logging.info("🔗 Conexión cerrada")

# CODIGO PARA VALIDAR SI ESTA CARGDO EL ARCHIVO .ENV
# from dotenv import load_dotenv
# import os

# load_dotenv()

# print("DB_HOST:", os.getenv("DB_HOST"))  # Verifica si se está cargando

# conecion.py
#codigo original
def ejecutor_sql(codigo_sql):
    import mysql.connector
    # Configuración de la conexión usando el host público
    config = {
        'user': 'root',
        'password': 'ydnAMyHtiNYTxNsLpSKUWtqMMdUUlPqT',
        'host': 'switchback.proxy.rlwy.net',
        'database': 'railway',
        'port': 13556
    }
    
    connection = None
    success = False  # Asumimos fracaso por defecto.
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute(codigo_sql)
        connection.commit()
        print("✅ Ejecución correcta de SQL")
        success = True
    except mysql.connector.Error as e:
        print(f"❌ Error de MySQL: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("🔗 Conexión cerrada")
    return success



def leer_tabla(tabla):
    import pandas as pd
    from sqlalchemy import create_engine

    config = {
        'user': 'root',
        'password': 'ydnAMyHtiNYTxNsLpSKUWtqMMdUUlPqT',
        'host': 'switchback.proxy.rlwy.net',
        'database': 'railway',
        'port': 13556
    }
    # Creamos la URL de conexión para SQLAlchemy
    db_password = config['password']
    db_host = config['host']
    port = config['port']
    db_url = f"mysql+pymysql://root:{db_password}@{db_host}:{port}/{config['database']}"

    # Crear el motor (engine)
    engine = create_engine(db_url)

    connection = None
    try:
        # Intentar conectarse a la base de datos
        connection = engine.connect()
        contenido = pd.read_sql(f"SELECT * FROM {tabla}", connection)
    except Exception as e:
        print(f"Error de conexión: {e}")
        contenido = None
    finally:
        if connection:
            connection.close()
        return contenido

def validar_conexion_bd():
    """
    Valida la conexión a la base de datos intentando conectarse con mysql.connector
    usando la configuración definida en la función ejecutor_sql.
    """
    import mysql.connector
    config = {
        'user': 'root',
        'password': 'ydnAMyHtiNYTxNsLpSKUWtqMMdUUlPqT',
        'host': 'switchback.proxy.rlwy.net',
        'database': 'railway',
        'port': 13556
    }
    connection = None
    try:
        connection = mysql.connector.connect(**config)
        print("✅ Conexión a la base de datos: OK")
    except mysql.connector.Error as e:
        print(f"❌ Error de conexión a la base de datos: {e}")
    finally:
        if connection:
            connection.close()
            print("🔗 Conexión cerrada")


            