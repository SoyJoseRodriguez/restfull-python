"""
    ! ---- Importación de librerías ---- 
    @param sqlite3: Trabajar con el gestor de bases de datos
    @param Error: Trabajar con los errores que se presenten en el gestor SQLite
"""

import sqlite3
from sqlite3 import Error


def create_connection(): # <-- Para crear la conexion de la base de datos
    conn = None # <-- Crear la bariable conexión

    try:
        conn = sqlite3.connect("database/tasks.db") # <-- Crear la conexión 
    except Error as e:
        print(f"Error al conectar a la base de datos {e}") # <-- Mostrar en caso de error
    return conn