from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Coleccion(db.db.Model):
    idCol       = db.db.Column(db.db.Integer, primary_key=True)
    nomCol      = db.db.Column(db.db.String(100))
    tipoCol     = db.db.Column(db.db.String(50))
    creCol      = db.db.Column(db.db.String(50))
    actCol      = db.db.Column(db.db.String(50))

    def __init__(self, nom, tipo, cre, act):
        self.nomCol     = nom
        self.tipoCol    = tipo
        self.creCol     = cre
        self.actCol     = act
    
    def to_json(self):
        return {
            'id_col'        : self.idCol,
            'nombre_col'    : self.nomCol,
            'tipo_col'      : self.tipoCol,
            'creacion_col'  : self.creCol,
            'actu_col'      : self.actCol
        }