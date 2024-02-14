from ...database.db import DatabaseManager
from src.models.tarjeta import Tarjeta

db = DatabaseManager().getInstancia()

def putPredeterminadoTarjeta(id_user, id_tarjeta):

    try:

        print('      [Servicio] Realizando conexión con la base de datos'.ljust(120, '.'))
        conn = db.connection()

        inst =  '''
                UPDATE UsuarioTarjeta
                    SET predeterminada = 'No'
                    WHERE idUsuario = %(id_user)s;
                UPDATE UsuarioTarjeta
                    SET predeterminada = 'Si'
                    WHERE idTarjeta = %(id_tarjeta)s;
                '''
        
        with conn.cursor() as cursor:
            print('      [Servicio] Ejecutando consulta'.ljust(120, '.'))
            cursor.execute(inst, {'id_user': id_user, 'id_tarjeta': id_tarjeta})
            conn.commit()
            cursor.close()
        conn.close()

        print('      [Servicio] Tarjetas actualizadas'.ljust(120, '.'))
        return 'COMPLETE'
        
    except Exception as e:
        print(f'      [Servicio] Error de lógica interna: {e}'.ljust(120, '.'))
        return 'ERROR INTERNO'