from ...database.db import DatabaseManager
from src.models.coleccion import Coleccion

db = DatabaseManager().getInstancia()

def getColeccion(id):
    try:
        print('      [Solicitud] Realizando conexión con la base de datos...')
        conn = db.connection()
        colecciones = []
        inst =  '''
                SELECT CO.idColeccion, CO.nombreColeccion, CO.tipoColeccion,
                        TO_CHAR(CO.fechaCreColeccion, 'DD-MM-YYYY'), TO_CHAR(CO.fechaActColeccion, 'DD-MM-YYYY') FROM Coleccion CO
                    WHERE CO.idColeccion in
                        (SELECT UC.idColeccion FROM UsuarioColeccion UC
                            WHERE UC.idUsuario = %(id)s)
                    ORDER BY CO.idColeccion;
                '''
        with conn.cursor() as cursor:
            print('      [Validación] Ejecutando consulta...')
            cursor.execute(inst, {'id': id})
            for row in cursor.fetchall():
                coleccion = Coleccion(row[1], row[2], row[3], row[4])
                coleccion.idCol = row[0]
                colecciones.append(coleccion.to_json())
            conn.commit()
            cursor.close()
        
        return colecciones
    except Exception as e:
        print('      [Validación] Error de lógica interna:', e)
        return None