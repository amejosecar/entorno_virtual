# SiGesBi.py
# Sistema de Gestión de Biblioteca
# -*- coding: utf-8 -*-
#
# Descripción:
#
# Crea un sistema para gestionar una biblioteca. El sistema debe permitir la gestión de diferentes
# tipos de materiales (libros, revistas, DVDs) mediante inserciones en la base de datos.
# Se reemplaza el manejo de archivo PKL por operaciones directas a la BD.

import time
import os

# Importamos las clases que representan los materiales
from biblioteca import Libro, Revista, DVD
from validar_campo import validate_string, validate_date, validate_integer, validate_float
# Importamos funciones de conexión a la BD desde conecion.py
from conecion import ejecutor_sql, leer_tabla, validar_conexion_bd
# Importamos las funciones del gestor de esquema
from crear_esquema import crear_esquema
from borrar_esquema import borrar_esquema
from DataSet      import DataSet
from datetime import datetime

# Función auxiliar para solicitar y validar datos.
def input_validated(prompt: str, validation_function, field_name: str, **kwargs):
    """
    Solicita un dato al usuario, lo valida con la función indicada y lo retorna
    cuando el dato es válido.
    """
    while True:
        value = input(prompt)
        try:
            validated_value = validation_function(value, field_name, **kwargs)
            return validated_value
        except ValueError as e:
            print(e)

def agregar_material():
    print("\nSeleccione el tipo de material a agregar:")
    print("1. Libro")
    print("2. Revista")
    print("3. DVD")
    opcion = input("Ingrese la opción (1/2/3): ")

    if opcion == "1":
       
        # Datos comunes para Libro: usar validate_integer con max_digits=6 para el código
        codigo = input_validated("Ingrese el código de inventario: ", validate_integer, "Código de inventario", max_digits=6)
        titulo = input_validated("Ingrese el título: ", validate_string, "Título")
        autor = input_validated("Ingrese el autor: ", validate_string, "Autor", allow_digits=False)
        #codigo = input_validated("Ingrese el código de inventario: ", validate_integer, "Código de inventario")
        ubicacion = input_validated("Ingrese la ubicación: ", validate_string, "Ubicación")
        disponible = True
        # Datos específicos para Libro
        numero_paginas = input_validated("Ingrese el número de páginas: ", validate_integer, "Número de páginas")
        isbn = input_validated("Ingrese el ISBN: ", validate_integer, "ISBN")
        editorial = input_validated("Ingrese la editorial: ", validate_string, "Editorial", allow_digits=False)
        fecha_input = input_validated("Ingrese la fecha de publicación (dd/mm/aaaa): ",
                                      validate_date, "Fecha de publicación", date_format="%d/%m/%Y")
        # Convertir la fecha a formato MySQL (yyyy-mm-dd)
        try:
            fecha_publicacion = datetime.strptime(fecha_input, "%d/%m/%Y").strftime("%Y-%m-%d")
        except Exception as e:
            print(f"Error al convertir la fecha: {e}")
            return
        edicion = input_validated("Ingrese la edición: ", validate_integer, "Edición")
        idioma = input_validated("Ingrese el idioma: ", validate_string, "Idioma", allow_digits=False)
        peso_libro = input_validated("Ingrese el peso del producto (grs): ", validate_float, "Peso del libro")
        formato_libro = input_validated("Ingrese el formato del libro (Tapa blanda, Digital, Audiolibro, Tapa dura): ",
                                        validate_string, "Formato del libro", allow_digits=False)
        tipo_literatura = input_validated("Ingrese el tipo de literatura (Novela, Poesía, Teatro, etc.): ",
                                          validate_string, "Tipo de literatura", allow_digits=False)
        resena = input_validated("Ingrese la reseña: ", validate_string, "Reseña")
        
        nuevo_material = Libro(
            titulo, autor, codigo, ubicacion, disponible,
            isbn, numero_paginas, editorial, fecha_publicacion, edicion, 
            idioma, peso_libro, formato_libro, tipo_literatura, resena
        )

        # Enviar los datos al módulo DataSet.py para construcción de la sentencia SQL
        DataSet.insertar(nuevo_material)
        print(f"Material '{nuevo_material.titulo}' enviado a DataSet.py para inserción.")

    

    elif opcion == "2":
        # Datos para Revista
        titulo = input_validated("Ingrese el título: ", validate_string, "Título")
        autor = input_validated("Ingrese el autor: ", validate_string, "Autor", allow_digits=False)
        isbn = input_validated("Ingrese el ISBN: ", validate_string, "ISBN")
        codigo = input_validated("Ingrese el código de inventario: ", validate_string, "Código de inventario")
        numero_edicion = input_validated("Ingrese el número de edición: ", validate_integer, "Número de edición")
        fecha_input = input_validated("Ingrese la fecha de publicación (dd/mm/aaaa): ",
                                      validate_date, "Fecha de publicación", date_format="%d/%m/%Y")
        try:
            fecha_publicacion = datetime.strptime(fecha_input, "%d/%m/%Y").strftime("%Y-%m-%d")
        except Exception as e:
            print(f"Error al convertir la fecha: {e}")
            return

        nuevo_material = Revista(titulo, autor, isbn, codigo, numero_edicion, fecha_publicacion)

        sql_material = f"""
        INSERT INTO material_biblioteca (codigo_inventario, titulo, autor, ubicacion, disponible, tipo_material)
        VALUES ('{codigo}', '{titulo}', '{autor}', '', 1, 'Revista');
        """
        res1 = ejecutor_sql(sql_material)

        sql_revista = f"""
        INSERT INTO revista (codigo_inventario, isbn, numero_edicion, fecha_publicacion)
        VALUES ('{codigo}', '{isbn}', {numero_edicion}, '{fecha_publicacion}');
        """
        res2 = ejecutor_sql(sql_revista)

        if res1 and res2:
            print(f"Material '{nuevo_material.titulo}' agregado a la base de datos.")
        else:
            print(f"❌ Error al agregar el material '{nuevo_material.titulo}' a la base de datos.")

    elif opcion == "3":
        # Datos para DVD
        titulo = input_validated("Ingrese el título: ", validate_string, "Título")
        autor = input_validated("Ingrese el autor: ", validate_string, "Autor", allow_digits=False)
        isbn = input_validated("Ingrese el ISBN: ", validate_string, "ISBN")
        codigo = input_validated("Ingrese el código de inventario: ", validate_string, "Código de inventario")
        duracion = input_validated("Ingrese la duración en minutos: ", validate_integer, "Duración")
        formato = input_validated("Ingrese el formato (por ejemplo, DVD, Blu-ray): ", validate_string, "Formato", allow_digits=False)
        
        nuevo_material = DVD(titulo, autor, isbn, codigo, duracion, formato)
        sql_material = f"""
        INSERT INTO material_biblioteca (codigo_inventario, titulo, autor, ubicacion, disponible, tipo_material)
        VALUES ('{codigo}', '{titulo}', '{autor}', '', 1, 'DVD');
        """
        res1 = ejecutor_sql(sql_material)

        sql_dvd = f"""
        INSERT INTO dvd (codigo_inventario, isbn, duracion, formato)
        VALUES ('{codigo}', '{isbn}', {duracion}, '{formato}');
        """
        res2 = ejecutor_sql(sql_dvd)

        if res1 and res2:
            print(f"Material '{nuevo_material.titulo}' agregado a la base de datos.")
        else:
            print(f"❌ Error al agregar el material '{nuevo_material.titulo}' a la base de datos.")
    else:
        print("Opción no válida. Regresando al menú principal.")
        time.sleep(5)
        return

