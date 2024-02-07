from ..database.db import DatabaseManager

db = DatabaseManager().getInstancia()

class Usuario(db.db.Model):
    idUser      = db.db.Column(db.db.Integer, primary_key=True)
    nomUser     = db.db.Column(db.db.String(50))
    aPatUser    = db.db.Column(db.db.String(50))
    aMatUser    = db.db.Column(db.db.String(50))
    correoUser  = db.db.Column(db.db.String(50))
    contraUser  = db.db.Column(db.db.Text)
    celUser     = db.db.Column(db.db.Integer)

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