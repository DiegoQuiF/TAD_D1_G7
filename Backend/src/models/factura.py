from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Factura(db.db.Model):
    idFact          = db.db.Column(db.db.Integer, primary_key=True)
    pagado          = db.db.Column(db.db.String(50))
    fechaC           = db.db.Column(db.db.String(50))
    fechaE           = db.db.Column(db.db.String(50))

    def __init__(self, pag, fec, fer):
        self.pagado     = pag
        self.fechaC      = fec
        self.fechaE     = fer
    
    def to_json(self):
        return {
            'idFact'        : self.idFact,
            'pagado'        : self.pagado,
            'fechaC'         : self.fechaC,
            'fechaE'        : self.fechaE
        }