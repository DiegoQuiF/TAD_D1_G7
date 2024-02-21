from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Comprador(db.db.Model):
    idUsuario          = db.db.Column(db.db.Integer, primary_key=True)
    comprador          = db.db.Column(db.db.String(160))
    fechaCompra        = db.db.Column(db.db.String(50))
    fechaEntrega       = db.db.Column(db.db.String(50))
    subtotal           = db.db.Column(db.db.Float)
    titulo             = db.db.Column(db.db.String(160))
    catalogo           = db.db.Column(db.db.String(160))

    def __init__(self, com, fec, fee, sub, tit, cat):
        self.idUsuario      = 0
        self.comprador      = com
        self.fechaCompra    = fec
        self.fechaEntrega   = fee
        self.subtotal       = sub
        self.titulo         = tit
        self.catalogo       = cat
    
    def to_json(self):
        return {
            'comprador':        self.comprador,
            'fechaCompra':      self.fechaCompra,
            'fechaEntrega':     self.fechaEntrega,
            'subtotal':         self.subtotal,
            'titulo':           self.titulo,
            'catalogo':         self.catalogo
        }