from collections import defaultdict
import json
from ...database.db import DatabaseManager
from ...database.db_wh import DatabaseManager_wh

db = DatabaseManager().getInstancia()
db_wh = DatabaseManager_wh().getInstancia()

def getFacturasPorFecha():
    try:
        conn = db.connection()
        cursor = conn.cursor()

        # Consulta SQL para obtener la fecha de compra y contar las facturas por fecha
        inst = '''
                SELECT fechacompra, COUNT(*) AS cantidad
                FROM factura
                GROUP BY fechacompra
                ORDER BY fechacompra; -- Ordenar por fecha de compra ascendente
               '''
        cursor.execute(inst)
        resultados = cursor.fetchall()

        # Convertir los resultados a una lista de diccionarios
        lista = [{"Fecha": str(row[0]), "Cantidad": row[1]} for row in resultados]

        # Convertir la lista a JSON
        facturas_por_fecha_json = lista

        # INICIAMOS LA CONEXIÓN EN LA DWH
        conn_wh = db_wh.connection()
        cursor_wh = conn_wh.cursor()

        # Limpiar la tabla metrica3 antes de la actualización
        cursor_wh.execute('DELETE FROM metrica3')

        # Resetear el contador de la secuencia a 1
        cursor_wh.execute('ALTER SEQUENCE metrica3_id_seq RESTART WITH 1')

        # Insertar los datos de facturas_por_fecha_json en la tabla metrica3
        for dato in facturas_por_fecha_json:
            fecha = dato["Fecha"]
            cantidad = dato["Cantidad"]
            insert_query = f'''
                INSERT INTO metrica3 (fecha, cantidad)
                VALUES ('{fecha}', {cantidad});
            '''
            cursor_wh.execute(insert_query)

        # Confirmar la transacción y cerrar la conexión de la bd de la data warehouse
        conn_wh.commit()
        cursor_wh.close()
        conn_wh.close()

        conn.close()
        return facturas_por_fecha_json
    except Exception as e:
        print("(SISTEMA) Error: " + str(e))
