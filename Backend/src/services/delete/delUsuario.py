from src.database.db import connection
from src.models.usuario import Usuario

# Esta función por el momento no se utilizará, almenos para los usuarios

def delUsuario(id):
    try:
        conn = connection()
        inst = "DELETE FROM Usuario WHERE idusuario = %(id)s;"
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id': id})
            conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("(SISTEMA)   Error: " + e)
        return False
    