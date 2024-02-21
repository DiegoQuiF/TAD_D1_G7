from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Transaccion(db.db.Model):
    idTransacciones     = db.db.Column(db.db.Integer, primary_key=True)
    nro_publicaciones   = db.db.Column(db.db.Integer)
    nro_compras         = db.db.Column(db.db.Integer)
    recaudado           = db.db.Column(db.db.Float)

    def __init__(self, pub, com, rec):
        self.idTransacciones = 0
        self.nro_publicaciones  = pub
        self.nro_compras  = com
        self.recaudado  = rec
    
    def to_json(self):
        return {
            'nro_publicaciones' : self.nro_publicaciones,
            'nro_compras'       : self.nro_compras,
            'recaudado'         : self.recaudado
        }