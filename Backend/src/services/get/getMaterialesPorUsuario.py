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
                SELECT uc.idusuario, COUNT(cm.idmaterial) AS cantidad_materiales
                FROM usuariocoleccion uc
                JOIN coleccionmaterial cm ON uc.idcoleccion = cm.idcoleccion
                GROUP BY uc.idusuario
                ORDER BY uc.idusuario; -- Ordenar por código del usuario ascendente
               '''
        cursor.execute(inst)
        resultados = cursor.fetchall()

        # Convertir los resultados a una lista de diccionarios
        lista = [{"idusuario": row[0], "cantidad_materiales": row[1]} for row in resultados]

        # Convertir la lista a JSON
        materiales_por_usuario_json = json.dumps(lista)

        conn.close()
        return materiales_por_usuario_json
    except Exception as e:
        print("(SISTEMA) Error: " + str(e))

