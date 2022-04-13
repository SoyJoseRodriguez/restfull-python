"""
    ! ---- Importación de librerías ---- 
    @param flask: Trabajar con el framework Web y todos los beneficios 
"""
from flask import Flask
#from flask_cors import CORS

"""
    ! ---- Importación de Archivos ---- 
    @param database: Carpeta donde se encuentra todo lo relacionado a la base de datos
    @param setup: Archivo donde están todas las configuraciones del proyecto
    @param resources.tasks: Carpeta y Archivo donde se encuentran todos los metodos a usar  
    @param tasks_bd: Base de datos que almacenara la información de las tareas 
"""

from database import setup
from resources.tasks import tasks_bp

app = Flask(__name__) # <-- el objeto con el que trabajaremos en el proyecto
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
setup.create_tables() # <-- de el archivo de configuración crearemos la tabla tasks con la que estaremos trabajando


@app.before_first_request # <-- Trabajar con los request de 
def create_tables():
    setup.create_tables()


app.register_blueprint(tasks_bp)


if __name__ == '__main__':
    app.run(debug=True)
