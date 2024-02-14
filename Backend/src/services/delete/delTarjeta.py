from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def delTarjeta(id):
    try:
        conn = db.connection()
        inst =  """
                DELETE FROM UsuarioTarjeta WHERE idTarjeta = %(id)s;
                DELETE FROM Tarjeta WHERE idTarjeta = %(id)s;
                """
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id':id})
            conn.commit()
            cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("Error: " + e)
        return False