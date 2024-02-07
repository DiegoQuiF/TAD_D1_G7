import re
from ...database.db import DatabaseManager
from src.auxiliar.encriptador import encriptar_contrasenia

db = DatabaseManager().getInstancia()

def putUsuario(nombre, aPat, aMat, correo, contra, celular, id):
    result = verificarDatos(nombre, aPat, aMat, correo, contra, celular)
    if result == 'COMPLETE':
        result = correoCelularRegistrado(correo, celular, id)
        if result == 'COMPLETE':    
            try:
                contra = encriptar(contra)
                conn = db.connection()
                inst =  '''
                        UPDATE Usuario U
                                SET nombreUsuario = %(nombre)s, apellidoPatUsuario = %(aPat)s, apellidoMatUsuario = %(aMat)s
                                FROM Contacto CO WHERE U.idUsuario = %(id)s AND U.idContacto = CO.idContacto;
                        '''
                with conn.cursor() as cursor:
                    cursor.execute(inst, {'nombre': nombre, 'aPat': aPat, 'aMat': aMat, 'id': id})
                    conn.commit()
                inst =  '''
                        UPDATE Contacto
                                SET correoContacto = %(correo)s, contraseniaContacto = %(contra)s, nroCelularContacto = %(celular)s
                                WHERE idContacto IN (SELECT idContacto FROM Usuario WHERE idUsuario = %(id)s);
                        '''
                with conn.cursor() as cursor:
                    cursor.execute(inst, {'correo': correo, 'contra': contra, 'celular': celular, 'id': id})
                    conn.commit()
                conn.close()
                return True
            except:
                return 'Hubo un error interno del sistema...'
        else:
            return result
    else:
        return result
        


def verificarDatos(nombre, aPat, aMat, correo, contra, celular):
    # Patrones de coincidencias
    patronNombresPropios = r'^[A-Z]([A-Z]|[a-z]|\s){0,49}$'
    patronCorreo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    patronCaracteresLibres = r'^(.{1,50})$'
    patronCelular = r'^(9)(\d{8})$'

    # Resultado de las comprobaciones
    resultado1 = re.match(patronNombresPropios, nombre)
    resultado2 = re.match(patronNombresPropios, aPat)
    resultado3 = re.match(patronNombresPropios, aMat)
    resultado4 = re.match(patronCorreo, correo)
    resultado5 = re.match(patronCaracteresLibres, correo)
    resultado6 = re.match(patronCaracteresLibres, contra)
    resultado7 = re.match(patronCelular, celular)

    if not resultado1:
        return 'Sintaxis de nombre incorrecto...'
    if not resultado2:
        return 'Sintaxis de apellido paterno incorrecto...'
    if not resultado3:
        return 'Sintaxis de apellido materno incorrecto...'
    if not resultado4:
        return 'Sintaxis de correo incorrecta...'
    if not resultado5:
        return 'Correo demasiado largo...'
    if not resultado6:
        return 'Contraseña demasiado larga...'
    if not resultado7:
        return 'Sintaxis de número de celular incorrecta...'
    return 'COMPLETE'

def correoCelularRegistrado(correo, celular, id):
    try:
        conn = db.connection()
        total = 0
        inst =  '''
                SELECT COUNT(*) AS total FROM Contacto WHERE ((correoContacto = %(correo)s) or %(celular)s)) and idContacto not in (
                    SELECT idContacto from Usuario where idUsuario = %(id)s);
                '''
        with conn.cursor() as cursor:
            cursor.execute(inst, {'correo': correo, 'celular': celular, 'id': id})
            for row in cursor.fetchall():
                total = row[0]
            conn.commit()
        conn.close()
        if total == 0:
            return 'COMPLETE'
        else:
            return 'El correo o número de celular ya están registrados...'
    except Exception as e:
        return 'Hubo un error interno del sistema...'

def encriptar(contra):
    texto = encriptar_contrasenia(contra)
    return texto