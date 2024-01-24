from src.database.db import connection
from src.models.material import Material

def getMaterial(id):
    try:
        print('      [Solicitud] Realizando conexión con la base de datos...')
        conn = connection()
        materiales = []
        inst =  '''
                SELECT idMaterial, nombreMaterial, autorMaterial, TO_CHAR(fechaPubMaterial, 'DD-MM-YYYY'), idiomaMaterial,
                        procedenciaMaterial, TO_CHAR(fechaPubOrigMaterial, 'DD-MM-YYYY'), electronicoMaterial, precioEMaterial,
                        fisicoMaterial, precioFMaterial, stockMaterial
                    FROM MaterialBibliografico
                    WHERE idMaterial in (SELECT idMaterial FROM coleccionMaterial WHERE idColeccion = %(id)s)
                '''
        with conn.cursor() as cursor:
            print('      [Validación] Ejecutando consulta...')
            cursor.execute(inst, {'id': id})
            for row in cursor.fetchall():
                material = Material(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                material.idMat = row[0]
                materiales.append(material.to_json())
            conn.commit()
            cursor.close()
        
        return materiales
    except Exception as e:
        print('      [Validación] Error de lógica interna:', e)
        return None