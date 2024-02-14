from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def delColeccion(id):
    try:
        conn = db.connection()
        inst =  """
                DELETE FROM usuarioColeccion WHERE idColeccion = %(id)s;
                DELETE FROM Coleccion WHERE idColeccion = %(id)s;
                """
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id':id})
            conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("(SISTEMA)   Error: " + e)
        return False