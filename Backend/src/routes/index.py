from flask import Blueprint, jsonify, request
from src.services.get.getFacturasPorFecha import getFacturasPorFecha
from src.services.get.getMaterialesPorAnio import getMaterialesPorAnio
from src.services.get.getMaterialesPorUsuario import getMaterialesPorUsuario
from src.services.get.getUsuarios import getUsuarios
from src.services.get.getMaterialCompleto import getMaterialesCompletos
from src.services.get.getCarritoCompleto import getCarritoCompleto
from src.services.get.getVentasTotales import getVentasTotales
from src.services.get.getMetricas import getMetricas
from src.services.get.getCategorias import getCategorias
from src.services.post.getComprados import getComprados
from src.services.post.getUsuario import getUsuario
from src.services.post.getTarjetas import getTarjetas
from src.services.post.getColeccion import getColeccion
from src.services.post.getMaterial import getMaterial
from src.services.post.getTransacciones import getTransacciones
from src.services.post.getCompradores import getCompradores
from src.services.post.getCategoriasMaterial import getCategoriasMaterial
from src.services.post.getCategoriasTienda import getCategoriasTienda
from src.services.post.postRegistrarUsuario import postRegistrarUsuario
from src.services.post.postRegistrarColeccion import postRegistrarColeccion
from src.services.post.postRegistrarLibro import postRegistrarLibro
from src.services.post.postFactura import postRegistrarFactura
from src.services.post.postRecargarTarjeta import postRecargarTarjeta
from src.services.post.postTarjeta import postTarjeta
from src.services.post.postRegistrarCarrito import postRegistrarCarrito
from src.services.post.postCategoria import postCategoria
from src.services.post.delCategoria import delCategoria
from src.services.put.putUsuario import putUsuario
from src.services.put.putColeccion import putColeccion
from src.services.put.putPredeterminadoTarjeta import putPredeterminadoTarjeta
from src.services.delete.delUsuario import delUsuario
from src.services.delete.delColeccion import delColeccion
from src.services.delete.delMaterial import delMaterial
from src.services.delete.delTarjeta import delTarjeta


main = Blueprint('index_blueprint', __name__)




# Página login-register

@main.route('/getUsuario', methods = ['POST'])      # Logueo en la página
def login():

    print(' [Backend] Servicio \'getUsuario\' solicitado'.ljust(120, '.'))
    try:

        print(' [Backend] Recepcionando archivo JSON'.ljust(120, '.'))
        data = request.get_json()
        correo = data['correo']
        contra = data['contra']

        print(' [Backend] Ejecutando solicitud de validación'.ljust(120, '.'))
        usuarios = getUsuario(correo, contra)

        if len(usuarios)>0 :
            print(' [Backend] Usuario encontrado'.ljust(120, '.'))
            return jsonify({'usuario':usuarios, 'message':'COMPLETE', 'success':True})
        
        else:
            print(' [Backend] Usuario no encontrado'.ljust(120, '.'))
            return jsonify({'message':"NOT FOUND", 'success':True})
        
    except Exception as e:

        print(f' [Backend] Validación fallida: {e}'.ljust(120, '.'))
        return jsonify({'message':'ERROR', 'success':False})
    

@main.route('/registrarUsuario', methods = ['POST'])        # Registro en la página
def registrarUsuario():

    print(' [Backend] Servicio \'registrarUsuario\' solicitado'.ljust(120, '.'))
    try:

        print(' [Backend] Recepcionando archivo JSON'.ljust(120, '.'))
        data = request.get_json()
        nombre = data['nombre']
        paterno = data['paterno']
        materno = data['materno']
        correo = data['correo']
        contra = data['contra']
        celular = data['celular']
        direccion = data['direccion']

        print(' [Backend] Ejecutando solicitud de registro'.ljust(120, '.'))
        mensaje = postRegistrarUsuario(nombre, paterno, materno, correo, contra, celular, direccion)

        if mensaje == 'COMPLETE':
            print(' [Backend] Registro exitoso'.ljust(120, '.'))
            return jsonify({'message':mensaje, 'success':True})
        
        else:
            print(' [Backend] Registro fallido'.ljust(120, '.'))
            return jsonify({'message':mensaje, 'success':True})
    
    except Exception as e:

        print(f' [Backend] Registro fallido: {e}'.ljust(120, '.'))
        return jsonify({'message':'ERROR', 'success':False})



