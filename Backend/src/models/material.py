from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Material(db.db.Model):
    idMaterial    = db.db.Column(db.db.Integer, primary_key=True)
    titulo          = db.db.Column(db.db.String(160))
    autor           = db.db.Column(db.db.String(160))
    fecha           = db.db.Column(db.db.String(50))
    idioma          = db.db.Column(db.db.String(80))
    procedencia     = db.db.Column(db.db.String(80))
    dispFisico      = db.db.Column(db.db.String(10))
    precioFisico    = db.db.Column(db.db.Float)
    stockFisico     = db.db.Column(db.db.Integer)
    dispElec        = db.db.Column(db.db.String(10))
    precioElec      = db.db.Column(db.db.Float)


    def __init__(self, tit, aut, pub, idi, pro, fis, prf, sto, ele, pre):
        self.titulo         = tit
        self.autor          = aut
        self.fecha          = pub
        self.idioma         = idi
        self.procedencia    = pro
        self.dispFisico     = fis
        self.precioFisico   = prf
        self.stockFisico    = sto
        self.dispElec       = ele
        self.precioElec     = pre
    
    def to_json(self):
        return {
            'idMaterial'  : self.idMaterial,
            'titulo'        : self.titulo,
            'autor'         : self.autor,
            'fecha'           : self.fecha,
            'idioma'        : self.idioma,
            'procedencia'   : self.procedencia,
            'dispFisico'        : self.dispFisico,
            'precioFisico'   : self.precioFisico,
            'stockFisico'       : self.stockFisico,
            'dispElec'        : self.dispElec,
            'precioElec'       : self.precioElec,
        }