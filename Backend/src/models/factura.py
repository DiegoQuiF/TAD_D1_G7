from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Factura(db.db.Model):
    idFact          = db.db.Column(db.db.Integer, primary_key=True)
    pagado          = db.db.Column(db.db.String(50))
    fecha           = db.db.Column(db.db.String(50))

    def __init__(self, pag, fec):
        self.pagado     = pag
        self.fecha      = fec
    
    def to_json(self):
        return {
            'idFact'        : self.idFact,
            'pagado'        : self.pagado,
            'fecha'         : self.fecha
        }