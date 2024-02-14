import re
from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def putColeccion(id, nombre, tipo, actu):
    print('      [Actualizar] Verificando sintaxis de datos ingresados...')
    if verificarDatos(nombre, tipo, actu):
        try:
            print('      [Actualizar] Estableciendo conexión con la base de datos...')
            conn = db.connection()

            print('      [Actualizar] Realizando actualización de datos de Coleccion...')
            
            inst =  """
                    UPDATE Coleccion CO
                        SET nombre = %(nombre)s, tipo = %(tipo)s,
                            actualizacion = TO_DATE(%(actu)s, 'DD/MM/YYYY')
                        WHERE CO.idColeccion = %(id)s;
                    """
            with conn.cursor() as cursor:
                cursor.execute(inst, {'nombre': nombre, 'tipo': tipo, 'actu': actu, 'id': id})
                conn.commit()
            conn.commit()
            conn.close()

            print(f'''
    {nombre}, {tipo}, {actu}, {id}
''')

            print('      [Actualizar] Actualización completa...')
            return True
        except Exception as e:
            print('      [Actualizar] Error de lógica interna:', e)
            return False
    else:
        print('      [Actualizar] Error: verificador de sintaxis...')
        return False
        


def verificarDatos(nombre, tipo, actualizacion):
    # Patrones de coincidencias
    patronNombresPropios = r'^[A-Z]([A-Z]|[a-z]|\s|\d){0,99}$'
    patronTipo = r'^(Publica|Privada)$'
    patronFecha = r'^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/\d{4}$'

    # Resultado de las comprobaciones
    resultado1 = re.match(patronNombresPropios, nombre)
    resultado2 = re.match(patronTipo, tipo)
    resultado3 = re.match(patronFecha, actualizacion)

    print('         [VerificadorS] Ejecutando verificaciones de los datos...')
    if resultado1 and resultado2 and resultado3:
        print('         [VerificadorS] Sintaxis validada...')
        return True
    else:
        print('         [VerificadorS] Error: sintaxis de datos errónea...')
        return False