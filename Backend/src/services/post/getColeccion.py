from ...database.db import DatabaseManager
from src.models.coleccion import Coleccion

db = DatabaseManager().getInstancia()

def getColeccion(id):
    try:
        print('      [Solicitud] Realizando conexión con la base de datos...')
        conn = db.connection()
        colecciones = []
        inst =  '''
                SELECT CO.idColeccion, CO.nombre, CO.tipo,
                        TO_CHAR(CO.creacion, 'DD-MM-YYYY') as creacion, TO_CHAR(CO.actualizacion, 'DD-MM-YYYY') as actualizacion FROM Coleccion CO
                    WHERE CO.idColeccion in
                        (SELECT UC.idColeccion FROM UsuarioColeccion UC
                            WHERE UC.idUsuario = %(id)s)
                    ORDER BY CO.idColeccion;
                '''
        
        print('      [Solicitud] Ejecutando consulta...')
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id': id})
            for row in cursor.fetchall():
                coleccion = Coleccion(row[1], row[2], row[3], row[4])
                coleccion.idColeccion = row[0]
                colecciones.append(coleccion.to_json())
            conn.commit()
            cursor.close()
        conn.close()
        
        return colecciones
    except Exception as e:
        print('      [Validación] Error de lógica interna:', e)
        return None