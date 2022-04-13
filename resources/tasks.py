"""
    ! ---- Importación de librerías ---- 
    @param flask: Trabajar con el framework Web y todos los beneficios 
    @param request: Trabajamos con solicitudes en la web
    @param jsonify: Trabajamos con formato JSON
    @param Blueprint: Trabajar con el diseño y arquitectura de flask
    @param datetime: Tendremos la fecha del sistema en diferentes formatos 
"""

from flask import request, jsonify, Blueprint
from datetime import datetime

from database import tasks


tasks_bp = Blueprint('routes-tasks', __name__) # <-- Dar diseño a la ruta

@tasks_bp.route('/tasks', methods=['POST']) # <-- Trabajar con POST
def add_task(): # <-- Registrar tarea
    title = request.json['title'] # <-- Pasar por parametro JSON el titulo de la tarea
    created_date = datetime.now().strftime("%x") # <-- Da formato de fecha tipo 5/13/2022

    data = (title, created_date) # <-- Crear el titulo y fecha
    task_id = tasks.insert_task(data) # <-- Insertar la tarea por id

    if task_id:
        task = tasks.select_task_by_id(task_id) # <-- Si existe la tarea no se agregara
        return jsonify(task)

    return jsonify({'mensaje': 'Error Interno'})


@tasks_bp.route('/tasks', methods=['GET']) # <-- Trabajar con GET
def get_tasks(): # <-- Obtener tareas 
    data = tasks.select_all_tasks() # <-- seleccionamos todas las tareas

    if data:
        return jsonify({'tasks': data}) # <-- Enseñamos las tareas
    elif data == False:
        return jsonify({'mensaje': 'Error Interno'}) # <-- Mostramos en caso de error
    else:
        return jsonify({'tasks': {}}) # <-- Mostramos la información de las tareas

@tasks_bp.route('/tasks', methods=['PUT']) # <-- Trabajar con PUT
def update_task(): # <-- Actualizar tarea
    title = request.json['title'] # <-- Pasamos el titulo de la tarea
    id_arg = request.args.get('id') # <-- Pasamos el id de la tarea a actualizar

    if tasks.update_task(id_arg, (title,)): 
        task = tasks.select_task_by_id(id_arg) # <-- Actualizamos la tarea por el id
        return jsonify(task)
    return jsonify({'mensaje': 'Error Interno'}) # <-- En caso de error mostramos

@tasks_bp.route('/tasks', methods=['DELETE']) # <-- Trabajamos con DELETE
def delete_task(): # <-- Eliminar tarea
    id_arg = request.args.get('id') # <-- Pasamos el id de la tarea a eliminar

    if tasks.delete_task(id_arg):
        return jsonify({'mensaje': 'Tarea Eliminada'}) # <-- Mostramos la tarea eliminada
    return jsonify({'mensaje': 'Error Interno'}) # <-- En caso de error mostramos


@tasks_bp.route('/tasks/completed', methods=['PUT']) # Trabajamos con PUT
def complete_task(): # <-- Completamos tarea
    id_arg = request.args.get('id') # <-- Pasamos el id de la tarea
    completed = request.args.get('completed') # <-- Pasamos tarea completada

    if tasks.complete_task(id_arg, completed):
        return jsonify({'mensaje': 'Tarea completada'}) # <-- Mostramos tarea completada
    return jsonify({'mensaje': 'Error Interno'}) # <-- En caso de error mostramos 
