from ...database.db import DatabaseManager
from src.models.materialCategoria import MaterialCategoria

db = DatabaseManager().getInstancia()

def getCategoriasTienda(id):
    try:
        conn = db.connection()
        MCs = []
        inst =  '''
                select MC.idMaterialCategoria, MB.idMaterial, CA.nombre
                    from MaterialCategoria MC, Categoria CA, Material MB, ColeccionMaterial CM, UsuarioColeccion UC, coleccion CO
                    where MB.idMaterial = MC.idMaterial and MC.idCategoria = CA.idCategoria
                        and CM.idMaterial = MB.idMaterial and UC.idColeccion = CM.idColeccion
                        and CO.idColeccion = CM.idColeccion and CO.tipo = 'Publica'
                        and UC.idUsuario not in (%(id)s);
                '''
        with conn.cursor() as cursor:
            cursor.execute(inst, {'id':id})
            for row in cursor.fetchall():
                MaterialCat = MaterialCategoria(row[1], row[2])
                MaterialCat.idMC = row[0]
                MCs.append(MaterialCat.to_json())
            conn.commit()
            cursor.close()
        conn.close()
        return MCs
    except Exception as e:
        print("(SISTEMA)   Error: " + e)




