from ...database.db import DatabaseManager
from src.models.materialCompleto import MaterialCompleto

db = DatabaseManager().getInstancia()

def getComprados(id):
    try:
        conn = db.connection()
        materialesCompletos = []
        inst =  '''
                SELECT MB.idMaterial, MB.titulo, MB.autor, TO_CHAR(MB.fecha, 'DD-MM-YYYY') as original, MB.idioma,
                    MB.dispElec, MB.precioElec, MB.dispFisico, MB.precioFisico,
                    CO.idColeccion, CO.nombre, CO.tipo,
                    U.idUsuario, U.nombre, U.aPaterno, U.aMaterno
                    FROM Material MB, ColeccionMaterial CM, Coleccion CO, UsuarioColeccion UC, Usuario U
                    WHERE MB.idMaterial = CM.idMaterial and CM.idColeccion = CO.idColeccion and CO.idColeccion = UC.idColeccion and UC.idUsuario = U.idUsuario
                        and U.idUsuario not in(%(id)s)
                        and MB.idMaterial in (select MF.idMaterial from MaterialFactura MF
                                            WHERE idFactura in (SELECT UF.idFactura from UsuarioFactura UF WHERE UF.idUsuario = %(id)s));
                '''
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id': id})
            for row in cursor.fetchall():
                material = MaterialCompleto(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                material.idMat = row[0]
                materialesCompletos.append(material.to_json())
            conn.commit()
            cursor.close()
        conn.close()
        return materialesCompletos
    except Exception as e:
        print("(SISTEMA)   Error: " + e)
