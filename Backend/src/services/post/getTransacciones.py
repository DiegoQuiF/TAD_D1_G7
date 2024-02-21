from ...database.db import DatabaseManager
from src.models.transaccion import Transaccion

db = DatabaseManager().getInstancia()

def getTransacciones(id):
    try:
        print('      [Solicitud] Realizando conexión con la base de datos'.ljust(120, '.'))
        conn = db.connection()
        transacciones = []
        inst =  '''
                SELECT
                    (SELECT COUNT(CM.*) 
                        FROM ColeccionMaterial CM
                            INNER JOIN Material MB ON CM.idMaterial = MB.idMaterial
                                WHERE CM.idColeccion IN (SELECT UC.idColeccion FROM UsuarioColeccion UC
                                    WHERE UC.idUsuario = %(id)s)) AS publicaciones,
                    
                    (SELECT COUNT(MF.*) 
                        FROM MaterialFactura MF
                            WHERE MF.idMaterial IN (SELECT idMaterial FROM ColeccionMaterial
                                WHERE idColeccion IN (SELECT idColeccion FROM UsuarioColeccion
                                    WHERE idUsuario = %(id)s))) AS compras,
                    
                    COALESCE((SELECT 0.7 * SUM(COALESCE(FA.subtotal, 0)) FROM Factura FA
                        INNER JOIN MaterialFactura MF ON FA.idFactura = MF.idFactura
                            WHERE MF.idMaterial IN (SELECT idMaterial FROM ColeccionMaterial
                                WHERE idColeccion IN (SELECT idColeccion FROM UsuarioColeccion
                                    WHERE idUsuario = %(id)s))), 0) AS recaudado;
                '''
        
        print('      [Solicitud] Ejecutando consulta...')
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id': id})
            for row in cursor.fetchall():
                transaccion = Transaccion(row[0], row[1], row[2])
                transacciones.append(transaccion.to_json())
            conn.commit()
            cursor.close()
        conn.close()
        
        return transacciones
    except Exception as e:
        print('      [Validación] Error de lógica interna:', e)
        return None
    