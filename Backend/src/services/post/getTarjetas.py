from ...database.db import DatabaseManager
from src.models.tarjeta import Tarjeta

db = DatabaseManager().getInstancia()

def getTarjetas(id_user):

    try:

        print('      [Servicio] Realizando conexión con la base de datos'.ljust(120, '.'))
        conn = db.connection()

        tarjetas = []
        inst =  '''
                SELECT TA.idTarjeta, TA.numero, TO_CHAR(TA.caducidad, 'MM/YYYY') AS caducidad, TA.cvv,
                        TA.saldo, UT.predeterminada FROM Tarjeta TA, UsuarioTarjeta UT
                    WHERE TA.idTarjeta = UT.idTarjeta AND UT.idUsuario = %(id)s
                    ORDER BY idTarjeta;
                '''
        
        with conn.cursor() as cursor:

            print('      [Servicio] Ejecutando consulta'.ljust(120, '.'))
            cursor.execute(inst, {'id': id_user})
            for row in cursor.fetchall():
                tarjeta = Tarjeta(row[1], row[2], row[3], row[4], row[5])
                tarjeta.idTarjeta = row[0]
                tarjetas.append(tarjeta.to_json())
            
            conn.commit()
            cursor.close()
        conn.close()

        print('      [Servicio] Tarjetas obtenidas'.ljust(120, '.'))
        return tarjetas
        
    except Exception as e:
        print(f'      [Validación] Error de lógica interna: {e}'.ljust(120, '.'))
        return None