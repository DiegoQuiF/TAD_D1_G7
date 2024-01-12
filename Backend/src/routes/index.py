from flask import Blueprint, jsonify, request
from src.services.get.getUsuarios import getUsuarios
from src.services.get.getUsuario import getUsuario

main = Blueprint('index_blueprint', __name__)

@main.route('/getUsuarios')
def inicio():
    try:
        usuarios = getUsuarios()
        if len(usuarios)>0 :
            return jsonify({'usuarios':usuarios, 'message':'SUCCESS', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})

@main.route('/getUsuario/<string:correo>/<string:contrasenia>')
def login(correo, contrasenia):
    try:
        usuarios = getUsuario(correo, contrasenia)
        if len(usuarios)>0 :
            return jsonify({'usuario':usuarios, 'message':'SUCCESS', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})