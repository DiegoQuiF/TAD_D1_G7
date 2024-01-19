from flask import Blueprint, jsonify, request
from src.services.get.getUsuarios import getUsuarios
from src.services.post.getUsuario import getUsuario
from src.services.post.postRegistrarUsuario import postRegistrarUsuario
from src.services.put.putUsuario import putUsuario
from src.services.delete.delUsuario import delUsuario

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




@main.route('/getUsuario', methods = ['POST'])
def login():
    print('   [Backend] Servicio \'getUsuario\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        correo = data['correo_user']
        contra = data['contra_user']
        print('   [Backend] Ejecutando solicitud de validación...')
        usuarios = getUsuario(correo, contra)
        if len(usuarios)>0 :
            print('   [Backend] Validación exitosa...\n')
            return jsonify({'usuario':usuarios, 'message':'SUCCESS', 'success':True})
        else:
            print('   [Backend] Validación fallida...\n')
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        print('   [Backend] Validación fallida...\n')
        return jsonify({'message':'ERROR', 'success':False})

@main.route('/registrarUsuario', methods = ['POST'])
def registrarUsuario():
    print('   [Backend] Servicio \'registrarUsuario\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        nombre = data['nombre']
        paterno = data['paterno']
        materno = data['materno']
        correo = data['correo']
        contra = data['contra']
        celular = data['celular']
        usuarios = []
        usuarios.append(data)
        print('   [Backend] Ejecutando solicitud de registro...')
        if (postRegistrarUsuario(nombre, paterno, materno, correo, contra, celular)):
            print('   [Backend] Registro exitoso...\n')
            return jsonify({'usuario': usuarios, 'success':True})
        else:
            print('   [Backend] Registro fallido...\n')
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        print('   [Backend] Registro fallido...\n')
        return jsonify({'message':'ERROR', 'success':False})




@main.route('/guardarUsuario', methods = ['PUT'])
def guardarUsuario():
    try:
        data = request.get_json()
        nombre = data['nombre']
        paterno = data['paterno']
        materno = data['materno']
        correo = data['correo']
        contra = data['contra']
        celular = data['celular']
        id = data['id']
        usuarios = []
        usuarios.append(data)
        if (putUsuario(nombre, paterno, materno, correo, contra, celular, id)):
            return jsonify({'usuario': usuarios, 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})




@main.route('/eliminarUsuario/<string:id>', methods = ['DELETE'])
def eliminarUsuario(id):
    try:
        data = { 'id': id , 'id': id }
        usuarios = []
        usuarios.append(data)
        if (delUsuario(id)):
            return jsonify({'usuario': usuarios, 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})