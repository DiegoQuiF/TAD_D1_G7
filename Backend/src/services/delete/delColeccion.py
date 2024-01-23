from src.database.db import connection
from src.models.usuario import Usuario

def delColeccion(id):
    try:
        conn = connection()
        inst =  """
                DELETE FROM usuarioColeccion WHERE idColeccion = %(id)s;
                DELETE FROM Coleccion WHERE idColeccion = %(id)s;
                """
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id':id, 'id':id})
            conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("(SISTEMA)   Error: " + e)
        return False