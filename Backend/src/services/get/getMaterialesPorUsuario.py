from collections import defaultdict
import json
from ...database.db import DatabaseManager
from ...database.db_wh import DatabaseManager_wh

db = DatabaseManager().getInstancia()
db_wh = DatabaseManager_wh().getInstancia()

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

        # INICIAMOS LA CONEXIÓN EN LA DWH
        conn_wh = db_wh.connection()
        cursor_wh = conn_wh.cursor()

        # Limpiar la tabla metrica2 antes de la actualización
        cursor_wh.execute('DELETE FROM metrica2')

        # Resetear el contador de la secuencia a 1
        cursor_wh.execute('ALTER SEQUENCE metrica2_id_seq RESTART WITH 1')

        # Insertar los datos de materiales_por_usuario_json en la tabla metrica2
        for dato in materiales_por_usuario_json:
            name = dato["name"]
            cantidad_materiales = dato["y"]
            insert_query = f'''
                INSERT INTO metrica2 (name, cantidad_materiales)
                VALUES ('{name}', {cantidad_materiales});
            '''
            cursor_wh.execute(insert_query)

        # Confirmar la transacción y cerrar la conexión de la bd de la data warehouse
        conn_wh.commit()
        cursor_wh.close()
        conn_wh.close()

        #Cerramos la conexión de la bd principal
        conn.close()
        return materiales_por_usuario_json
    except Exception as e:
        print("(SISTEMA) Error: " + str(e))

