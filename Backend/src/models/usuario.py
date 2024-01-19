from src.database.db import db

class Usuario(db.Model):
    idUser      = db.Column(db.Integer, primary_key=True)
    nomUser     = db.Column(db.String(50))
    aPatUser    = db.Column(db.String(50))
    aMatUser    = db.Column(db.String(50))
    correoUser  = db.Column(db.String(50))
    contraUser  = db.Column(db.Text)
    celUser     = db.Column(db.Integer)

    def __init__(self, nom, aPat, aMat, correo, contra, cel):
        self.nomUser    = nom
        self.aPatUser   = aPat
        self.aMatUser   = aMat
        self.correoUser = correo
        self.contraUser = contra
        self.celUser    = cel
    
    def to_json(self):
        return {
            'id_user'       : self.idUser,
            'nom_user'      : self.nomUser,
            'a_pat_user'    : self.aPatUser,
            'a_mat_user'    : self.aMatUser,
            'correo_user'   : self.correoUser,
            'contra_user'   : self.contraUser,
            'cel_user'      : self.celUser
        }