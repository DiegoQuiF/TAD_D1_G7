from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Coleccion(db.db.Model):
    idColeccion     = db.db.Column(db.db.Integer, primary_key=True)
    nombre          = db.db.Column(db.db.String(80))
    tipo            = db.db.Column(db.db.String(80))
    creacion        = db.db.Column(db.db.String(16))
    actualizacion   = db.db.Column(db.db.String(16))

    def __init__(self, nom, tipo, cre, act):
        self.nombre   = nom
        self.tipo           = tipo
        self.creacion       = cre
        self.actualizacion  = act
    
    def to_json(self):
        return {
            'id_coleccion'  : self.idColeccion,
            'nombre'        : self.nombre,
            'tipo'          : self.tipo,
            'creacion'      : self.creacion,
            'actualizacion' : self.actualizacion
        }