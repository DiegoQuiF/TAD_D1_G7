import re
from src.database.db import connection
from src.auxiliar.encriptador import encriptar_contrasenia

def postRegistrarUsuario(nombre, aPat, aMat, correo, contra, celular):
    print('    [Registrar] Verificando sintaxis de datos'.ljust(120, '.'))
    result = verificarDatos(nombre, aPat, aMat, correo, contra, celular)
    if result == 'COMPLETE':
        print('    [Registrar] Verificando correo & nro. celular'.ljust(120, '.'))
        result = correoCelularRegistrado(correo, celular)
        if result == 'COMPLETE':
            try:
                print('    [Registrar] Encriptando contraseña'.ljust(120, '.'))
                contra = encriptar(contra)
                print('    [Registrar] Obteniendo conexión a la BD'.ljust(120, '.'))
                conn = connection()
                inst =  '''
                        INSERT INTO Contacto(correoContacto, contraseniaContacto, nroCelularContacto)
	                            VALUES (%(correo)s, %(contra)s, %(celular)s);
                        '''
                print('    [Registrar] Ejecutando instrucción de inserción'.ljust(120, '.'))
                with conn.cursor() as cursor:
                    cursor.execute(inst, {'correo': correo, 'contra': contra, 'celular': celular})
                    conn.commit()
                idContacto = ''
                inst =  '''
                        SELECT idContacto FROM Contacto WHERE correoContacto = %(correo)s and contraseniaContacto = %(contra)s
		                        and nroCelularContacto = %(celular)s;
                        '''
                with conn.cursor() as cursor:
                    cursor.execute(inst, {'correo': correo, 'contra': contra, 'celular': celular})
                    for row in cursor.fetchall():
                        idContacto = row[0]
                    conn.commit()
                inst =  '''
                        INSERT INTO Usuario(nombreUsuario, apellidoPatUsuario, apellidoMatUsuario, idContacto)
	                            VALUES (%(nombre)s, %(aPat)s, %(aMat)s, %(idContacto)s);
                        '''
                with conn.cursor() as cursor:
                    cursor.execute(inst, {'nombre': nombre, 'aPat': aPat, 'aMat': aMat, 'idContacto':idContacto})
                    conn.commit()
                print('    [Registrar] Registro completo'.ljust(120, '.'))
                return 'COMPLETE'
            except Exception as e:
                print('    [Registrar] Error interno del sistema'.ljust(120, '.'))
                return 'Hubo un error interno del sistema...'
        else:
            print('    [Registrar] Error: Correo o celular registrados'.ljust(120, '.'))
            return result
    else:
        print('    [Registrar] Error: Sintaxis de datos'.ljust(120, '.'))
        return result

def verificarDatos(nombre, aPat, aMat, correo, contra, celular):
    # Patrones de coincidencias
    patronNombresPropios = r'^[A-Z]([A-Z]|[a-z]|\s){0,49}$'
    patronCorreo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    patronCaracteresLibres = r'^(.{1,50})$'
    patronCelular = r'^(9)(\d{8})$'

    print('        [VerificadorS] Realizando verificación'.ljust(120, '.'))

    # Resultado de las comprobaciones
    resultado1 = re.match(patronNombresPropios, nombre)
    resultado2 = re.match(patronNombresPropios, aPat)
    resultado3 = re.match(patronNombresPropios, aMat)
    resultado4 = re.match(patronCorreo, correo)
    resultado5 = re.match(patronCaracteresLibres, correo)
    resultado6 = re.match(patronCaracteresLibres, contra)
    resultado7 = re.match(patronCelular, celular)

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
        print('        [VerificadorS] Correo demasiado largo'.ljust(120, '.'))
        return 'Correo demasiado largo...'
    if not resultado6:
        print('        [VerificadorS] Contraseña demasiado larga'.ljust(120, '.'))
        return 'Contraseña demasiado larga...'
    if not resultado7:
        print('        [VerificadorS] Sintaxis de número de celular incorrecta'.ljust(120, '.'))
        return 'Sintaxis de número de celular incorrecta...'
    
    print('        [VerificadorS] Verificación correcta'.ljust(120, '.'))
    return 'COMPLETE'


def correoCelularRegistrado(correo, celular):
    try:
        print('        [VerificadorCC] Obteniendo conexión a la BD'.ljust(120, '.'))
        conn = connection()
        total = 0
        inst =  '''
                SELECT COUNT(*) AS total FROM Contacto WHERE correoContacto = %(correo)s or nroCelularContacto = %(celular)s;
                '''
        print('        [VerificadorCC] Ejecutando instrucción de verificación'.ljust(120, '.'))
        with conn.cursor() as cursor:
            cursor.execute(inst, {'correo': correo, 'celular': celular})
            for row in cursor.fetchall():
                total = row[0]
            conn.commit()
        conn.close()
        if total == 0:
            print('        [VerificadorCC] Verificación correcta'.ljust(120, '.'))
            return 'COMPLETE'
        else:
            print('        [VerificadorCC] El correo o número de celular ya están registrados'.ljust(120, '.'))
            return 'El correo o número de celular ya están registrados...'
    except Exception as e:
        print('        [VerificadorCC] Hubo un error interno del sistema'.ljust(120, '.'))
        return 'Hubo un error interno del sistema...'

def encriptar(contra):
    print('        [Encriptador] Encriptando contraseña'.ljust(120, '.'))
    texto = encriptar_contrasenia(contra)
    print('        [VerificadorCC] Encriptación correcta'.ljust(120, '.'))
    return texto
