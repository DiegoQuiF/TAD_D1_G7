from collections import defaultdict
import json
from ...database.db import DatabaseManager
from ...database.db_wh import DatabaseManager_wh


db = DatabaseManager().getInstancia()
db_wh = DatabaseManager_wh().getInstancia()
def getMaterialesPorAnio():
    try:
        conn = db.connection()
        cursor = conn.cursor()

        # EXTRACCIÓN

        # Consulta SQL para obtener el año de publicación y contar los materiales por año
        inst = '''
                SELECT EXTRACT(YEAR FROM fecha) AS year FROM Material
                ORDER BY year; -- Ordenar por año ascendente
               '''
        with conn.cursor() as cursor:
            cursor.execute(inst)
            anios = cursor.fetchall()
            
            # TRANSFORMACIÓN CONTINUA
            # Contar el número de materiales subidos por año
            conteo_materiales = defaultdict(int)
            for anio in anios:
                anio_formateado = int(anio[0])  # Convertir el año a entero
                conteo_materiales[anio_formateado] += 1

            # Crear la lista con los años y la cantidad de materiales
            lista = [{"Anio": str(anio), "Total": cantidad} for anio, cantidad in conteo_materiales.items()]

            # Convertir la lista a JSON
            materiales_por_fecha_json = lista

            #INICIAMOS LA CONEXION EN LA DWH
            conn_wh = db_wh.connection()
            cursor_wh = conn_wh.cursor()

            # Limpiar la tabla metrica1 antes de la actualización
            cursor_wh.execute('DELETE FROM metrica1')

            # Resetear el contador de la secuencia a 1
            cursor_wh.execute('ALTER SEQUENCE metrica1_id_seq RESTART WITH 1')

            # Insertar los datos de materiales_por_fecha_json en la tabla metrica1
            for dato in materiales_por_fecha_json:
                anio = dato["Anio"]
                total = dato["Total"]
                insert_query = f'''
                    INSERT INTO metrica1 (anio, total)
                    VALUES ({anio}, {total});
                '''
                cursor_wh.execute(insert_query)


            # Confirmar la transacción y cerrar la conexión de la bd de la data warehouse
            conn_wh.commit()
            cursor_wh.close()
            conn_wh.close()
        #Cerramos la conexion de la primera bd    
        conn.close()
        return materiales_por_fecha_json
    except Exception as e:
        print("(SISTEMA) Error: " + str(e))

