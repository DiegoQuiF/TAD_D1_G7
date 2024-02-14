import re
from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def postRegistrarColeccion(id_user, nombre, tipo, creacion, actualizacion):
    print('      [Registro] Verificando sintaxis de datos ingresados...')
    if verificarDatos(nombre, tipo, creacion, actualizacion):
        try:
            print('      [Registro] Realizando conexión con la base de datos...')
            conn = db.connection()
            print('      [Registro] Ejecutando inserción de nueva colección...')
            print('      [Registro] Inserción de coleccion...')
            
            inst =  '''
                    WITH nueva_coleccion AS (
                        INSERT INTO Coleccion(nombre, tipo, creacion, actualizacion)
                        VALUES(%(nombre)s, %(tipo)s, TO_DATE(%(creacion)s, 'DD/MM/YYYY'), TO_DATE(%(actualizacion)s, 'DD/MM/YYYY'))
                        RETURNING idColeccion
                    )
                    INSERT INTO UsuarioColeccion(idUsuario, idColeccion)
                        SELECT %(id_user)s, idColeccion FROM nueva_coleccion;
                    '''
            with conn.cursor() as cursor:
                cursor.execute(inst, {'nombre': nombre, 'tipo': tipo, 'creacion': creacion, 'actualizacion': actualizacion, 'id_user':id_user})
                conn.commit()
            print('      [Registro] Inserción ejecutada correctamente...')
            return True
        except Exception as e:
            print('      [Registro] Error de lógica interna:', e)
            return False
    else:
        print('      [Registro] Error: verificador de sintaxis...')
        return False

def verificarDatos(nombre, tipo, creacion, actualizacion):
    # Patrones de coincidencias
    patronNombresPropios = r'^[A-Z]([A-Z]|[a-z]|\s|\d){0,99}$'
    patronTipo = r'^(Publica|Privada)$'
    patronFecha = r'^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/\d{4}$'

    # Resultado de las comprobaciones
    resultado1 = re.match(patronNombresPropios, nombre)
    resultado2 = re.match(patronTipo, tipo)
    resultado3 = re.match(patronFecha, creacion)
    resultado4 = re.match(patronFecha, actualizacion)

    print('         [VerificadorS] Ejecutando verificaciones de los datos...')
    if resultado1 and resultado2 and resultado3 and resultado4:
        print('         [VerificadorS] Sintaxis validada...')
        return True
    else:
        print('         [VerificadorS] Error: sintaxis de datos errónea...')
        return False