from flask import Blueprint, jsonify, request
from src.services.get.getUsuarios import getUsuarios

main = Blueprint('index_blueprint', __name__)

@main.route('/')
def inicio():
    try:
        usuarios = getUsuarios()
        if len(usuarios)>0 :
            return jsonify({'usuarios':usuarios, 'message':'SUCCESS', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})
