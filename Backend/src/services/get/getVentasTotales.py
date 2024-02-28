from collections import defaultdict
import json
from ...database.db import DatabaseManager
from ...database.db_wh import DatabaseManager_wh

db = DatabaseManager().getInstancia()
db_wh = DatabaseManager_wh().getInstancia()

def getVentasTotales():
    try:
        conn = db.connection()
        cursor = conn.cursor()

        # EXTRACCIÓN

        # Consulta SQL para obtener los IDs de usuario y contar las ventas por usuario
        inst = '''
                SELECT UC.idUsuario FROM usuarioColeccion UC, coleccionMaterial CM, materialFactura MF
                    WHERE UC.idColeccion = CM.idColeccion
                        AND CM.idMaterial = MF.idMaterial
                        ORDER BY UC.idUsuario;
               '''
        with conn.cursor() as cursor:
            cursor.execute(inst)
            ids = cursor.fetchall()
            
            # TRANSFORMACIÓN CONTINUA
            # Contar el número de ventas por usuario
            conteo_ventas = defaultdict(int)
            for id in ids:
                conteo_ventas[id[0]] += 1

            # Crear la lista con los IDs de usuario y la cantidad de ventas
            lista = [{"Id": id_usuario, "Ventas": cantidad} for id_usuario, cantidad in conteo_ventas.items()]

            # Convertir la lista a JSON
            ventas_por_usuario = lista

            # INICIAMOS LA CONEXIÓN EN LA DWH
            conn_wh = db_wh.connection()
            cursor_wh = conn_wh.cursor()

            # Limpiar la tabla metrica4 antes de la actualización
            cursor_wh.execute('DELETE FROM metrica4')

            # Resetear el contador de la secuencia a 1
            cursor_wh.execute('ALTER SEQUENCE metrica4_id_seq RESTART WITH 1')

            # Insertar los datos de ventas_por_usuario en la tabla metrica4
            for dato in ventas_por_usuario:
                usuario_id = dato["Id"]
                ventas = dato["Ventas"]
                insert_query = f'''
                    INSERT INTO metrica4 (usuario_id, ventas)
                    VALUES ({usuario_id}, {ventas});
                '''
                cursor_wh.execute(insert_query)

            # Confirmar la transacción y cerrar la conexión de la bd de la data warehouse
            conn_wh.commit()
            cursor_wh.close()
            conn_wh.close()

        # CERRAMOS LA CONEXIÓN EN LA BD ORIGINAL
        conn.close()

        return ventas_por_usuario
    except Exception as e:
        print("(SISTEMA) Error: " + str(e))