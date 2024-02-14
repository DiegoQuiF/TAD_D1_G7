from ...database.db import DatabaseManager
from src.models.material import Material

db = DatabaseManager().getInstancia()

def getMaterial(id):
    try:
        print('      [Solicitud] Realizando conexión con la base de datos...')
        conn = db.connection()
        materiales = []
        inst =  '''
                SELECT idMaterial, titulo, autor, TO_CHAR(fecha, 'DD-MM-YYYY'), idioma,
                        procedencia, dispFisico, precioFisico, stockFisico, dispElec, precioElec
                    FROM Material
                    WHERE idMaterial in (SELECT idMaterial FROM coleccionMaterial WHERE idColeccion = %(id)s)
                '''
        with conn.cursor() as cursor:
            print('      [Validación] Ejecutando consulta...')
            cursor.execute(inst, {'id': id})
            for row in cursor.fetchall():
                material = Material(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                material.idMaterial = row[0]
                materiales.append(material.to_json())
            conn.commit()
            cursor.close()
        
        return materiales
    except Exception as e:
        print('      [Validación] Error de lógica interna:', e)
        return None