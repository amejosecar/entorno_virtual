# -*- coding: utf-8 -*-
"""MySQL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OIvkhe7bkCDrO_Eh7PNiaNZAeh7othQS

Creación de una base de datos en Railway.com   
- https://railway.com/
- 🛠️ La aplicación Railway ofrece una solución sencilla para implementar bases de datos MySQL sin instalación.
- 🔑 Se puede acceder fácilmente a las variables de conexión para la integración con clientes de bases de datos.
"""

!pip install mysql-connector-python

import pandas as pd

"""# Creamos la conexión a la base de datos de railway"""

import mysql.connector
# mysql://root:sQGJOjroYvDHdacUUcfqgwnuYrsFqkbv@viaduct.proxy.rlwy.net:17016/railway
# Configuración de la conexión usando el host público
config = {
    'user': 'root',  # Usuario
    'password': 'sQGJOjroYvDHdacUUcfqgwnuYrsFqkbv',  # Contraseña
    'host': 'viaduct.proxy.rlwy.net',  # Host público de Railway
    'database': 'railway',  # Nombre de la base de datos
    'port': 17016  # Puerto público de Railway
}

# Establecer la conexión
connection = mysql.connector.connect(**config)

# Crear un cursor para ejecutar consultas
cursor = connection.cursor()

# Verificar que puedo enviarle SQL
cursor.execute("SELECT 1")
result = cursor.fetchone()
print(result)

# Cerrar el cursor y la conexión
cursor.close()
connection.close()

"""# Creamos una función que se conecte a la Base de Datos, ejecute el código SQL y cierre la conexión"""

