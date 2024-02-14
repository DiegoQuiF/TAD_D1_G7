from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Tarjeta(db.db.Model):
    idTarjeta       = db.db.Column(db.db.Integer, primary_key=True)
    numero          = db.db.Column(db.db.String(19))
    caducidad       = db.db.Column(db.db.String(20))
    cvv             = db.db.Column(db.db.Integer)
    saldo           = db.db.Column(db.db.Float)
    predeterminada  = db.db.Column(db.db.String(10))

    def __init__(self, numero, caducidad, cvv, saldo, predeterminada):
        self.numero         = numero
        self.caducidad      = caducidad
        self.cvv            = cvv
        self.saldo          = saldo
        self.predeterminada = predeterminada
    
    def to_json(self):
        return {
            'id'            : self.idTarjeta,
            'numero'        : self.numero,
            'caducidad'     : self.caducidad,
            'cvv'           : self.cvv,
            'saldo'         : self.saldo,
            'predeterminada': self.predeterminada,
        }