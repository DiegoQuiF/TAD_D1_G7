from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Categoria(db.db.Model):
    idCTC       = db.db.Column(db.db.Integer, primary_key=True)
    idTC        = db.db.Column(db.db.String(80))
    nombreTC    = db.db.Column(db.db.String(80))
    idC         = db.db.Column(db.db.String(80))
    nombreC     = db.db.Column(db.db.String(80))

    def __init__(self, idTC, nombreTC, idC, nombreC):
        self.idTC = idTC
        self.nombreTC = nombreTC
        self.idC = idC
        self.nombreC = nombreC
    
    def to_json(self):
        return {
            'idCTC': self.idCTC,
            'idTC': self.idTC,
            'nombreTC': self.nombreTC,
            'idC': self.idC,
            'nombreC': self.nombreC
        }