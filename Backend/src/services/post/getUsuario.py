from ...database.db import DatabaseManager
from src.models.usuario import Usuario
from ...auxiliar.proxyEncriptador import Proxy

db = DatabaseManager().getInstancia()

def getUsuario(correo, contra):

    try:

        print('      [Validación] Realizando conexión con la base de datos'.ljust(120, '.'))
        conn = db.connection()

        usuarios = []
        inst =  '''
                SELECT US.idUsuario, US.nombre, US.aPaterno, US.aMaterno,
                        CO.correo, CO.contrasenia, CO.nroCelular, CO.direccion
                    FROM Usuario US, Contacto CO
                    WHERE US.idContacto = CO.idContacto AND CO.correo = %(correo)s;
                '''
        
        with conn.cursor() as cursor:

            print('      [Validación] Ejecutando consulta de validación'.ljust(120, '.'))
            cursor.execute(inst, {'correo': correo})
            for row in cursor.fetchall():
                usuario = Usuario(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                usuario.idUser = row[0]
                usuarios.append(usuario.to_json())
            
            conn.commit()
            cursor.close()
        conn.close()

        print('      [Validación] Consulta ejecutada correctamente'.ljust(120, '.'))
        print('      [Validación] Validando contraseña'.ljust(120, '.'))
        if validarContrasenia(contra, usuarios[0]['contra_user']):
            usuarios[0]['contra_user'] = contra
            print('      [Validación] Contraseña validada'.ljust(120, '.'))
            return usuarios
        
        else:
            print('      [Validación] Error: contraseña no valida'.ljust(120, '.'))
            return None
        
    except Exception as e:
        print(f'      [Validación] Error de lógica interna: {e}'.ljust(120, '.'))
        return None


def validarContrasenia(contrades, contraen):

    desencriptador = Proxy()

    print("         [Encriptador] Validando".ljust(120, '.'))
    if contrades == desencriptador.desencriptar(contraen):
        print("         [Encriptador] Validación correcta".ljust(120, '.'))
        return True
    
    else:
        print("         [Encriptador] Validación incorrecta".ljust(120, '.'))
        return False