import re
from ...database.db import DatabaseManager
from ...auxiliar.proxyEncriptador import Proxy

db = DatabaseManager().getInstancia()

def putUsuario(nombre, aPat, aMat, correo, contra, celular, direccion, id):
    celular = str(celular)

    print('    [Registrar] Verificando sintaxis de datos'.ljust(120, '.'))
    result = verificarDatos(nombre, aPat, aMat, correo, contra, celular, direccion)

    if result == 'COMPLETE':
        print('    [Registrar] Verificando disponibilidad de correo y número de celular'.ljust(120, '.'))
        result = correoCelularRegistrado(correo, celular, id)

        if result == 'COMPLETE':    
            try:
                
                print('    [Registrar] Solicitando encriptación de contraseña'.ljust(120, '.'))
                encriptador = Proxy()
                contra = encriptar(contra)

                print('    [Registrar] Estableciendo conexión con la BD'.ljust(120, '.'))
                conn = db.connection()
                inst =  '''
                        UPDATE Usuario 
                            SET nombre = %(nombre)s, aPaterno = %(aPat)s, aMaterno = %(aMat)s
                            WHERE idUsuario = %(id)s;
                        UPDATE Contacto
                            SET correo = %(correo)s, contrasenia = %(contra)s, nroCelular = %(celular)s, direccion = %(direccion)s
                            WHERE idContacto IN (SELECT idContacto FROM Usuario WHERE idUsuario = %(id)s)
                        '''
                print('    [Registrar] Actualizando datos del usuario'.ljust(120, '.'))
                with conn.cursor() as cursor:
                    cursor.execute(inst, {'nombre': nombre, 'aPat': aPat, 'aMat': aMat, 'id': id, 'correo': correo, 'contra': contra, 'celular': celular, 'direccion':direccion, 'id':id})
                    conn.commit()
                    cursor.close()
                conn.close()

                print('    [Registrar] Actualización completa'.ljust(120, '.'))
                return 'COMPLETE'
            except:
                return 'Hubo un error interno del sistema...'
        else:
            return result
    else:
        return result
        

def verificarDatos(nombre, aPat, aMat, correo, contra, celular, direccion):
    # Patrones de coincidencias
    patronLargo80 = r'^(.){0,80}$'
    patronLargo160 = r'^(.){0,160}$'
    patronContra = r'^(.){8,80}$'
    patronNombresPropios = r'^[A-Z]([A-Z]|[a-z]|\s)*$'
    patronCorreo = r'^([a-z]|[A-Z]|\_|\.)+\@[a-zA-Z]+\.[a-zA-Z]+(\.([a-zA-Z])+)*$'
    patronCelular = r'^(9)(\d{8})$'
    patronDireccion = r'^([A-Z]|[a-z]|\s|\.|\d|\_)+$'

    print('        [VerificadorS] Realizando verificación'.ljust(120, '.'))
    

    # Resultado de las comprobaciones
    resultado1 = re.match(patronNombresPropios, nombre)
    resultado2 = re.match(patronNombresPropios, aPat)
    resultado3 = re.match(patronNombresPropios, aMat)
    resultado4 = re.match(patronCorreo, correo)
    resultado5 = re.match(patronLargo80, nombre)
    resultado6 = re.match(patronLargo80, aPat)
    resultado7 = re.match(patronLargo80, aMat)
    resultado8 = re.match(patronLargo80, correo)
    resultado9 = re.match(patronContra, contra)
    resultado10 = re.match(patronCelular, celular)
    resultado11 = re.match(patronDireccion, direccion)
    resultado12 = re.match(patronLargo160, direccion)

    
    if not resultado1:
        print('        [VerificadorS] Sintaxis de nombre incorrecto'.ljust(120, '.'))
        return 'Sintaxis de nombre incorrecto...'
    if not resultado2:
        print('        [VerificadorS] Sintaxis de apellido paterno incorrecto'.ljust(120, '.'))
        return 'Sintaxis de apellido paterno incorrecto...'
    if not resultado3:
        print('        [VerificadorS] Sintaxis de apellido materno incorrecto'.ljust(120, '.'))
        return 'Sintaxis de apellido materno incorrecto...'
    if not resultado4:
        print('        [VerificadorS] Sintaxis de correo incorrecta'.ljust(120, '.'))
        return 'Sintaxis de correo incorrecta...'
    if not resultado5:
        print('        [VerificadorS] El nombre es demasiado largo, debe ser menor a 80 caracteres'.ljust(120, '.'))
        return 'El nombre es demasiado largo, debe ser menor a 80 caracteres...'
    if not resultado6:
        print('        [VerificadorS] El apellido paterno es demasiado largo, debe ser menor a 80 caracteres'.ljust(120, '.'))
        return 'El apellido paterno es demasiado largo, debe ser menor a 80 caracteres...'
    if not resultado7:
        print('        [VerificadorS] El apellido materno es demasiado largo, debe ser menor a 80 caracteres'.ljust(120, '.'))
        return 'El apellido materno es demasiado largo, debe ser menor a 80 caracteres...'
    if not resultado8:
        print('        [VerificadorS] El correo es demasiado largo, debe ser menor a 80 caracteres'.ljust(120, '.'))
        return 'Sintaxis de correo incorrecta...'
    if not resultado9:
        print('        [VerificadorS] La contraseña es no debe ser menor que 8 caracteres ni mayor a 80'.ljust(120, '.'))
        return 'La contraseña es no debe ser menor que 8 caracteres ni mayor a 80...'
    if not resultado10:
        print('        [VerificadorS] Sintaxis de número de celular incorrecta'.ljust(120, '.'))
        return 'Sintaxis de número de celular incorrecta...'
    if not resultado11:
        print('        [VerificadorS] Sintaxis de dirección incorrecta'.ljust(120, '.'))
        return 'Sintaxis de dirección incorrecta...'
    if not resultado12:
        print('        [VerificadorS] La direccion es demasiada larga, debe ser menor a 80 caracteres'.ljust(120, '.'))
        return 'La direccion es demasiada larga, debe ser menor a 80 caracteres...'
    
    print('        [VerificadorS] Verificación correcta'.ljust(120, '.'))
    return 'COMPLETE'


def correoCelularRegistrado(correo, celular, id):
    try:
        conn = db.connection()
        total = 0
        inst =  '''
                SELECT COUNT(*) AS total FROM Contacto
                    WHERE ((correo = %(correo)s) OR (nroCelular = %(celular)s))
                        AND idContacto NOT IN (SELECT idContacto FROM Usuario WHERE idUsuario = %(id)s);
                '''
        
        with conn.cursor() as cursor:
            cursor.execute(inst, {'correo': correo, 'celular': celular, 'id': id})
            for row in cursor.fetchall():
                total = row[0]
            conn.commit()
            cursor.close()
        conn.close()

        if total == 0:
            return 'COMPLETE'
        
        else:
            return 'El correo o número de celular ya están registrados...'
        
    except Exception as e:
        return 'Hubo un error interno del sistema...'
    

def encriptar(contra):
    print('        [Encriptador] Encriptando contraseña'.ljust(120, '.'))
    encriptador = Proxy()
    texto = encriptador.encriptar(contra)

    print('        [Encriptador] Encriptación correcta'.ljust(120, '.'))
    return texto