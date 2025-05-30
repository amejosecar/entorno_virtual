# borrar_esquema.py

from conecion import ejecutor_sql

# Lista de sentencias DROP TABLE en el orden correcto
drop_statements = [
    "DROP TABLE IF EXISTS prestamos;",
    "DROP TABLE IF EXISTS libro;",
    "DROP TABLE IF EXISTS revista;",
    "DROP TABLE IF EXISTS dvd;",
    "DROP TABLE IF EXISTS usuarios;",
    "DROP TABLE IF EXISTS material_biblioteca;"
]

def borrar_esquema():
    for statement in drop_statements:
        print("Ejecutando sentencia SQL:")
        print(statement)
        ejecutor_sql(statement)
        print("-" * 60)

if __name__ == '__main__':
    borrar_esquema()
