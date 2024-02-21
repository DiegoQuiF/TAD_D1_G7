from ...database.db import DatabaseManager
from src.models.comprador import Comprador

db = DatabaseManager().getInstancia()

def getCompradores(id):
    try:
        print('      [Solicitud] Realizando conexión con la base de datos'.ljust(120, '.'))
        conn = db.connection()
        compradores = []
        inst =  '''
                SELECT US.idUsuario, CONCAT(US.nombre, ' ', US.aPaterno, ' ', US.aMaterno) as comprador,
                    TO_CHAR(FA.fechaCompra, 'DD-MM-YYYY'), TO_CHAR(FA.fechaEntrega, 'DD-MM-YYYY'), 0.7*FA.subtotal as subtotal,
                    MA.titulo, CO.nombre as catalogo
                    FROM Usuario US, usuarioFactura UF, factura FA, MaterialFactura MF,
                        ColeccionMaterial CM, UsuarioColeccion UC, Material MA,
                        Coleccion CO
                    WHERE US.idUsuario = UF.idUsuario
                        AND UF.idFactura = FA.idFactura
                        AND FA.idFactura = MF.idFactura
                        AND MF.idMaterial = CM.idMaterial
                        AND CM.idColeccion = UC.idColeccion
                        AND MA.idMaterial = MF.idMaterial
                        AND CO.idColeccion = CM.idColeccion
                        AND UC.idUsuario = %(id)s;
                '''
        
        print('      [Solicitud] Ejecutando consulta'.ljust(120, '.'))
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id': id})
            for row in cursor.fetchall():
                comprador = Comprador(row[1], row[2], row[3], row[4], row[5], row[6])
                comprador.idUsuario = row[0];
                compradores.append(comprador.to_json())
            conn.commit()
            cursor.close()
        conn.close()
        
        return compradores
    except Exception as e:
        print('      [Solicitud] Error de lógica interna:', e)
        return None
    