import re
from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def postRegistrarFactura(fechaC, fechaE, idMaterial, idUsuario):
    print('      [Registro] Verificando sintaxis de datos ingresados...')
    if verificarDatos(fechaC, fechaE):
        print('      [Registro] Sintaxis validada...')
        print('      [Registro] Verificando medio de pago...')
        if verificarSaldos(idMaterial, idUsuario):
            print('      [Registro] Medio de pago validado...')
            if verificarStock(idMaterial):
                print('      [Registro] Stock verificado...')
                print('      [Registro] Realizando operación...')
                
                print('         [Registro] Conectandose con la base de datos...')
                conn = db.connection()
                inst =  '''
                        DO $$ 
                        DECLARE 
                            nueva_factura_id integer;
                        BEGIN 
                            -- Insertar en Factura y obtener el idFactura generado
                            INSERT INTO Factura(pagado, fechaCompra, fechaEntrega, subtotal)
                            VALUES ('Si', TO_DATE(%(fechaC)s, 'DD/MM/YYYY'), TO_DATE(%(fechaE)s, 'DD/MM/YYYY'), 
                                    (SELECT precioFisico FROM Material WHERE idMaterial = %(idMaterial)s))
                            RETURNING idFactura INTO nueva_factura_id;

                            -- Insertar en MaterialFactura utilizando el idFactura obtenido
                            INSERT INTO MaterialFactura(idMaterial, idFactura)
                            VALUES (%(idMaterial)s, nueva_factura_id);

                            -- Insertar en UsuarioFactura utilizando el mismo idFactura
                            INSERT INTO UsuarioFactura(idUsuario, idFactura)
                            VALUES (%(idUsuario)s, nueva_factura_id);
                        END $$;

                        UPDATE Tarjeta SET
                            saldo = saldo - (SELECT precioFisico FROM Material WHERE idMaterial = %(idMaterial)s)
                            WHERE idTarjeta in (select TA.idTarjeta from Tarjeta TA, usuarioTarjeta UT
                            WHERE TA.idTarjeta = UT.idTarjeta AND UT.idUsuario = %(idUsuario)s AND UT.predeterminada = 'Si');

                        UPDATE Material SET stockFisico = stockFisico - 1 WHERE idMaterial = %(idMaterial)s;

                        UPDATE Tarjeta SET
                            saldo = saldo + (0.7*(SELECT precioFisico FROM Material WHERE idMaterial = %(idMaterial)s))
                            WHERE idTarjeta in (select UT.idTarjeta from usuarioTarjeta UT
                            WHERE UT.predeterminada = 'Si' AND UT.idUsuario in (SELECT UC.idUsuario FROM UsuarioColeccion UC, ColeccionMaterial CM
                                WHERE UC.idColeccion = CM.idColeccion AND CM.idMaterial = %(idMaterial)s));
                            
                        UPDATE Tarjeta SET
                            saldo = saldo + (0.3*(SELECT precioFisico FROM Material WHERE idMaterial = %(idMaterial)s))
                            WHERE idTarjeta = '60012';
                        '''
                print('         [Registro] Ejecutando transacción...')
                with conn.cursor() as cursor:
                    cursor.execute(inst, {'idMaterial': idMaterial, 'idUsuario': idUsuario, 'fechaC':fechaC, 'fechaE': fechaE})
                    conn.commit()
                    cursor.close()
                conn.close()

                print('      [Registro] Transacción realizada...')
                return True
            else:
                print('      [Registro] No se pudo verificar el stock / no hay stock...')
            return False
        else:
            print('      [Registro] Fallas en el medio de pago...')
            return False
    else:
        print('      [Registro] Fallas en la sintaxis...')
        return False


def verificarDatos(fechaC, fechaE):
    # Patrones de coincidencias
    patronFecha = r'^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/\d{4}$'

    # Resultado de las comprobaciones
    resultado1 = re.match(patronFecha, fechaC)
    resultado2 = re.match(patronFecha, fechaE)

    print('         [VerificadorSintx] Ejecutando verificación...')
    if resultado1 and resultado2:
        print('         [VerificadorSintx] Sintaxis validada...')
        return True
    else:
        print('         [VerificadorSintx] Sintaxis de datos errónea...')
        return False


def verificarSaldos(idMaterial, idUsuario):
    try:
        print('         [VerificadorSaldo] Conectandose con la base de datos...')
        conn = db.connection()
        res1 = None
        res2 = None
        
        print('         [VerificadorSaldo] Ejecutando verificación...')

        inst =  '''
            select TA.saldo>MB.precioFisico as disponible from Tarjeta TA, usuarioTarjeta UT, material MB, carrito CA
                WHERE TA.idTarjeta = UT.idTarjeta AND UT.predeterminada = 'Si' AND UT.idUsuario = %(idUsuario)s
                    AND MB.idMaterial = %(idMaterial)s AND CA.idUsuario = UT.idUsuario AND CA.idMaterial = MB.idMaterial
        '''

        with conn.cursor() as cursor:
            cursor.execute(inst, {'idMaterial': idMaterial, 'idUsuario':idUsuario})
            for row in cursor.fetchall():
                res1 = row[0]
            conn.commit()

        inst =  '''
            select TA.saldo>0 as disponible from Tarjeta TA, usuarioTarjeta UT
                WHERE TA.idTarjeta = UT.idTarjeta AND UT.predeterminada = 'Si'
                    AND UT.predeterminada = 'Si' AND UT.idUsuario in (SELECT UC.idUsuario FROM UsuarioColeccion UC, ColeccionMaterial CM
                        WHERE UC.idColeccion = CM.idColeccion AND CM.idMaterial = %(idMaterial)s)
        '''

        with conn.cursor() as cursor:
            cursor.execute(inst, {'idMaterial': idMaterial})
            for row in cursor.fetchall():
                res2 = row[0]
            conn.commit()
            cursor.close()
        conn.close()

        print('         [VerificadorSaldo] Validando...')
        if res1 and res2:
            print('         [VerificadorSaldo] Tarjetas validadas...')
            return True
        else:
            print('         [VerificadorSaldo] Tarjetas no encontradas...')
            return False
    except Exception as e:
        print('         [VerificadorSaldo] Error de lógica interna:', e)
        return False


def verificarStock(idMaterial):
    try:
        print('         [VerificadorStock] Conectandose con la base de datos...')
        conn = db.connection()
        res = None
        inst =  '''
                select MB.stockFisico>0 as disponible from Material MB
	                WHERE MB.idMaterial = %(idMaterial)s;
                '''
        print('         [VerificadorStock] Ejecutando verificación...')
        with conn.cursor() as cursor:
            cursor.execute(inst, {'idMaterial': idMaterial})
            for row in cursor.fetchall():
                res = row[0]
            conn.commit()
            cursor.close()
        conn.close()

        print('         [VerificadorStock] Validando...')
        if res:
            print('         [VerificadorStock] Stock encontrado...')
            return True
        else:
            print('         [VerificadorStock] Stock no encontrado...')
            return False
    except Exception as e:
        print('         [VerificadorStock] Error de lógica interna:', e)
        return False