import re
from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def postRegistrarFactura(pagado, fecha, idMaterial, idUsuario):
    print('      [Registro] Verificando sintaxis de datos ingresados...')
    if verificarDatos(pagado, fecha):
        print('      [Registro] Sintaxis validada...')
        try:
            print('      [Registro] Verificando stock...')
            if verificarStock(idMaterial):
                print('      [Registro] Stock verificado...')
                print('      [Registro] Disminuyendo stock...')
                if disminuirStock(idMaterial):
                    print('      [Registro] Stock disminuido...')
                    print('      [Registro] Registrando factura...')
                    if registrarFactura(pagado, fecha, idMaterial, idUsuario):
                        print('      [Registro] Factura registrada...')
                        return True
                    else:
                        print('      [Registro] Factura no registrada...')
                else:
                    print('      [Registro] No se pudo disminuir el stock...')
            else:
                print('      [Registro] No se pudo verificar el stock / no hay stock...')
            return False
        except Exception as e:
            print('      [Registro] Error de lógica interna:', e)
            return False
    else:
        print('      [Registro] Fallas en la sintaxis...')
        return False


def verificarDatos(pagado, fecha):
    # Patrones de coincidencias
    patronSiNo = r'^(Si|No)$'
    patronFecha = r'^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/\d{4}$'

    # Resultado de las comprobaciones
    resultado1 = re.match(patronSiNo, pagado)
    resultado2 = re.match(patronFecha, fecha)

    print('         [VerificadorSintx] Ejecutando verificación...')
    if resultado1 and resultado2:
        print('         [VerificadorSintx] Sintaxis validada...')
        return True
    else:
        print('         [VerificadorSintx] Sintaxis de datos errónea...')
        return False


def verificarStock(idMaterial):
    try:
        print('         [VerificadorStock] Conectandose con la base de datos...')
        conn = db.connection()
        stock = ''
        inst =  '''
                SELECT MB.stockMaterial FROM MaterialBibliografico MB WHERE idMaterial = %(idMaterial)s;
                '''
        print('         [VerificadorStock] Ejecutando verificación...')
        with conn.cursor() as cursor:
            cursor.execute(inst, {'idMaterial': idMaterial})
            for row in cursor.fetchall():
                stock = row[0]
            conn.commit()
        conn.close()
        print('         [VerificadorStock] Validando...')
        if int(stock) >= 1:
            print('         [VerificadorStock] Stock encontrado...')
            return True
        else:
            print('         [VerificadorStock] Stock no encontrado...')
            return False
    except Exception as e:
        print('         [VerificadorStock] Error de lógica interna:', e)
        return False


def disminuirStock(idMaterial):
    try:
        print('         [ControlStock] Conectandose con la base de datos...')
        conn = db.connection()
        stock = ''
        inst =  '''
                UPDATE MaterialBibliografico SET stockMaterial = stockMaterial-1 WHERE idMaterial = %(idMaterial)s;
                '''
        print('         [ControlStock] Ejecutando disminución...')
        with conn.cursor() as cursor:
            cursor.execute(inst, {'idMaterial': idMaterial})
            conn.commit()
        conn.close()
        print('         [ControlStock] Disminución efectuada...')
        return True
    except Exception as e:
        print('         [ControlStock] Error de lógica interna:', e)
        return False

def registrarFactura(pagado, fecha, idMaterial, idUsuario):
    try:
        print('         [RegistroFactura] Conectandose con la base de datos...')
        conn = db.connection()
        inst =  '''
                DO $$ 
                DECLARE 
                    nueva_factura_id integer;
                BEGIN 
                    -- Insertar en Factura y obtener el idFactura generado
                    INSERT INTO Factura(pagadoFactura, fechaFactura)
                    VALUES (%(pagado)s, TO_DATE(%(fecha)s, 'DD/MM/YYYY'))
                    RETURNING idFactura INTO nueva_factura_id;

                    -- Insertar en MaterialFactura utilizando el idFactura obtenido
                    INSERT INTO MaterialFactura(idMaterial, idFactura)
                    VALUES (%(idMaterial)s, nueva_factura_id);

                    -- Insertar en UsuarioFactura utilizando el mismo idFactura
                    INSERT INTO UsuarioFactura(idUsuario, idFactura)
                    VALUES (%(idUsuario)s, nueva_factura_id);
                END $$;
                '''
        print('         [RegistroFactura] Ejecutando registro de factura...')
        with conn.cursor() as cursor:
            cursor.execute(inst, {'pagado': pagado, 'fecha':fecha, 'idMaterial':idMaterial, 'idUsuario':idUsuario})
            conn.commit()
        conn.close()
        print('         [RegistroFactura] Factura registrada...')
        return True
    except Exception as e:
        print('         [RegistroFactura] Error de lógica interna:', e)
        return False