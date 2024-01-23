from src.database.db import db

class Coleccion(db.Model):
    idCol       = db.Column(db.Integer, primary_key=True)
    nomCol      = db.Column(db.String(100))
    tipoCol     = db.Column(db.String(50))
    creCol      = db.Column(db.String(50))
    actCol      = db.Column(db.String(50))

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