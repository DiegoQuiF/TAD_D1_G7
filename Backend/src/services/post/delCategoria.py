from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def delCategoria(idMC):
    try:
        conn = db.connection()
        inst =  """
                delete from materialCategoria where idMaterialCategoria = %(idMC)s;
                """
        with conn.cursor() as cursor:
            cursor.execute(inst, {'idMC':idMC})
            conn.commit()
            cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("Error: " + e)
        return False