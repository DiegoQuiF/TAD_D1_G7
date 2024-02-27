from ...database.db import DatabaseManager
from src.models.categoria import Categoria

db = DatabaseManager().getInstancia()

def getCategorias():
    try:
        conn = db.connection()
        categorias = []
        inst =  '''
                select CTC.idCategoriaTipoCategoria, TC.idTipoCategoria, TC.nombre, CA.idCategoria, CA.nombre
                    from tipoCategoria TC, categoria CA, categoriaTipoCategoria CTC
                    where TC.idTipoCategoria = CTC.idTipoCategoria
                        and CTC.idCategoria = CA.idCategoria;
                '''
        with conn.cursor() as cursor:
            cursor.execute(inst,)
            for row in cursor.fetchall():
                categoria = Categoria(row[1], row[2], row[3], row[4])
                categoria.idCTC = row[0]
                categorias.append(categoria.to_json())
            conn.commit()
            cursor.close()
        conn.close()
        return categorias
    except Exception as e:
        print("(SISTEMA)   Error: " + e)
