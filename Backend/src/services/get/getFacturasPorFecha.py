from collections import defaultdict
import json
from ...database.db import DatabaseManager


db = DatabaseManager().getInstancia()

def getFacturasPorFecha():
    try:
        conn = db.connection()
        cursor = conn.cursor()

        # Consulta SQL para obtener la fecha de compra y contar las facturas por fecha
        inst = '''
                SELECT fechacompra FROM factura
                ORDER BY fechacompra; -- Ordenar por fecha de compra ascendente
               '''
        with conn.cursor() as cursor:
            cursor.execute(inst)
            fechas = cursor.fetchall()
            
            # Contar el número de facturas por fecha de compra
            conteo_facturas = defaultdict(int)
            for fecha in fechas:
                fecha_formateada = fecha[0].strftime('%d/%m/%Y')  # Convertir la fecha a formato DD/MM/YYYY
                conteo_facturas[fecha_formateada] += 1

            # Crear la lista con las fechas y la cantidad de facturas
            lista = [{"fechacompra": fecha, "cantidad_facturas": cantidad} for fecha, cantidad in conteo_facturas.items()]

            # Convertir la lista a JSON
            facturas_por_fecha_json = json.dumps(lista)

        conn.close()
        return facturas_por_fecha_json
    except Exception as e:
        print("(SISTEMA) Error: " + str(e))
