import re
from src.database.db import connection

def postRegistrarUsuario(nombre, aPat, aMat, correo, contra, celular):
    if verificarDatos(nombre, aPat, aMat, correo, contra, celular):
        try:
            conn = connection()
            inst = "INSERT INTO Usuario (nombreUsuario, apellidoPatUsuario, apellidoMatUsuario, correo, contrasenia, nroCelular) values (%(nombre)s, %(aPat)s, %(aMat)s, %(correo)s, %(contra)s, %(celular)s)"
            with conn.cursor() as cursor:
                cursor.execute(inst, {'nombre': nombre, 'aPat': aPat, 'aMat': aMat, 'correo': correo, 'contra': contra, 'celular': celular})
                conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("(SISTEMA)   Error: "+e)
            return False
    else:
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

    if resultado1 and resultado2 and resultado3 and resultado4 and resultado5 and resultado6 and resultado7:
        print("AAAA")
        return True
    else:
        return False