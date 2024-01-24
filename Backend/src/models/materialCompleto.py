from src.database.db import db

class MaterialCompleto(db.Model):
    idMat           = db.Column(db.Integer, primary_key=True)
    tituloMat       = db.Column(db.String(100))
    autorMat        = db.Column(db.String(120))
    originalMat     = db.Column(db.String(50))
    idiomaMat       = db.Column(db.String(50))
    electronicoMat  = db.Column(db.String(50))
    precioEMat      = db.Column(db.String(50))
    fisicoMat       = db.Column(db.String(50))
    precioFMat      = db.Column(db.String(50))
    idCol           = db.Column(db.String(50))
    nombreCol       = db.Column(db.String(50))
    tipoCol         = db.Column(db.String(50))
    idUsu           = db.Column(db.String(50))
    nombreUsu       = db.Column(db.String(50))
    aPatUsu         = db.Column(db.String(50))
    aMatUsu         = db.Column(db.String(50))

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