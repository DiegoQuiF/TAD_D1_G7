from src.database.db import connection

def delMaterial(id):
    try:
        conn = connection()
        inst =  """
                DELETE FROM coleccionMaterial WHERE idMaterial = %(id)s;
                DELETE FROM MaterialBibliografico WHERE idMaterial = %(id)s;
                """
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id':id, 'id':id})
            conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("(SISTEMA)   Error: " + e)
        return False