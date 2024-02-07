from ...database.db import DatabaseManager
from src.models.usuario import Usuario

db = DatabaseManager().getInstancia()

def getUsuarios():
    try:
        conn = db.connection()
        usuarios = []
        inst =  '''
                SELECT US.idUsuario, US.nombreUsuario, US.apellidoPatUsuario, US.apellidoMatUsuario,
                        CO.correoContacto, CO.contraseniaContacto, CO.nroCelularContacto
                        FROM Usuario US, Contacto CO
                        WHERE US.idContacto = CO.idContacto;
                '''
        with conn.cursor() as cursor:
            cursor.execute(inst, )
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