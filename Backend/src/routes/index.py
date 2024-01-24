from flask import Blueprint, jsonify, request
from src.services.get.getUsuarios import getUsuarios
from src.services.get.getMaterialCompleto import getMaterialesCompletos
from src.services.post.getUsuario import getUsuario
from src.services.post.getColeccion import getColeccion
from src.services.post.getMaterial import getMaterial
from src.services.post.postRegistrarUsuario import postRegistrarUsuario
from src.services.post.postRegistrarColeccion import postRegistrarColeccion
from src.services.post.postRegistrarLibro import postRegistrarLibro
from src.services.post.postFactura import postRegistrarFactura
from src.services.put.putUsuario import putUsuario
from src.services.put.putColeccion import putColeccion
from src.services.delete.delUsuario import delUsuario
from src.services.delete.delColeccion import delColeccion
from src.services.delete.delMaterial import delMaterial

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

@main.route('/getMaterialesCompletos/<string:id>')
def obtenerMaterialesCompletos(id):
    try:
        libros = getMaterialesCompletos(id)
        if (len(libros)>0 and libros):
            return jsonify({'materiales': libros, 'success':True})
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

@main.route('/getColeccion', methods = ['POST'])
def colecciones():
    print('   [Backend] Servicio \'getColecciones\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        id = data['id_user']
        print('   [Backend] Ejecutando solicitud...')
        coleccion = getColeccion(id)
        if len(coleccion)>0:
            print('   [Backend] Solicitud exitosa...\n')
            return jsonify({'coleccion':coleccion, 'message':'SUCCESS', 'success':True})
        else:
            print('   [Backend] Validación fallida...\n')
            return jsonify({'message':"NOT FOUND", 'success':True})

    except Exception as e:
        print('   [Backend] Consulta fallida...\n')
        return jsonify({'message':'ERROR', 'success':False})

@main.route('/getMaterial', methods = ['POST'])
def materiales():
    print('   [Backend] Servicio \'getMaterial\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        id = data['id_coleccion']
        print('   [Backend] Ejecutando solicitud...')
        material = getMaterial(id)
        if len(material)>0:
            print('   [Backend] Solicitud exitosa...\n')
            return jsonify({'material':material, 'message':'SUCCESS', 'success':True})
        else:
            print('   [Backend] Validación fallida...\n')
            return jsonify({'message':"NOT FOUND", 'success':True})

    except Exception as e:
        print('   [Backend] Consulta fallida...\n')
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

@main.route('/registrarColeccion', methods = ['POST'])
def registrarColeccion():
    print('   [Backend] Servicio \'registrarColeccion\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        id_user = data['id_user']
        nombre = data['nombre_col']
        tipo = data['tipo_col']
        creacion = data['creacion_col']
        actualizacion = data['actualizacion_col']
        coleccion = []
        coleccion.append(data)
        print('   [Backend] Ejecutando solicitud de registro...')
        if (postRegistrarColeccion(id_user, nombre, tipo, creacion, actualizacion)):
            print('   [Backend] Registro exitoso...\n')
            return jsonify({'coleccion': coleccion, 'success':True})
        else:
            print('   [Backend] Registro fallido...\n')
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        print('   [Backend] Registro fallido...\n')
        return jsonify({'message':'ERROR', 'success':False})
    
@main.route('/registrarLibro', methods = ['POST'])
def registrarLibro():
    print('   [Backend] Servicio \'registrarLibro\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        titulo = data['titulo']
        autor = data['autor']
        hoy = data['hoy']
        idioma = data['idioma']
        procedencia = data['procedencia']
        fechaO = data['fechaO']
        electronico = data['electronico']
        precioE = data['precioE']
        fisico = data['fisico']
        precioF = data['precioF']
        stockF = data['stockF']
        idColeccion = data['id_coleccion']
        libros = []
        libros.append(data)
        print('   [Backend] Ejecutando solicitud de registro...')
        if (postRegistrarLibro(titulo, autor, hoy, idioma, procedencia, fechaO, electronico, precioE, fisico, precioF, stockF, idColeccion)):
            print('   [Backend] Registro exitoso...\n')
            return jsonify({'libro': libros, 'success':True})
        else:
            print('   [Backend] Registro fallido...\n')
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        print('   [Backend] Registro fallido...\n')
        return jsonify({'message':'ERROR', 'success':False})

@main.route('/registrarFactura', methods = ['POST'])
def registrarFactura():
    print('   [Backend] Servicio \'registrarFactura\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        pagado = data['pagado']
        fecha = data['fecha']
        idMaterial = data['id_material']
        idUsuario = data['id_usuario']
        factura = []
        factura.append(data)
        print('   [Backend] Ejecutando solicitud de registro...')
        if postRegistrarFactura(pagado, fecha, idMaterial, idUsuario):
            print('   [Backend] Registro exitoso...\n')
            return jsonify({'factura': factura, 'success':True})
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

@main.route('/guardarColeccion', methods = ['PUT'])
def guardarColeccion():
    try:
        data = request.get_json()
        id = data['id_coleccion']
        nombre = data['nombre_coleccion']
        tipo = data['tipo_coleccion']
        actu = data['actualizacion_coleccion']
        colecciones = []
        colecciones.append(data)
        if (putColeccion(id, nombre, tipo, actu)):
            return jsonify({'coleccion': colecciones, 'success':True})
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

@main.route('/eliminarColeccion/<string:id>', methods = ['DELETE'])
def eliminarColeccion(id):
    try:
        data = { 'id': id , 'id': id }
        colecciones = []
        colecciones.append(data)
        if (delColeccion(id)):
            return jsonify({'coleccion': colecciones, 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})

@main.route('/eliminarMaterial/<string:id>', methods = ['DELETE'])
def eliminarMaterial(id):
    try:
        data = { 'id': id , 'id': id }
        libros = []
        libros.append(data)
        if (delMaterial(id)):
            return jsonify({'libro': libros, 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})