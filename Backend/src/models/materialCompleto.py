from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class MaterialCompleto(db.db.Model):
    idMat           = db.db.Column(db.db.Integer, primary_key=True)
    tituloMat       = db.db.Column(db.db.String(100))
    autorMat        = db.db.Column(db.db.String(120))
    originalMat     = db.db.Column(db.db.String(50))
    idiomaMat       = db.db.Column(db.db.String(50))
    electronicoMat  = db.db.Column(db.db.String(50))
    precioEMat      = db.db.Column(db.db.String(50))
    fisicoMat       = db.db.Column(db.db.String(50))
    precioFMat      = db.db.Column(db.db.String(50))
    idCol           = db.db.Column(db.db.String(50))
    nombreCol       = db.db.Column(db.db.String(50))
    tipoCol         = db.db.Column(db.db.String(50))
    idUsu           = db.db.Column(db.db.String(50))
    nombreUsu       = db.db.Column(db.db.String(50))
    aPatUsu         = db.db.Column(db.db.String(50))
    aMatUsu         = db.db.Column(db.db.String(50))

    def __init__(self, tituloMat, autorMat, originalMat, idiomaMat, electronicoMat, precioEMat, fisicoMat, precioFMat, idCol, nombreCol, tipoCol, idUsu, nombreUsu, aPatUsu, aMatUsu):
        self.tituloMat = tituloMat
        self.autorMat = autorMat
        self.originalMat = originalMat
        self.idiomaMat = idiomaMat
        self.electronicoMat = electronicoMat
        self.precioEMat = precioEMat
        self.fisicoMat = fisicoMat
        self.precioFMat = precioFMat
        self.idCol = idCol
        self.nombreCol = nombreCol
        self.tipoCol = tipoCol
        self.idUsu = idUsu
        self.nombreUsu = nombreUsu
        self.aPatUsu = aPatUsu
        self.aMatUsu = aMatUsu
    
    def to_json(self):
        return {
            'idMat': self.idMat,
            'tituloMat': self.tituloMat,
            'autorMat': self.autorMat,
            'originalMat': self.originalMat,
            'idiomaMat': self.idiomaMat,
            'electronicoMat': self.electronicoMat,
            'precioEMat': self.precioEMat,
            'fisicoMat': self.fisicoMat,
            'precioFMat': self.precioFMat,
            'idCol': self.idCol,
            'nombreCol': self.nombreCol,
            'tipoCol': self.tipoCol,
            'idUsu': self.idUsu,
            'nombreUsu': self.nombreUsu,
            'aPatUsu': self.aPatUsu,
            'aMatUsu': self.aMatUsu,
        }