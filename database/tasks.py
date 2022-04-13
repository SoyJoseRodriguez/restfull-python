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


def insert_task(data): # <-- Insertar tarea 
    conn = create_connection() # <-- Crear la conexion 

    sql = """ INSERT INTO tasks (title, created_date)
             VALUES(?, ?)
    """ # <-- Insertar en la tabla task el titulo y la fecha de la tarea

    try:
        cur = conn.cursor() # <-- Crear cursor
        cur.execute(sql, data) # <-- Ejecutar sql y mandar los datos 
        conn.commit() # <-- Verificar sql
        return cur.lastrowid

    except Error as e:
        print(f"Error al insertar tarea: {e}") # <-- Mostrar en caso de error
        return False
    
    finally:
        if conn:
            cur.close() # <-- Cerrar cursor
            conn.close() # <-- Cerrar conexion

def select_task_by_id(_id): # <-- Para seleccionar tarea por id
    conn = create_connection() # <-- crear conexion
    
    sql = f"SELECT * FROM tasks WHERE id = {_id}" # <-- Seleccionar la tabla tareas y selecciona el id

    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor() # <-- Crear cursor
        cur.execute(sql) # <-- Ejecutar sql
        task = dict(cur.fetchone()) # <-- pasar a diccionario
        return task

    except Error as e:
        print(f"Error al seleccionar tarea por id : {e}") # <-- En caso de error mostrar 
        return False

    finally:
        if conn:
            cur.close() # <-- Cerrar cursor
            conn.close() # <-- Cerrar conexion


def select_all_tasks(): # <-- Para seleccionar todas las tareas
    conn = create_connection() # <-- crear conexion

    sql = "SELECT * FROM tasks" # <-- Seleccionar tabla de tareas

    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor() # <-- Crear cursor 
        cur.execute(sql) # <-- ejecutar sql
        task_rows = cur.fetchall()
        tasks = [ dict(row) for row in task_rows ] # <-- Pasar en un diccionario todas las tareas
        return tasks

    except Error as e:
        print(f"Error al seleccionar todas las tareas: {e}") # <-- Mostrar en caso de error
        return False

    finally:
        if conn:
            cur.close() # <-- Cerrar cursor 
            conn.close() # <-- Cerrar conexion 


def update_task(_id, data): # <-- Para actualizar tarea por id
    conn = create_connection() # <-- Crear la conexion

    sql = f""" UPDATE tasks SET title = ?
             WHERE id = {_id}
    """ # <-- Actualizar la tabla tareas el titulo por el id

    try:
        cur = conn.cursor() # <-- Crear cursor
        cur.execute(sql, data) # <-- ejecutar sql con datos
        conn.commit() # Verificar sql
        return True

    except Error as e:
        print(f"Error al actualizar la tarea : {e}") # <-- En caso de error mostrar
        return False
    
    finally:
        if conn:
            cur.close() # <-- Cerrar cursor
            conn.close() # <-- Cerrar conexion

def delete_task(_id): # <-- Para borrar tarea 
    conn = create_connection() # <-- Crear conexion

    sql = f"DELETE FROM tasks WHERE id = {_id}" # <-- Borrar de la tabla tasks el id

    try:
        cur = conn.cursor() # <-- Crear cursor
        cur.execute(sql) # <-- Ejecutar sql
        conn.commit() # <-- Verificar sql
        return True

    except Error as e:
        print(f"Error al eliminar la tarea {e}") # <-- Mostrar en caso de error 
    
    finally:
        if conn:
            cur.close() # <-- Cerrar cursor
            conn.close() # <-- Cerrar conexion


def complete_task(_id, completed): # <-- Para marcar tarea como completa por id
    conn = create_connection() # <-- crear conexion

    sql = f""" UPDATE tasks SET completed = {completed}
            WHERE id = {_id}
    """ # <-- Actualizar de la tabla tasks el estado de la tarea por id
    try:
        cur = conn.cursor() # <-- Crear cursor
        cur.execute(sql) # <-- Ejecutar sql
        conn.commit() # <-- Verificar sql
        return True

    except Error as e:
        print(f"Error al acompletar la tarea: {e}") # <-- En caso de error mostrar

    finally:
        if conn:
            cur.close() # <-- Cerrar cursor
            conn.close() # <-- Cerrar conexion