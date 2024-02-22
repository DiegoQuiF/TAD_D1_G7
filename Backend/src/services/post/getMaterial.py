from ...database.db import DatabaseManager
from src.models.material import Material

db = DatabaseManager().getInstancia()

def getMaterial(id):
    try:
        print('      [Solicitud] Realizando conexión con la base de datos...')
        conn = db.connection()
        materiales = []
        inst =  '''
                SELECT MA.idMaterial, MA.titulo, MA.autor, TO_CHAR(MA.fecha, 'DD-MM-YYYY'), MA.idioma,
                        MA.procedencia, MA.dispFisico, MA.precioFisico, MA.stockFisico, MA.dispElec, MA.precioElec, CM.idColeccion
                    FROM Material MA, ColeccionMaterial CM, UsuarioColeccion UC
                    WHERE MA.idMaterial = CM.idMaterial
                        AND	CM.idColeccion = UC.idColeccion
                        AND UC.idUsuario = %(id)s
	                ORDER BY MA.idMaterial;
                '''
        with conn.cursor() as cursor:
            print('      [Solicitud] Ejecutando consulta...')
            cursor.execute(inst, {'id': id})
            for row in cursor.fetchall():
                material = Material(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                material.idMaterial = row[0]
                materiales.append(material.to_json())
            conn.commit()
            cursor.close()
        
        return materiales
    except Exception as e:
        print('      [Solicitud] Error de lógica interna:', e)
        return None