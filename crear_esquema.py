# crear_esquema.py

from conecion import ejecutor_sql

# Lista de sentencias SQL para crear las tablas
sql_statements = [
    """
    CREATE TABLE material_biblioteca (
        codigo_inventario VARCHAR(50) PRIMARY KEY,
        titulo            VARCHAR(255) NOT NULL,
        autor             VARCHAR(255) NOT NULL,
        ubicacion         VARCHAR(255),
        disponible        BOOLEAN NOT NULL DEFAULT TRUE,
        tipo_material     VARCHAR(50) NOT NULL  -- Por ejemplo: 'Libro', 'Revista', 'DVD'
    );
    """,
    """
    CREATE TABLE libro (
        codigo_inventario VARCHAR(50) PRIMARY KEY,
        isbn              VARCHAR(50),
        numero_paginas    INT,
        editorial         VARCHAR(255),
        fecha_publicacion DATE,
        edicion           VARCHAR(50),
        idioma            VARCHAR(50),
        peso_libro        DECIMAL(10,2),
        formato_libro     VARCHAR(50),
        tipo_literatura   VARCHAR(50),
        resena            TEXT,
        CONSTRAINT fk_libro_material
            FOREIGN KEY (codigo_inventario)
            REFERENCES material_biblioteca(codigo_inventario)
    );
    """,
    """
    CREATE TABLE revista (
        codigo_inventario VARCHAR(50) PRIMARY KEY,
        isbn              VARCHAR(50),
        numero_edicion    INT,
        fecha_publicacion DATE,
        CONSTRAINT fk_revista_material
            FOREIGN KEY (codigo_inventario)
            REFERENCES material_biblioteca(codigo_inventario)
    );
    """,
    """
    CREATE TABLE dvd (
        codigo_inventario VARCHAR(50) PRIMARY KEY,
        isbn              VARCHAR(50),
        duracion          INT,         -- Duración en minutos
        formato           VARCHAR(50),
        CONSTRAINT fk_dvd_material
            FOREIGN KEY (codigo_inventario)
            REFERENCES material_biblioteca(codigo_inventario)
    );
    """,
    # Aquí se modifica la sentencia para usuarios
    """
    CREATE TABLE usuarios (
        usuario_id INT PRIMARY KEY AUTO_INCREMENT,
        nombre       VARCHAR(255) NOT NULL,
        apellido     VARCHAR(255) NOT NULL,
        email        VARCHAR(255) UNIQUE NOT NULL,
        fecha_registro DATE DEFAULT (CURDATE())
    );
    """,
    """
    CREATE TABLE prestamos (
        prestamo_id INT PRIMARY KEY AUTO_INCREMENT,
        codigo_inventario VARCHAR(50) NOT NULL,
        usuario_id       INT NOT NULL,
        fecha_prestamo   DATE NOT NULL,
        fecha_devolucion DATE,  -- Puede ser NULL hasta la devolución
        devuelto         BOOLEAN DEFAULT FALSE,  -- Indica si el préstamo fue devuelto
        CONSTRAINT fk_prestamo_material
            FOREIGN KEY (codigo_inventario)
            REFERENCES material_biblioteca(codigo_inventario),
        CONSTRAINT fk_prestamo_usuario
            FOREIGN KEY (usuario_id)
            REFERENCES usuarios(usuario_id)
    );
    """
]

def crear_esquema():
    for statement in sql_statements:
        print("Ejecutando sentencia SQL:")
        print(statement)
        ejecutor_sql(statement)
        print("-" * 60)
        
if __name__ == '__main__':
    crear_esquema()
    print("Esquema creado con éxito.")