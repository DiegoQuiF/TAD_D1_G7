from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Material(db.db.Model):
    idMat           = db.db.Column(db.db.Integer, primary_key=True)
    titulo          = db.db.Column(db.db.String(100))
    autor           = db.db.Column(db.db.String(120))
    publicacion     = db.db.Column(db.db.String(50))
    idioma          = db.db.Column(db.db.String(50))
    procedencia     = db.db.Column(db.db.String(100))
    original        = db.db.Column(db.db.String(50))
    electronico     = db.db.Column(db.db.String(50))
    precioE         = db.db.Column(db.db.String(50))
    fisico          = db.db.Column(db.db.String(50))
    precioF         = db.db.Column(db.db.String(50))
    stockF          = db.db.Column(db.db.String(50))

    def __init__(self, tit, aut, pub, idi, pro, ori, ele, pre, fis, prf, sto):
        self.titulo     = tit
        self.autor        = aut
        self.publicacion= pub
        self.idioma     = idi
        self.procedencia= pro
        self.original   = ori
        self.electronico= ele
        self.precioE    = pre
        self.fisico     = fis
        self.precioF    = prf
        self.stockF     = sto
    
    def to_json(self):
        return {
            'idMat'         : self.idMat,
            'titulo'        : self.titulo,
            'autor'         : self.autor,
            'publicacion'           : self.publicacion,
            'idioma'        : self.idioma,
            'procedencia'   : self.procedencia,
            'original'        : self.original,
            'electronico'   : self.electronico,
            'precioE'       : self.precioE,
            'fisico'        : self.fisico,
            'precioF'       : self.precioF,
            'stockF'        : self.stockF
        }