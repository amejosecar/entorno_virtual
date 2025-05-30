# DataSet.py
# -*- coding: utf-8 -*-

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
        """Ejecuta una sentencia SELECT."""
        sql = f"SELECT * FROM {tabla}"
        if condiciones:
            filtros = " AND ".join(f"{col}='{val}'" for col, val in condiciones.items())
            sql += f" WHERE {filtros}"
        return ejecutor_sql(sql)

    def actualizar(self, tabla, cambios, condiciones):
        """Ejecuta una sentencia UPDATE."""
        cambios_sql = ", ".join(f"{col}='{val}'" for col, val in cambios.items())
        condiciones_sql = " AND ".join(f"{col}='{val}'" for col, val in condiciones.items())
        sql = f"UPDATE {tabla} SET {cambios_sql} WHERE {condiciones_sql};"
        return ejecutor_sql(sql)

    def eliminar(self, tabla, condiciones):
        """Ejecuta una sentencia DELETE."""
        condiciones_sql = " AND ".join(f"{col}='{val}'" for col, val in condiciones.items())
        sql = f"DELETE FROM {tabla} WHERE {condiciones_sql};"
        return ejecutor_sql(sql)
