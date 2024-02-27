from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class MaterialCategoria(db.db.Model):
    idMC        = db.db.Column(db.db.Integer, primary_key=True)
    idM         = db.db.Column(db.db.String(80))
    nombreC     = db.db.Column(db.db.String(80))

    def __init__(self, idM, nombreC):
        self.idM = idM
        self.nombreC = nombreC
    
    def to_json(self):
        return {
            'idMC': self.idMC,
            'idM': self.idM,
            'nombreC': self.nombreC
        }