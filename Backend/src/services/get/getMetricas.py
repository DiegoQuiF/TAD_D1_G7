from collections import defaultdict
import json
from ...database.db import DatabaseManager


db = DatabaseManager().getInstancia()

def getMetricas():
    try:
        conn = db.connection()
        metricas = []
        inst =  '''
                SELECT
                    count_usuarios,
                    count_materiales,
                    count_materiales_factura,
                    ROUND(count_materiales_factura::numeric / count_usuarios, 3) AS ratio
                    FROM (
                    SELECT
                        (SELECT COUNT(*) FROM usuario) AS count_usuarios,
                        (SELECT COUNT(*) FROM material) AS count_materiales,
                        (SELECT COUNT(*) FROM materialFactura) AS count_materiales_factura
                    ) AS counts;
                '''
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id': id})
            for row in cursor.fetchall():
                metrica = {'usuarios': row[0], 'materiales':row[1], 'ventas':row[2], 'metrica':row[3]}
                metricas.append(metrica)
            conn.commit()
            cursor.close()
        conn.close()
        return metricas
    except Exception as e:
        print("(SISTEMA)   Error: " + e)