# Página logueado

# Perfil

@main.route('/guardarUsuario', methods = ['PUT'])       # Actualizar usuario
def guardarUsuario():
    print(' [Backend] Servicio \'guardarUsuario\' solicitado'.ljust(120, '.'))

    try:

        print(' [Backend] Recepcionando archivo JSON'.ljust(120, '.'))
        data = request.get_json()
        nombre = data['nombre']
        paterno = data['paterno']
        materno = data['materno']
        correo = data['correo']
        contra = data['contra']
        celular = data['celular']
        direccion = data['direccion']
        id = data['id']

        print(' [Backend] Ejecutando solicitud de actualización'.ljust(120, '.'))
        mensaje = putUsuario(nombre, paterno, materno, correo, contra, celular, direccion, id)

        if mensaje == 'COMPLETE':
            print(' [Backend] Actualización exitosa'.ljust(120, '.'))
            return jsonify({'message':mensaje, 'success':True})
        
        else:
            print(' [Backend] Actualización fallida'.ljust(120, '.'))
            return jsonify({'message':mensaje, 'success':True})
        
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})


@main.route('/getTarjetas', methods = ['POST'])      # Obtener tarjetas de un usuario
def tarjetas():

    print(' [Backend] Servicio \'getTarjetas\' solicitado'.ljust(120, '.'))
    try:

        print(' [Backend] Recepcionando archivo JSON'.ljust(120, '.'))
        data = request.get_json()
        id = data['id_user']

        print(' [Backend] Ejecutando solicitud'.ljust(120, '.'))
        tarjetas = getTarjetas(id)

        if len(tarjetas)>0 :
            print(' [Backend] Tarjetas encontradas'.ljust(120, '.'))
            return jsonify({'tarjetas':tarjetas, 'message':'COMPLETE', 'success':True})
        
        else:
            print(' [Backend] El usuario no cuenta con tarjetas'.ljust(120, '.'))
            return jsonify({'message':"NOT FOUND", 'success':True})
        
    except Exception as e:

        print(f' [Backend] Servicio fallido: {e}'.ljust(120, '.'))
        return jsonify({'message':'ERROR', 'success':False})


@main.route('/eliminarTarjeta/<string:id>', methods = ['DELETE'])      # eliminarTarjeta
def deleteTarjeta(id):

    print(' [Backend] Servicio \'eliminarTarjeta\' solicitado'.ljust(120, '.'))
    try:

        print(' [Backend] Ejecutando solicitud'.ljust(120, '.'))

        if delTarjeta(id):
            print(' [Backend] Solicitud exitosa'.ljust(120, '.'))
            return jsonify({'message':'COMPLETE', 'success':True})
        
        else:
            return jsonify({'message':"FALLIDO", 'success':True})
        
    except Exception as e:

        print(f' [Backend] Servicio fallido: {e}'.ljust(120, '.'))
        return jsonify({'message':'ERROR', 'success':False})


@main.route('/recargarTarjeta', methods = ['POST'])      # recargarTarjeta
def recargaT():

    print(' [Backend] Servicio \'recargarTarjeta\' solicitado'.ljust(120, '.'))
    try:

        print(' [Backend] Recepcionando archivo JSON'.ljust(120, '.'))
        data = request.get_json()
        id = data['id_tarjeta']
        monto = data['monto_tarjeta']

        print(' [Backend] Ejecutando solicitud'.ljust(120, '.'))

        if postRecargarTarjeta(id, monto):
            print(' [Backend] Recarga exitosa'.ljust(120, '.'))
            return jsonify({'message':'COMPLETE', 'success':True})
        
        else:
            print(' [Backend] Recarga exitosa'.ljust(120, '.'))
            return jsonify({'message':"FALLIDO", 'success':True})
        
    except Exception as e:

        print(f' [Backend] Servicio fallido: {e}'.ljust(120, '.'))
        return jsonify({'message':'ERROR', 'success':False})


