import re
from src.database.db import connection
from src.auxiliar.encriptador import encriptar_contrasenia

def postRegistrarUsuario(nombre, aPat, aMat, correo, contra, celular):
    print('      [Registro] Verificando sintaxis de datos ingresados...')
    if verificarDatos(nombre, aPat, aMat, correo, contra, celular):
        print('      [Registro] Verificando disponibilidad de correo y nro. de celular...')
        if not correoCelularRegistrado(correo, celular):
            try:
                print('      [Registro] Solicitando encriptación de contraseña...')
                contra = encriptar(contra)
                print('      [Registro] Realizando conexión con la base de datos...')
                conn = connection()
                print('      [Registro] Ejecutando inserción de nuevo usuario...')
                print('      [Registro] Inserción de contacto...')
                inst = "INSERT INTO Contacto(correo, contrasenia, nrocelular) VALUES(%(correo)s, %(contra)s, %(celular)s)"
                with conn.cursor() as cursor:
                    cursor.execute(inst, {'correo': correo, 'contra': contra, 'celular': celular})
                    conn.commit()
                print('      [Registro] Obtención de contacto...')
                idContacto = ''
                inst = "select idContacto from Contacto where correo = %(correo)s and contrasenia = %(contra)s and nrocelular = %(celular)s"
                with conn.cursor() as cursor:
                    cursor.execute(inst, {'correo': correo, 'contra': contra, 'celular': celular})
                    for row in cursor.fetchall():
                        idContacto = row[0]
                    conn.commit()
                print('      [Registro] Inserción de usuario...')
                inst = "INSERT INTO Usuario (nombreUsuario, apellidoPatUsuario, apellidoMatUsuario, idcontacto) values (%(nombre)s, %(aPat)s, %(aMat)s, %(idContacto)s)"
                with conn.cursor() as cursor:
                    cursor.execute(inst, {'nombre': nombre, 'aPat': aPat, 'aMat': aMat, 'idContacto':idContacto})
                    conn.commit()
                print('      [Registro] Inserción ejecutada correctamente...')
                return True
            except Exception as e:
                print('      [Registro] Error de lógica interna:', e)
                return False
        else:
            print('      [Registro] Error: verificador de disponibilidad de correo y celular...')
            return False
    else:
        print('      [Registro] Error: verificador de sintaxis...')
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

def correoCelularRegistrado(correo, celular):
    try:
        print('         [VerificadorCC] Realizando conexión con la base de datos...')
        conn = connection()
        total = 0
        print('         [VerificadorCC] Ejecutando consulta de disponibilidad de correo y celular...')
        inst = "SELECT COUNT(*) as total FROM Contacto WHERE correo = %(correo)s or nrocelular = %(celular)s;"
        with conn.cursor() as cursor:
            cursor.execute(inst, {'correo': correo, 'celular': celular})
            for row in cursor.fetchall():
                total = row[0]
            conn.commit()
        conn.close()
        if total == 0:
            print('         [VerificadorCC] Correo y celular validados...')
            return False
        else:
            print('         [VerificadorCC] Error: celular o correo ya registrados...')
            return True
    except Exception as e:
        print("         [VerificadorCC] Error de lógica interna:", e)
        return True

def encriptar(contra):
    print("         [Encriptador] Encriptando contraseña...")
    texto = encriptar_contrasenia(contra)
    print("         [Encriptador] Contraseña encriptada...")
    return texto
