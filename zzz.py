# DataSet.py
# -*- coding: utf-8 -*-
#
# Módulo centralizado para ejecutar sentencias SQL: INSERT, SELECT, DELETE, UPDATE.

from conecion import ejecutor_sql

class DataSet:
    def __init__(self):
        pass

    def insertar(self, tabla, datos):
        """Ejecuta una sentencia INSERT con los datos proporcionados."""
        columnas = ", ".join(datos.keys())
        valores = ", ".join(f"'{v}'" for v in datos.values())
        sql = f"INSERT INTO {tabla} ({columnas}) VALUES ({valores});"
        return ejecutor_sql(sql)

    def consultar(self, tabla, condiciones=None):
        """Ejecuta una sentencia SELECT con condiciones opcionales."""
        sql = f"SELECT * FROM {tabla}"
        if condiciones:
            filtros = " AND ".join(f"{col}='{val}'" for col, val in condiciones.items())
            sql += f" WHERE {filtros}"
        return ejecutor_sql(sql)

    def actualizar(self, tabla, cambios, condiciones):
        """Ejecuta una sentencia UPDATE con los cambios y condiciones proporcionados."""
        cambios_sql = ", ".join(f"{col}='{val}'" for col, val in cambios.items())
        condiciones_sql = " AND ".join(f"{col}='{val}'" for col, val in condiciones.items())
        sql = f"UPDATE {tabla} SET {cambios_sql} WHERE {condiciones_sql};"
        return ejecutor_sql(sql)

    def eliminar(self, tabla, condiciones):
        """Ejecuta una sentencia DELETE con las condiciones proporcionadas."""
        condiciones_sql = " AND ".join(f"{col}='{val}'" for col, val in condiciones.items())
        sql = f"DELETE FROM {tabla} WHERE {condiciones_sql};"
        return ejecutor_sql(sql)




# SiGesBi.py
# Sistema de Gestión de Biblioteca usando DataSet.py

import time
import os
from biblioteca import Libro, Revista, DVD
from validar_campo import validate_string, validate_date, validate_integer, validate_float
from conecion import validar_conexion_bd
from datetime import datetime
from DataSet import DataSet

def input_validated(prompt: str, validation_function, field_name: str, **kwargs):
    while True:
        value = input(prompt)
        try:
            return validation_function(value, field_name, **kwargs)
        except ValueError as e:
            print(e)

def agregar_material():
    datos = {
        "codigo_inventario": input_validated("Código de inventario: ", validate_integer, "Código", max_digits=6),
        "titulo": input_validated("Título: ", validate_string, "Título"),
        "autor": input_validated("Autor: ", validate_string, "Autor", allow_digits=False),
        "ubicacion": input_validated("Ubicación: ", validate_string, "Ubicación"),
        "disponible": 1,
        "tipo_material": "Libro",
        "numero_paginas": input_validated("Número de páginas: ", validate_integer, "Número de páginas"),
        "isbn": input_validated("ISBN: ", validate_integer, "ISBN"),
        "editorial": input_validated("Editorial: ", validate_string, "Editorial", allow_digits=False),
        "fecha_publicacion": datetime.strptime(input_validated("Fecha (dd/mm/aaaa): ", validate_date, "Fecha"), "%d/%m/%Y").strftime("%Y-%m-%d"),
        "edicion": input_validated("Edición: ", validate_integer, "Edición"),
        "idioma": input_validated("Idioma: ", validate_string, "Idioma", allow_digits=False),
        "peso_libro": input_validated("Peso del libro (grs): ", validate_float, "Peso del libro"),
        "formato_libro": input_validated("Formato del libro: ", validate_string, "Formato", allow_digits=False),
        "tipo_literatura": input_validated("Tipo de literatura: ", validate_string, "Tipo", allow_digits=False),
        "resena": input_validated("Reseña: ", validate_string, "Reseña")
    }

    dataset = DataSet()
    resultado = dataset.insertar("libros", datos)

    if resultado:
        print(f"✅ Material '{datos['titulo']}' agregado a la base de datos.")
    else:
        print(f"❌ Error al agregar el material '{datos['titulo']}'.")

def listar_materiales():
    dataset = DataSet()
    materiales = dataset.consultar("libros")

    if materiales:
        print("\nMateriales registrados en la base de datos:")
        print(materiales)
    else:
        print("No se encontraron materiales registrados.")

def mostrar_detalle_material():
    codigo = input_validated("Ingrese el código de inventario: ", validate_integer, "Código de inventario")
    dataset = DataSet()
    material = dataset.consultar("libros", {"codigo_inventario": codigo})

    if material:
        print("\nInformación detallada:")
        print(material)
    else:
        print("No se encontró ningún material con ese código.")

def eliminar_material():
    codigo = input_validated("Ingrese el código de inventario a eliminar: ", validate_integer, "Código")
    dataset = DataSet()
    resultado = dataset.eliminar("libros", {"codigo_inventario": codigo})

    if resultado:
        print(f"✅ Material con código {codigo} eliminado correctamente.")
    else:
        print(f"❌ Error al eliminar el material con código {codigo}.")

def actualizar_material():
    codigo = input_validated("Ingrese el código del material a actualizar: ", validate_integer, "Código de inventario")
    campo = input("Ingrese el campo a actualizar: ")
    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")

    dataset = DataSet()
    resultado = dataset.actualizar("libros", {campo: nuevo_valor}, {"codigo_inventario": codigo})

    if resultado:
        print(f"✅ Material actualizado correctamente.")
    else:
        print(f"❌ Error al actualizar el material.")

def menu_gestion_biblioteca():
    while True:
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Agregar nuevo material")
        print("2. Listar todos los materiales")
        print("3. Mostrar información detallada de un material")
        print("4. Eliminar material")
        print("5. Actualizar material")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_material()
        elif opcion == "2":
            listar_materiales()
        elif opcion == "3":
            mostrar_detalle_material()
        elif opcion == "4":
            eliminar_material()
        elif opcion == "5":
            actualizar_material()
        elif opcion == "6":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        time.sleep(2)

if __name__ == '__main__':
    menu_gestion_biblioteca()
