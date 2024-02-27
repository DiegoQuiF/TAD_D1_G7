from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def postCategoria(idM, idC):
    try:
        conn = db.connection()
        total = 0;
        inst =  """
                select COUNT(*) as total from materialCategoria
	                WHERE idCategoria = %(idC)s and idMaterial = %(idM)s;
                """
        with conn.cursor() as cursor:
            cursor.execute(inst, {'idM':idM, 'idC':idC})
            for row in cursor.fetchall():
                total = row[0]
            conn.commit()
        
        if(total > 0):
            return False
        else:
            inst =  """
                    insert into materialCategoria(idCategoria, idMaterial)
                        values(%(idC)s, %(idM)s)
                    """
            with conn.cursor() as cursor:
                cursor.execute(inst, {'idM':idM, 'idC':idC})
                conn.commit()
                cursor.close()
            conn.close()
            return True
    except Exception as e:
        print("Error: " + e)
        return False