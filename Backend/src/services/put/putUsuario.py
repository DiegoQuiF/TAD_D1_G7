import re
from src.database.db import connection
from src.auxiliar.encriptador import encriptar_contrasenia

def putUsuario(nombre, aPat, aMat, correo, contra, celular, id):
    print('      [Actualizar] Verificando sintaxis de datos ingresados...')
    if verificarDatos(nombre, aPat, aMat, correo, contra, celular):
        try:
            print('      [Actualizar] Solicitando encriptación de contraseña...')
            contra = encriptar(contra)
            print('      [Actualizar] Estableciendo conexión con la base de datos...')
            conn = connection()

            print('      [Actualizar] Realizando actualización de datos de Usuario...')
            
            inst =  '''
                    UPDATE Usuario U
                            SET nombreUsuario = %(nombre)s, apellidoPatUsuario = %(aPat)s, apellidoMatUsuario = %(aMat)s
                            FROM Contacto CO WHERE U.idUsuario = %(id)s AND U.idContacto = CO.idContacto;
                    '''
            with conn.cursor() as cursor:
                cursor.execute(inst, {'nombre': nombre, 'aPat': aPat, 'aMat': aMat, 'id': id})
                conn.commit()
            
            print('      [Actualizar] Realizando actualización de datos de Contacto...')
            inst =  '''
                    UPDATE Contacto
                            SET correoContacto = %(correo)s, contraseniaContacto = %(contra)s, nroCelularContacto = %(celular)s
                            WHERE idContacto IN (SELECT idContacto FROM Usuario WHERE idUsuario = %(id)s);
                    '''
            with conn.cursor() as cursor:
                cursor.execute(inst, {'correo': correo, 'contra': contra, 'celular': celular, 'id': id})
                conn.commit()
            conn.close()
            print('      [Actualizar] Actualización completa...')
            return True
        except Exception as e:
            print('      [Actualizar] Error de lógica interna:', e)
            return False
    else:
        print('      [Actualizar] Error: verificador de sintaxis...')
        return False
        


def verificarDatos(nombre, aPat, aMat, correo, contra, celular):
    # Patrones de coincidencias
    patronNombresPropios = r'^[A-Z]([A-Z]|[a-z]|\s){0,49}$'
    patronCorreo = r'^(([a-zA-Z0-9\.\_])+@([a-zA-Z0-9])+(\.([a-zA-Z])+)+)$'
    patronCorreoLargo = r'^(.{1,50})$'
    patronCelular = r'^(9)(\d{8})$'

    # Resultado de las comprobaciones
    resultado1 = re.match(patronNombresPropios, nombre)
    resultado2 = re.match(patronNombresPropios, aPat)
    resultado3 = re.match(patronNombresPropios, aMat)
    resultado4 = re.match(patronCorreo, correo)
    resultado5 = re.match(patronCorreoLargo, correo)
    resultado6 = re.match(patronCorreoLargo, contra)
    resultado7 = re.match(patronCelular, celular)

    print('         [VerificadorS] Ejecutando verificaciones de los datos...')
    if resultado1 and resultado2 and resultado3 and resultado4 and resultado5 and resultado6 and resultado7:
        print('         [VerificadorS] Sintaxis validada...')
        return True
    else:
        print('         [VerificadorS] Error: sintaxis de datos errónea...')
        return False

def encriptar(contra):
    print("         [Encriptador] Encriptando contraseña...")
    texto = encriptar_contrasenia(contra)
    print("         [Encriptador] Contraseña encriptada...")
    return texto