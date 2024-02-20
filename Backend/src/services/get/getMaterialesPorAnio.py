from collections import defaultdict
import json
from ...database.db import DatabaseManager


db = DatabaseManager().getInstancia()

def getMaterialesPorAnio():
    try:
        conn = db.connection()
        cursor = conn.cursor()

        # Consulta SQL para obtener el año de publicación y contar los materiales por año
        inst = '''
                SELECT EXTRACT(YEAR FROM fecha) AS year FROM Material
                ORDER BY year; -- Ordenar por año ascendente
               '''
        with conn.cursor() as cursor:
            cursor.execute(inst)
            anios = cursor.fetchall()
            
            # Contar el número de materiales subidos por año
            conteo_materiales = defaultdict(int)
            for anio in anios:
                anio_formateado = int(anio[0])  # Convertir el año a entero
                conteo_materiales[anio_formateado] += 1

            # Crear la lista con los años y la cantidad de materiales
            lista = [{"anio": anio, "cantidad_materiales": cantidad} for anio, cantidad in conteo_materiales.items()]

            # Convertir la lista a JSON
            materiales_por_fecha_json = json.dumps(lista)

        conn.close()
        return materiales_por_fecha_json
    except Exception as e:
        print("(SISTEMA) Error: " + str(e))

