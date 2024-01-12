from src.database.db import connection

def postRegistrarUsuario(nombre, aPat, aMat, correo, contra, celular):
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