@main.route('/registrarTarjeta', methods = ['POST'])       # registrar tarjeta
def registrarTarjeta():
    print(' [Backend] Servicio \'registrarTarjeta\' solicitado'.ljust(120, '.'))

    try:

        print(' [Backend] Recepcionando archivo JSON'.ljust(120, '.'))
        data = request.get_json()
        id_user = data['id_user']
        numero_tar = data['numero_tar']
        caducidad_tar = data['caducidad_tar']
        cvv_tar = data['cvv_tar']
        saldo_tar = data['saldo_tar']

        print(' [Backend] Ejecutando solicitud de registro'.ljust(120, '.'))
        mensaje = postTarjeta(id_user, numero_tar, caducidad_tar, cvv_tar, saldo_tar)

        if mensaje == 'COMPLETE':
            print(' [Backend] Registro exitoso'.ljust(120, '.'))
            return jsonify({'message':mensaje, 'success':True})
        
        else:
            print(' [Backend] Actualización fallida'.ljust(120, '.'))
            return jsonify({'message':mensaje, 'success':True})
        
    except Exception as e:
        return jsonify({'message':'ERROR '+f'{e}', 'success':False})


@main.route('/cambiarPredeterminado', methods = ['POST'])       # registrar tarjeta
def cambiarPredeterminado():
    print(' [Backend] Servicio \'cambiarPredeterminado\' solicitado'.ljust(120, '.'))

    try:

        print(' [Backend] Recepcionando archivo JSON'.ljust(120, '.'))
        data = request.get_json()
        id_user = data['id_user']
        id_tarjeta = data['id_tarjeta']

        print(' [Backend] Ejecutando solicitud de registro'.ljust(120, '.'))
        mensaje = putPredeterminadoTarjeta(id_user, id_tarjeta)

        if mensaje == 'COMPLETE':
            print(' [Backend] Actualización exitoza'.ljust(120, '.'))
            return jsonify({'message':mensaje, 'success':True})
        
        else:
            print(' [Backend] Actualización fallida'.ljust(120, '.'))
            return jsonify({'message':mensaje, 'success':True})
        
    except Exception as e:
        return jsonify({'message':'ERROR '+f'{e}', 'success':False})


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
            return jsonify({'coleccion':coleccion, 'message':'COMPLETE', 'success':True})
        else:
            print('   [Backend] Validación fallida...\n')
            return jsonify({'message':"NOT FOUND", 'success':True})

    except Exception as e:
        print('   [Backend] Consulta fallida...\n')
        return jsonify({'message':'ERROR', 'success':False})
    

