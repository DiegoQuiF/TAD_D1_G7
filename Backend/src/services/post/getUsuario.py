from src.database.db import connection
from src.models.usuario import Usuario
from src.auxiliar.encriptador import encriptar_contrasenia
from src.auxiliar.encriptador import desencriptar_contrasenia

def getUsuario(correo, contra):
    try:
        print('      [Validación] Realizando conexión con la base de datos...')
        conn = connection()
        usuarios = []
        inst = "SELECT US.idusuario, US.nombreusuario, US.apellidopatusuario, US.apellidomatusuario, CO.correo, CO.contrasenia, CO.nrocelular FROM Usuario US, Contacto CO WHERE US.idContacto = CO.idContacto and CO.correo = %(correo)s;"
        with conn.cursor() as cursor:
            print('      [Validación] Ejecutando consulta de validación...')
            cursor.execute(inst, {'correo': correo})
            for row in cursor.fetchall():
                usuario = Usuario(row[1], row[2], row[3], row[4], row[5], row[6])
                usuario.idUser = row[0]
                usuarios.append(usuario.to_json())
            conn.commit()
            cursor.close()
        conn.close()
        print('      [Validación] Consulta ejecutada correctamente...')
        print('      [Validación] Validando contraseña...')
        if validarContrasenia(contra, usuarios[0]['contra_user']):
            usuarios[0]['contra_user'] = contra
            print('      [Validación] Contraseña validada...')
            return usuarios
        else:
            print('      [Validación] Error: contraseña no valida...')
            return None
    except Exception as e:
        print('      [Validación] Error de lógica interna:', e)
        return None

def validarContrasenia(contrades, contraen):
    print("         [Encriptador] Validando...")
    if contrades == desencriptar_contrasenia(contraen):
        print("         [Encriptador] Validación correcta...")
        return True
    else:
        print("         [Encriptador] Validación incorrecta...")
        return False