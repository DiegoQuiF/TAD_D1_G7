from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def postRecargarTarjeta(id, monto):
    try:
        conn = db.connection()
        inst =  """
                UPDATE Tarjeta
                    SET saldo = saldo + %(monto)s
                    WHERE idTarjeta = %(id)s;
                """
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id':id, 'monto':monto})
            conn.commit()
            cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("Error: " + e)
        return False