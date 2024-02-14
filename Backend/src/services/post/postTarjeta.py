import re
from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def postTarjeta(id, numero, caducidad, cvv, saldo):
    numero = str(numero)
    caducidad = str(caducidad)
    cvv = str(cvv)
    saldo = str(saldo)

    print('    [Registrar] Verificando sintaxis de datos'.ljust(120, '.'))
    result = verificarDatos(numero, caducidad, cvv, saldo)

    if result == 'COMPLETE':
        print('    [Registrar] Verificando numero'.ljust(120, '.'))
        result = numeroRegistrado(numero)

        if result == 'COMPLETE':
            try:

                print('    [Registrar] Obteniendo conexión a la BD'.ljust(120, '.'))
                conn = db.connection()

                inst =  '''
                        UPDATE UsuarioTarjeta
                            SET predeterminada = 'No'
                            WHERE idUsuario = %(id)s;
                        WITH nueva_tarjeta AS (
                            INSERT INTO Tarjeta(numero, caducidad, cvv, saldo)
                            VALUES(%(numero)s, TO_DATE(%(caducidad)s, 'DD/MM/YYYY'), %(cvv)s, %(saldo)s)
                            RETURNING idTarjeta
                        )
                        INSERT INTO UsuarioTarjeta(predeterminada, idUsuario, idTarjeta)
                            SELECT 'Si', %(id)s, idTarjeta FROM nueva_tarjeta;
                        '''
                
                print('    [Registrar] Ejecutando instrucción de creación de nueva tarjeta'.ljust(120, '.'))
                with conn.cursor() as cursor:
                    cursor.execute(inst, {'id': id, 'numero': numero, 'caducidad': caducidad, 'cvv':cvv, 'saldo':saldo})
                    conn.commit()
                    cursor.close()
                conn.close()
                
                print('    [Registrar] Registro completo'.ljust(120, '.'))
                return 'COMPLETE'
            
            except Exception as e:

                print('    [Registrar] Error interno del sistema'.ljust(120, '.'))
                return 'Hubo un error interno del sistema...'
            
        else:
            print('    [Registrar] Error: tarjeta ya registrada'.ljust(120, '.'))
            return result
        
    else:
        print('    [Registrar] Error: Sintaxis de datos'.ljust(120, '.'))
        return result


def verificarDatos(numero, caducidad, cvv, saldo):
    # Patrones de coincidencias
    patronNumero = r'^(\d){4}\-(\d){4}\-(\d){4}\-(\d){4}$'
    patronCaducidad = r'^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/\d{4}$'
    patronCvv = r'^(\d){3}$'
    patronSaldo = r'^(\d)+(\.(\d)+)?$'

    print('        [VerificadorS] Realizando verificación'.ljust(120, '.'))

    # Resultado de las comprobaciones
    resultado1 = re.match(patronNumero, numero)
    resultado2 = re.match(patronCaducidad, caducidad)
    resultado3 = re.match(patronCvv, cvv)
    resultado4 = re.match(patronSaldo, saldo)

    if not resultado1:
        print('        [VerificadorS] Sintaxis de número incorrecta'.ljust(120, '.'))
        return 'Sintaxis de número incorrecta...'
    if not resultado2:
        print('        [VerificadorS] Sintaxis de fecha de caducidad incorrecta'.ljust(120, '.'))
        return 'Sintaxis de fecha de caducidad incorrecta...'
    if not resultado3:
        print('        [VerificadorS] Sintaxis de cvv incorrecta'.ljust(120, '.'))
        return 'Sintaxis de cvv incorrecta...'
    if not resultado4:
        print('        [VerificadorS] Sintaxis de saldo incorrecta'.ljust(120, '.'))
        return 'Sintaxis de saldo incorrecta...'
    
    print('        [VerificadorS] Verificación correcta'.ljust(120, '.'))
    return 'COMPLETE'


def numeroRegistrado(numero):
    try:

        print('        [VerificadorCC] Obteniendo conexión a la BD'.ljust(120, '.'))
        conn = db.connection()

        total = 0
        inst =  '''
                SELECT COUNT(*) as total from Tarjeta where numero = %(numero)s;
                '''
        
        print('        [VerificadorCC] Ejecutando instrucción de verificación'.ljust(120, '.'))
        with conn.cursor() as cursor:
            cursor.execute(inst, {'numero': numero})
            for row in cursor.fetchall():
                total = row[0]
            conn.commit()
            cursor.close()
        conn.close()

        if total == 0:
            print('        [VerificadorCC] Verificación correcta'.ljust(120, '.'))
            return 'COMPLETE'
        
        else:
            print('        [VerificadorCC] El numero de tarjeta ya está registrado'.ljust(120, '.'))
            return 'El numero de tarjeta ya está registrado...'
        
    except Exception as e:

        print('        [VerificadorCC] Hubo un error interno del sistema'.ljust(120, '.'))
        return 'Hubo un error interno del sistema...'
