from src.database.db import connection
from src.models.usuario import Usuario

def getUsuario(correo, contra):
    try:
        conn = connection()
        usuarios = []
        inst = "SELECT * FROM Usuario WHERE correo = %(correo)s and contrasenia = %(contra)s;"
        with conn.cursor() as cursor:
            cursor.execute(inst, {'correo': correo, 'contra': contra})
            for row in cursor.fetchall():
                usuario = Usuario(row[1], row[2], row[3], row[4], row[5], row[6])
                usuario.idUser = row[0]
                usuarios.append(usuario.to_json())
            conn.commit()
            cursor.close()
        conn.close()
        return usuarios
    except Exception as e:
        print("(SISTEMA)   Error: " + e)