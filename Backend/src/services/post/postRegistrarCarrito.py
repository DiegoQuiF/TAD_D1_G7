from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def postRegistrarCarrito(id_material, id_user):
    try:
        conn = db.connection()
        inst =  """
                INSERT INTO Carrito(idUsuario, idMaterial)
	                VALUES(%(id_user)s, %(id_material)s);
                """
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id_material':id_material, 'id_user':id_user})
            conn.commit()
            cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("Error: " + e)
        return False