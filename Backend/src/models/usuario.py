from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Usuario(db.db.Model):
    idUser      = db.db.Column(db.db.Integer, primary_key=True)
    nomUser     = db.db.Column(db.db.String(80))
    aPatUser    = db.db.Column(db.db.String(80))
    aMatUser    = db.db.Column(db.db.String(80))
    correoUser  = db.db.Column(db.db.String(80))
    contraUser  = db.db.Column(db.db.Text)
    celUser     = db.db.Column(db.db.Integer)
    direccion   = db.db.Column(db.db.String(160))

    def __init__(self, nom, aPat, aMat, correo, contra, cel, direccion):
        self.nomUser    = nom
        self.aPatUser   = aPat
        self.aMatUser   = aMat
        self.correoUser = correo
        self.contraUser = contra
        self.celUser    = cel
        self.direccion  = direccion
    
    def to_json(self):
        return {
            'id_user'       : self.idUser,
            'nom_user'      : self.nomUser,
            'a_pat_user'    : self.aPatUser,
            'a_mat_user'    : self.aMatUser,
            'correo_user'   : self.correoUser,
            'contra_user'   : self.contraUser,
            'cel_user'      : self.celUser,
            'direc_user'    : self.direccion
        }