@main.route('/registrarColeccion', methods = ['POST'])
def registrarColeccion():
    print('   [Backend] Servicio \'registrarColeccion\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        id_user = data['id_user']
        nombre = data['nombre']
        tipo = data['tipo']
        creacion = data['creacion']
        actualizacion = data['actualizacion']
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
    

@main.route('/guardarColeccion', methods = ['PUT'])
def guardarColeccion():
    try:
        data = request.get_json()
        id = data['id_coleccion']
        nombre = data['nombre']
        tipo = data['tipo']
        actualizacion = data['actualizacion']
        colecciones = []
        colecciones.append(data)
        if (putColeccion(id, nombre, tipo, actualizacion)):
            return jsonify({'coleccion': colecciones, 'success':True})
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


@main.route('/registrarLibro', methods = ['POST'])
def registrarLibro():
    print('   [Backend] Servicio \'registrarLibro\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        idColeccion = data['idColeccion']
        titulo = data['titulo']
        autor = data['autor']
        fecha = data['fecha']
        idioma = data['idioma']
        procedencia = data['procedencia']
        dispFisico = data['dispFisico']
        precioFisico = data['precioFisico']
        stockFisico = data['stockFisico']
        dispElec = data['dispElec']
        precioElec = data['precioElec']

        libros = []
        libros.append(data)
        print('   [Backend] Ejecutando solicitud de registro...')
        if (postRegistrarLibro(titulo, autor, fecha, idioma, procedencia, dispFisico, precioFisico, stockFisico, dispElec, precioElec, idColeccion)):
            print('   [Backend] Registro exitoso...\n')
            return jsonify({'libro': libros, 'success':True})
        else:
            print('   [Backend] Registro fallido...\n')
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        print('   [Backend] Registro fallido...\n')
        return jsonify({'message':'ERROR', 'success':False})


@main.route('/getMaterial', methods = ['POST'])
def materiales():
    print('   [Backend] Servicio \'getMaterial\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        id = data['id_user']
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
    
@main.route('/getComprados', methods = ['POST'])
def comprados():
    try:
        data = request.get_json()
        id = data['id_user']
        comprados = getComprados(id)
        if len(comprados)>0:
            return jsonify({'comprados':comprados, 'message':'SUCCESS', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})
    
@main.route('/delCategoria', methods = ['POST'])
def deleteCategoria():
    try:
        data = request.get_json()
        idMC = data['idMC']
        if delCategoria(idMC):
            return jsonify({'message':'SUCCESS', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':False})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})
    
@main.route('/agregarCategoria', methods = ['POST'])
def addCategoria():
    try:
        data = request.get_json()
        idM = data['idM']
        idC = data['idC']
        if postCategoria(idM, idC):
            return jsonify({'message':'SUCCESS', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':False})
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
    
@main.route('/getCategorias')
def obtenerCategorias():
    try:
        categorias = getCategorias()
        if (len(categorias)>0 and categorias):
            return jsonify({'categorias': categorias, 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})


@main.route('/registrarCarrito', methods = ['POST'])
def registrarCarrito():
    print('   [Backend] Servicio \'registrarCarrito\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        id_material = data['id_material']
        id_user = data['id_user']

        carrito = []
        carrito.append(data)
        print('   [Backend] Ejecutando solicitud de registro...')
        if (postRegistrarCarrito(id_material, id_user)):
            print('   [Backend] Registro exitoso...\n')
            return jsonify({'carrito': carrito, 'success':True})
        else:
            print('   [Backend] Registro fallido...\n')
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        print('   [Backend] Registro fallido...\n')
        return jsonify({'message':'ERROR', 'success':False})


@main.route('/getCarritoCompleto/<string:id>')
def obtenerCarritoCompleto(id):
    try:
        libros = getCarritoCompleto(id)
        if (len(libros)>0 and libros):
            return jsonify({'carrito': libros, 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})
    




@main.route('/registrarFactura', methods = ['POST'])
def registrarFactura():
    print('   [Backend] Servicio \'registrarFactura\' solicitado...')
    try:
        print('   [Backend] Recepcionando archivo JSON...')
        data = request.get_json()
        fechaC = data['fechaC']
        fechaE = data['fechaE']
        idMaterial = data['id_material']
        idUsuario = data['id_usuario']
        factura = []
        factura.append(data)
        print('   [Backend] Ejecutando solicitud de registro...')
        if postRegistrarFactura(fechaC, fechaE, idMaterial, idUsuario):
            print('   [Backend] Registro exitoso...\n')
            return jsonify({'factura': factura, 'success':True})
        else:
            print('   [Backend] Registro fallido...\n')
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        print('   [Backend] Registro fallido...\n')
        return jsonify({'message':'ERROR', 'success':False})





# ETL
@main.route('/getMaterialesPorAnio')
def obtenerMaterialesPorAnio():
    try:
        materialesPorAnio = getMaterialesPorAnio()
        if len(materialesPorAnio)>0 :
            return jsonify({'materialesPorAnio':materialesPorAnio, 'message':'SUCCESS', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})
    
@main.route('/getFacturasPorFecha')
def obtenerFacturasPorFecha():
    try:
        facturasPorFecha = getFacturasPorFecha()
        if len(facturasPorFecha)>0 :
            return jsonify({'facturasPorFecha':facturasPorFecha, 'message':'SUCCESS', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})
    
@main.route('/getMaterialesPorUsuario')
def obtenerMaterialesPorUsuario():
    try:
        materialesPorUsuario = getMaterialesPorUsuario()
        if len(materialesPorUsuario)>0 :
            return jsonify({'materialesPorUsuario':materialesPorUsuario, 'message':'SUCCESS', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})

@main.route('/getVentasTotales')
def obtenerVentasTotales():
    try:
        ventasTotales = getVentasTotales()
        if len(ventasTotales)>0 :
            return jsonify({'ventasTotales':ventasTotales, 'message':'SUCCESS', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})
    
@main.route('/getMetricas')
def obtenerMetricas():
    try:
        metricas = getMetricas()
        if len(metricas)>0 :
            return jsonify({'metricas':metricas, 'message':'SUCCESS', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        return jsonify({'message':'ERROR', 'success':False})




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

@main.route('/getTransacciones', methods = ['POST'])
def getTransaccion():
    print('   [Backend] Servicio \'getTransacciones\' solicitado'.ljust(120, '.'))
    try:
        print('   [Backend] Recepcionando archivo JSON'.ljust(120, '.'))
        data = request.get_json()
        id = data['id_user']
        print('   [Backend] Ejecutando solicitud'.ljust(120, '.'))
        transaccion = getTransacciones(id)
        if len(transaccion)>0:
            print('   [Backend] Solicitud exitosa'.ljust(120, '.'))
            return jsonify({'transaccion':transaccion, 'message':'COMPLETE', 'success':True})
        else:
            print('   [Backend] Solicitud fallida: NOT FOUND'.ljust(120, '.'))
            return jsonify({'message':"NOT FOUND", 'success':True})

    except Exception as e:
        print('   [Backend] Solicitud fallida: ERROR'.ljust(120, '.'))
        return jsonify({'message':'ERROR', 'success':False})

@main.route('/getCompradores', methods = ['POST'])
def getComprador():
    print('   [Backend] Servicio \'getCompradores\' solicitado'.ljust(120, '.'))
    try:
        print('   [Backend] Recepcionando archivo JSON'.ljust(120, '.'))
        data = request.get_json()
        id = data['id_user']
        print('   [Backend] Ejecutando solicitud'.ljust(120, '.'))
        compradores = getCompradores(id)
        if len(compradores)>0:
            print('   [Backend] Solicitud exitosa'.ljust(120, '.'))
            return jsonify({'compradores':compradores, 'message':'COMPLETE', 'success':True})
        else:
            print('   [Backend] Solicitud fallida: NOT FOUND'.ljust(120, '.'))
            return jsonify({'message':"NOT FOUND", 'success':True})

    except Exception as e:
        print('   [Backend] Solicitud fallida: ERROR'.ljust(120, '.'))
        return jsonify({'message':'ERROR', 'success':False})
    
@main.route('/getMaterialCategoria', methods = ['POST'])
def getMaterialCategorias():
    try:
        data = request.get_json()
        id = data['id_user']
        materialesCategoria = getCategoriasMaterial(str(id))
        if len(materialesCategoria)>0:
            return jsonify({'materialCategorias':materialesCategoria, 'message':'COMPLETE', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        print(e)
        return jsonify({'message':'ERROR', 'success':False})
    
@main.route('/getCategoriasTienda', methods = ['POST'])
def getCategoriasT():
    try:
        data = request.get_json()
        id = data['id_user']
        tiendaCategorias = getCategoriasTienda(str(id))
        if len(tiendaCategorias)>0:
            return jsonify({'categoriasTienda':tiendaCategorias, 'message':'COMPLETE', 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as e:
        print(e)
        return jsonify({'message':'ERROR', 'success':False})