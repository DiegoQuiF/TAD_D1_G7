from src.database.db import db

class Factura(db.Model):
    idFact          = db.Column(db.Integer, primary_key=True)
    pagado          = db.Column(db.String(50))
    fecha           = db.Column(db.String(50))

    def __init__(self, pag, fec):
        self.pagado     = pag
        self.fecha      = fec
    
    def to_json(self):
        return {
            'idFact'        : self.idFact,
            'pagado'        : self.pagado,
            'fecha'         : self.fecha
        }