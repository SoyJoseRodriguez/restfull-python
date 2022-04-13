"""
    ! ---- Importación de librerías ---- 
    @param sqlite3: Trabajar con el gestor de bases de datos
    @param Error: Trabajar con los errores que se presenten en el gestor SQLite
"""

import sqlite3
from sqlite3 import Error

"""
    ! ---- Trabajar con archivos ---- 
    @param connection: Trabajar con el archivo de connection
    @param create_connection: Trabajar con la función de conexión a la base de datos
"""

from .connection import create_connection


def read_file(path): # <-- Para leer un archivo
    with open(path, "r") as sql_file: # <-- Para abrir el archivo
        return sql_file.read()

def create_tables(): # <-- Para crear las tablas
    conn = create_connection() # <-- crear la conexión 

    path = "database/sql/tables.sql" # <-- Ruta para leer el archivo

    sql = read_file(path) # <-- Leer el archivo
  
    try:
        cur = conn.cursor() # <-- Crear el cursor
        cur.execute(sql) # <-- ejecutar sql
        conn.commit() # <-- verificar el sql
        return True

    except Error as e:
        print(f"Error al crear la tabla: {e}") # <-- Mostrar en caso de error
        return False
    finally:
        if conn:
            cur.close() # <-- cerrar cursor
            conn.close() # <-- cerrar conexión 