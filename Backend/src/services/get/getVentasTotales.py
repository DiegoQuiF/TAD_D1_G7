from collections import defaultdict
import json
from ...database.db import DatabaseManager


db = DatabaseManager().getInstancia()

def getVentasTotales():
    try:
        conn = db.connection()
        cursor = conn.cursor()

        # EXTRACCIÓN

        # Consulta SQL para obtener el año de publicación y contar los materiales por año
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
            # Contar el número de materiales subidos por año
            conteo_ventas = defaultdict(int)
            for id in ids:
                conteo_ventas[id] += 1

            # Crear la lista con los años y la cantidad de materiales
            lista = [{"Id": id[0], "Ventas": cantidad} for id, cantidad in conteo_ventas.items()]

            # Convertir la lista a JSON
            ventas_por_usuario = lista
        
        # CARGA
        # Agregar carga en una nueva BD

        conn.close()
        return ventas_por_usuario
    except Exception as e:
        print("(SISTEMA) Error: " + str(e))