def listar_materiales():
    df = leer_tabla("material_biblioteca")
    if df is not None and not df.empty:
        print("\nMateriales registrados en la base de datos:")
        print(df)
    else:
        print("No se encontraron materiales registrados.")

def mostrar_detalle_material():
    codigo = input_validated("Ingrese el código de inventario: ", validate_integer, "Código de inventario")
    df = leer_tabla("material_biblioteca")
    if df is not None and not df.empty:
        filtro = df[df["codigo_inventario"] == str(codigo)]
        if not filtro.empty:
            print("\nInformación detallada:")
            print(filtro)
        else:
            print("No se encontró ningún material con ese código.")
    else:
        print("No se encontraron materiales en la base de datos.")

# Placeholders para funciones de préstamos y usuarios
def registrar_prestamo():
    print("Función 'registrar_prestamo' no implementada.")
    
def listar_prestamos():
    print("Función 'listar_prestamos' no implementada.")
    
def devolver_material():
    print("Función 'devolver_material' no implementada.")
    
def registrar_usuario():
    print("Función 'registrar_usuario' no implementada.")
    
def listar_usuarios():
    print("Función 'listar_usuarios' no implementada.")
    
def consultar_usuario():
    print("Función 'consultar_usuario' no implementada.")

def menu_gestion_biblioteca():
    while True:
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Agregar nuevo material")
        print("2. Listar todos los materiales")
        print("3. Mostrar información detallada de un material")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_material()
        elif opcion == "2":
            print("Cargando materiales...")
            time.sleep(5)
            listar_materiales()
        elif opcion == "3":
            mostrar_detalle_material()
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        time.sleep(5)

def menu_prestamos():
    while True:
        print("\n--- Menú de Préstamos ---")
        print("1. Registrar nuevo préstamo")
        print("2. Listar préstamos activos")
        print("3. Devolver material")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            listar_prestamos()
        elif opcion == "3":
            devolver_material()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_usuarios():
    while True:
        print("\n--- Menú de Usuarios ---")
        print("1. Registrar nuevo usuario")
        print("2. Listar usuarios")
        print("3. Consultar información de un usuario")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            consultar_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def gestor_de_bd_menu():
    while True:
        print("\n--- Gestor de BD ---")
        print("1. Validar conexión de BD")
        print("2. Crear esquema de BD")
        print("3. Borrar esquema de BD")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            validar_conexion_bd()
        elif opcion == "2":
            crear_esquema()
        elif opcion == "3":
            borrar_esquema()
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        time.sleep(5)

def menu():
    while True:
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Menú de Préstamos")
        print("2. Menú de Gestión de Biblioteca")
        print("3. Menú de Usuarios")
        print("4. Gestor de BD")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_prestamos()
        elif opcion == "2":
            menu_gestion_biblioteca()
        elif opcion == "3":
            menu_usuarios()
        elif opcion == "4":
            gestor_de_bd_menu()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        time.sleep(5)

if __name__ == '__main__':
    menu()
    print("Gracias por usar el Sistema de Gestión de Biblioteca. ¡Hasta pronto!")

