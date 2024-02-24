from collections import defaultdict
import json
from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def getMaterialesPorUsuario():
    try:
        conn = db.connection()
        cursor = conn.cursor()

        # Consulta SQL para contar los materiales por usuario
        inst = '''
                SELECT CONCAT(US.nombre, ' ', US.aPaterno, ' (', US.idUsuario, ')'), COUNT(CM.idmaterial) AS cantidad_materiales
                    FROM usuariocoleccion UC, usuario US, coleccionMaterial CM
                    WHERE US.idUsuario = UC.idUsuario
                        AND UC.idColeccion = CM.idColeccion
                    GROUP BY US.idusuario; -- Ordenar por código del usuario ascendente
               '''
        cursor.execute(inst)
        resultados = cursor.fetchall()

        # Convertir los resultados a una lista de diccionarios
        lista = [{"name": str(row[0]), "y": row[1]} for row in resultados]

        # Convertir la lista a JSON
        materiales_por_usuario_json = lista

        conn.close()
        return materiales_por_usuario_json
    except Exception as e:
        print("(SISTEMA) Error: " + str(e))

