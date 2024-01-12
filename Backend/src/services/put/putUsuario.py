from src.database.db import connection

def putUsuario(nombre, aPat, aMat, correo, contra, celular, id):
    try:
        conn = connection()
        inst = "UPDATE Usuario set nombreusuario = %(nombre)s, apellidopatusuario = %(aPat)s, apellidomatusuario = %(aMat)s, correo = %(correo)s, contrasenia = %(contra)s, nrocelular = %(celular)s WHERE idusuario = %(id)s"
        with conn.cursor() as cursor:
            cursor.execute(inst, {'nombre': nombre, 'aPat': aPat, 'aMat': aMat, 'correo': correo, 'contra': contra, 'celular': celular, 'id': id})
            conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("(SISTEMA)   Error: "+e)
        return False