def ejecutor_sql(codigo_sql):
    import mysql.connector
    # Configuración de la conexión usando el host público
    config = {
        'user': 'root',  # Usuario
        'password': 'sQGJOjroYvDHdacUUcfqgwnuYrsFqkbv',  # Contraseña
        'host': 'viaduct.proxy.rlwy.net',  # Host público de Railway
        'database': 'railway',  # Nombre de la base de datos
        'port': 17016  # Puerto público de Railway
    }

    # Crear un cursor para ejecutar consultas
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Crear la tabla si no existe
        cursor.execute(codigo_sql)
        connection.commit()
        print("✅ Ejecución correcta de SQL")

    except mysql.connector.Error as e:
        print(f"❌ Error de MySQL: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("🔗 Conexión cerrada")

"""## Creación de la base de datos"""

# Crear una base de datos
create_table_query = """
CREATE DATABASE videoclub;
USE videoclub;
"""
ejecutor_sql(create_table_query)

"""# Inserción de la tabla de ciudades"""

# Crear una tabla
create_table_query = """
-- Tabla Ciudades
CREATE TABLE Ciudades (
ciudad_id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
provincia VARCHAR(30),
comunidad VARCHAR(30),
cod_postal VARCHAR(5),
latitud DECIMAL(11, 8),
longitud DECIMAL(11, 8)
);
"""
ejecutor_sql(create_table_query)

# Eliminar una tabla
delete_table_query = """
-- Tabla Ciudades
DROP TABLE Ciudades;
"""
# ejecutor_sql(delete_table_query)

"""## Vamos a añadir todos los municipios de España a Ciudades"""

municipios_espana = pd.read_excel("https://www.businessintelligence.info/resources/assets/listado-longitud-latitud-municipios-espana.xls", skiprows=2)
# Como añadirlos todos tarda más de 15 minutos, selecciono sólo los de Euskadi
municipios_espana = municipios_espana[municipios_espana['Comunidad'] == 'País Vasco']
municipios_espana.head()

cp = pd.read_csv("https://github.com/inigoflores/ds-codigos-postales-ine-es/raw/refs/heads/master/data/codigos_postales_municipios.csv")
cp.head()

municipios_espana = municipios_espana.merge(cp, left_on='Población', right_on='municipio_nombre')
municipios_espana.head()

municipios_espana.info()

"""Esta función irá añadiendo a la base de datos cada municipio, recibiendo los datos como parámetro"""

# Insertar datos de ciudades
def insertar_ciudades(values):
    insert_query = f"""INSERT INTO Ciudades (nombre, provincia, comunidad, cod_postal, latitud, longitud)
    VALUES ('{values[0]}', '{values[1]}', '{values[2]}', '{values[3]}', {values[4]}, {values[5]});"""
    ejecutor_sql(insert_query)  # Es importante hacer commit para guardar los cambios
    print(f"{values[0]} insertado exitosamente")

"""Voy extrayendo los datos en formato tupla de cada fila del DataFrame y haciendo la inserción."""

for index, row in municipios_espana.iterrows():
    nombre = row['Población']
    provincia = row['Provincia']
    comunidad = row['Comunidad']
    cod_postal = row['codigo_postal']
    latitud = row['Latitud']
    longitud = row['Longitud']
    values = (nombre, provincia, comunidad, cod_postal, latitud, longitud)
    insertar_ciudades(values)

!pip install pymysql

# URL de conexión a la base de datos
from sqlalchemy import create_engine
def leer_tabla(tabla):
    config = {
        'user': 'root',  # Usuario
        'password': 'sQGJOjroYvDHdacUUcfqgwnuYrsFqkbv',  # Contraseña
        'host': 'viaduct.proxy.rlwy.net',  # Host público de Railway
        'database': 'railway',  # Nombre de la base de datos
        'port': 17016  # Puerto público de Railway
    }
    db_password = config['password']
    db_host = config['host']
    port = config['port']
    db_url = f"mysql+pymysql://root:{db_password}@{db_host}:{port}/railway"

    # Crear una instancia de motor (engine)
    engine = create_engine(db_url)

    # Realizar una conexión a la base de datos
    try:
        # Intentar conectarse a la base de datos
        connection = engine.connect()
        contenido = pd.read_sql(f"SELECT * FROM {tabla}", connection)
    except Exception as e:
        print(f"Error de conexión: {e}")
    finally:
        # Cerrar la conexión cuando hayas terminado
        if connection:
            connection.close()
        return contenido
leer_tabla("Ciudades")

"""## Creacion Tipo_cliente"""

creacion_tabla = """
    CREATE TABLE Tipos_cliente (
    tipo_cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    clase VARCHAR(1) NOT NULL,
    tasa DECIMAL(4, 2),
    num_prestamos INT,
    dias_max_prestamo INT
    );"""
insercion_datos = """
    INSERT INTO Tipos_cliente (clase, tasa, num_prestamos, dias_max_prestamo)
    VALUES ("1", 10.5, 3, 3),("2", 15.0, 5, 5),("3", 25.0, 7, 15);
    """
ejecutor_sql(creacion_tabla)
ejecutor_sql(insercion_datos)

leer_tabla("Tipos_cliente")

"""## Creación e inserción de datos en Clientes"""

sql_crea_tabla = """
-- Tabla Clientes
CREATE TABLE Clientes (
cliente_id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
apellidos VARCHAR(100) NOT NULL,
telefono VARCHAR(15),
dni VARCHAR(20) UNIQUE NOT NULL,
correo_e VARCHAR(100) NOT NULL,
direccion TEXT,
ciudad INT,
fecha_nacimiento DATE,
tipo_cliente INT,
password VARCHAR(255) NOT NULL,
FOREIGN KEY (ciudad) REFERENCES Ciudades(ciudad_id),
FOREIGN KEY (tipo_cliente) REFERENCES Tipos_cliente(tipo_cliente_id)
);"""
sql_inserta_datos = """INSERT INTO Clientes (nombre, apellidos, telefono, dni, correo_e, direccion, ciudad, fecha_nacimiento, tipo_cliente, password)
VALUES
('Carlos', 'García López', '123456789', '12345678A', 'carlos.garcia@example.com', 'Calle Mayor, 10', 1, '1985-06-15', 1, 'password123'),
('María', 'Fernández Ruiz', '987654321', '87654321B', 'maria.fernandez@example.com', 'Avenida del Sol, 22', 2, '1990-12-05', 2, 'securepassword'),
('Juan', 'Martínez Pérez', '555555555', '11223344C', 'juan.martinez@example.com', 'Plaza de España, 7', 3, '1982-03-28', 1, 'mypassword123'),
('Laura', 'Hernández Gómez', '444444444', '55667788D', 'laura.hernandez@example.com', 'Calle Luna, 15', 1, '1995-07-22', 3, 'laurapass'),
('Sergio', 'Jiménez Ortiz', '666777888', '66778899E', 'sergio.jimenez@example.com', 'Paseo de la Castellana, 30', 2, '1988-11-02', 1, 'sergiopass'),
('Ana', 'Díaz Morales', '777888999', '77889900F', 'ana.diaz@example.com', 'Calle Nueva, 18', 3, '1992-09-14', 2, 'anapass123'),
('Luis', 'Sánchez Torres', '888999000', '88990011G', 'luis.sanchez@example.com', 'Calle Real, 12', 1, '1987-02-19', 3, 'luissecure'),
('Marta', 'Romero Castro', '999000111', '99001122H', 'marta.romero@example.com', 'Camino del Río, 9', 2, '1993-05-06', 2, 'martapass2023'),
('Javier', 'López Vargas', '000111222', '00112233I', 'javier.lopez@example.com', 'Calle Jardines, 45', 3, '1980-08-11', 1, 'javiervault'),
('Elena', 'González Flores', '111222333', '11223344J', 'elena.gonzalez@example.com', 'Calle Princesa, 8', 1, '1998-04-30', 2, 'elenasecret');
"""
ejecutor_sql(sql_crea_tabla)
ejecutor_sql(sql_inserta_datos)

leer_tabla("Clientes")

"""## Inserción de datos de Películas

### Obtención de los datos
"""

peliculas = pd.read_csv("https://github.com/LearnDataSci/articles/raw/refs/heads/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv")

peliculas.columns

years = [2014, 2015, 2016]
peliculas_nuevas = peliculas[peliculas['Year'].isin(years)]

peliculas_nuevas.reset_index(drop=True, inplace=True)

peliculas_nuevas.reset_index(drop=False, inplace=True)

peliculas_nuevas.rename(columns={'index': 'pelicula_id'}, inplace=True)

peliculas_nuevas

"""### Primero necesito crear la tabla `Peliculas` en la base de datos"""

ejecutor_sql("""-- Tabla Peliculas
CREATE TABLE Peliculas (
pelicula_id INT AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(255) NOT NULL,
anio YEAR,
duracion INT,
pais VARCHAR(100),
director VARCHAR(100),
nota DECIMAL(3, 1),
referencia VARCHAR(255),
enlace TEXT
);""")

"""La tabla está creada, pero vacía"""

leer_tabla("Peliculas")

"""Vamos a mejorar el ejecutor_sql para que admita parametros y devuelva datos al hacer SELECT"""

config = {
    'user': 'root',  # Usuario
    'password': 'sQGJOjroYvDHdacUUcfqgwnuYrsFqkbv',  # Contraseña
    'host': 'viaduct.proxy.rlwy.net',  # Host público de Railway
    'database': 'railway',  # Nombre de la base de datos
    'port': 17016  # Puerto público de Railway
}
def ejecutor_sql(codigo_sql, config, params=None, return_results=False):
    import mysql.connector
    import pandas as pd

    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Ejecutar la consulta
        if params:
            cursor.execute(codigo_sql, params)  # Consulta parametrizada
        else:
            cursor.execute(codigo_sql)  # Consulta sin parámetros

        # Si es una consulta de selección y se solicitan resultados
        if return_results and codigo_sql.strip().upper().startswith("SELECT"):
            # Obtener los resultados
            results = cursor.fetchall()
            # Convertir a DataFrame de Pandas (opcional)
            columns = [col[0] for col in cursor.description]  # Obtener nombres de columnas
            df = pd.DataFrame(results, columns=columns)
            return df
        else:
            # Confirmar la transacción para consultas que no son SELECT
            connection.commit()
            print("✅ Ejecución correcta de SQL")

    except mysql.connector.Error as e:
        print(f"❌ Error de MySQL: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("🔗 Conexión cerrada")

# Insertar datos de ciudades
def insertar_peliculas(values):
    insert_query = f"""INSERT INTO Peliculas (titulo, anio, duracion, pais, director, nota, referencia, enlace)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
    ejecutor_sql(insert_query, config, params = values)  # Es importante hacer commit para guardar los cambios
    print(f"{values[0]} insertado exitosamente")

peliculas_nuevas.columns

for index, row in peliculas_nuevas.iterrows():
    titulo = row['Title']
    anio = row['Year']
    duracion = row['Runtime (Minutes)']
    pais = "Desconocido"
    director = row['Director']
    nota = row['Rating']
    referencia = row['Description']
    enlace = row['Actors']
    values = (titulo, anio, duracion, pais, director, nota, referencia, enlace)
    insertar_peliculas(values)

leer_tabla("Peliculas")

tabla_peliculas = ejecutor_sql("SELECT * FROM Peliculas;", config, return_results=True)
tabla_peliculas

creacion_copias = """
CREATE TABLE Copias (
copia_id INT AUTO_INCREMENT PRIMARY KEY,
pelicula INT,
pasillo VARCHAR(20),
estanteria VARCHAR(20),
FOREIGN KEY (pelicula) REFERENCES Peliculas(pelicula_id)
);"""
insercion_copias = """
INSERT INTO Copias (pelicula, pasillo, estanteria)
VALUES
(1, '1', 'A'),
(2, '2', 'B'),
(3, '4', 'C'),
(3, '2', 'C'),
(2, '3', 'B'),
(5, '1', 'A'),
(6, '4', 'C'),
(7, '4', 'B'),
(8, '5', 'C'),
(6, '1', 'A');
"""
ejecutor_sql(creacion_copias, config)
ejecutor_sql(insercion_copias, config)

creacion_prestamos = """
-- Tabla Préstamos
CREATE TABLE Prestamos (
prestamo_id INT AUTO_INCREMENT PRIMARY KEY,
copia INT,
cliente INT,
fecha_prestamo DATE,
fecha_devolucion DATE,
FOREIGN KEY (copia) REFERENCES Copias(copia_id),
FOREIGN KEY (cliente) REFERENCES Clientes(cliente_id)
);
"""
insercion_prestamos = """INSERT INTO Prestamos (copia, cliente, fecha_prestamo, fecha_devolucion)
VALUES
(1, 1, '2025-01-01', '2025-01-15'),
(2, 2, '2025-01-05', '2025-01-20'),
(3, 3, '2025-01-10', NULL),
(4, 4, '2025-01-15', '2025-01-30'),
(5, 5, '2025-01-18', NULL),
(6, 6, '2025-01-20', '2025-02-01'),
(7, 7, '2025-01-25', '2025-02-05'),
(8, 8, '2025-01-27', NULL),
(9, 9, '2025-01-29', NULL),
(10, 10, '2025-01-30', NULL);"""
ejecutor_sql(creacion_prestamos, config)
ejecutor_sql(insercion_prestamos, config)

leer_tabla("Prestamos")

