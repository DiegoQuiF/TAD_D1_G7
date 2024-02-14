import re
from ...database.db import DatabaseManager

db = DatabaseManager().getInstancia()

def postRegistrarLibro(titulo, autor, fecha, idioma, procedencia, dispFisico, precioFisico, stockFisico, dispElec, precioElec, idColeccion):
    precioFisico = str(precioFisico)
    precioElec = str(precioElec)
    stockFisico = str(stockFisico)
    print('      [Registro] Verificando sintaxis de datos ingresados...')
    if verificarDatos(titulo, autor, fecha, idioma, procedencia, dispFisico, precioFisico, stockFisico, dispElec, precioElec, idColeccion):
        try:
            print('      [Registro] Realizando conexión con la base de datos...')
            conn = db.connection()
            print('      [Registro] Ejecutando inserción de nuevo material bibliografico...')
            print('      [Registro] Inserción de material bibliografico...')
            
            inst =  '''
                    WITH nuevo_libro AS (
                        INSERT INTO Material(titulo, autor, fecha, idioma, procedencia,
                            dispFisico, precioFisico, stockFisico, dispElec, precioElec)
                        VALUES(%(titulo)s, %(autor)s, TO_DATE(%(fecha)s, 'DD/MM/YYYY'), %(idioma)s, %(procedencia)s,
                            %(dispFisico)s, %(precioFisico)s, %(stockFisico)s, %(dispElec)s, %(precioElec)s)
                        RETURNING idMaterial
                    )
                    INSERT INTO coleccionMaterial(idColeccion, idMaterial)
                        SELECT %(idColeccion)s, idMaterial FROM nuevo_libro;
                    '''
            with conn.cursor() as cursor:
                cursor.execute(inst, {'titulo': titulo, 'autor': autor, 'fecha': fecha, 'idioma': idioma, 'procedencia':procedencia,
                                      'dispElec':dispElec, 'precioElec':precioElec, 'dispFisico':dispFisico,
                                      'precioFisico':precioFisico, 'stockFisico':stockFisico, 'idColeccion':idColeccion})
                conn.commit()
                cursor.close()
            conn.close()
            print('      [Registro] Inserción ejecutada correctamente...')
            return True
        except Exception as e:
            print('      [Registro] Error de lógica interna:', e)
            return False
    else:
        print('      [Registro] Error: verificador de sintaxis...')
        return False

def verificarDatos(titulo, autor, fecha, idioma, procedencia, dispFisico, precioFisico, stockFisico, dispElec, precioElec, idColeccion):
    try:
        # Patrones de coincidencias
        #patronTitulo = r'^[A-Za-z]([A-Za-z]|\s|\d|\-|\_|[0-9])*$'
        #Titulo ahora acepta cualquier combinación de caracteres
        patronTitulo = r'^.*$'
        #patronAutor = r'^[A-Za-z]([A-Za-z]|\s|\d|[0-9])*$'
        patronAutor = r'^([A-Za-z]|\s)+$'
        patronFechas = r'^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/\d{4}$'
        patronIdioma = r'^(Espanol|Ingles|Portugues)$'
        #patronProcedencia = r'^[A-Za-z]([A-Za-z]|\s|\d|[0-9])*$'
        patronProcedencia = r'^([A-Za-z]|\s)+$'
        patronSiNo = r'^(Si|No)$'
        patronNumReal = r'^\d+\.\d+$'
        patronNumEntero = r'^\d+$'
        patron80 = r'^.{0,80}$'
        patron160 = r'^.{0,160}$'

    
        # Resultado de las comprobaciones
        resultado1 = re.match(patronTitulo, titulo)
        resultado2 = re.match(patronAutor, autor)
        resultado3 = re.match(patronFechas, fecha)
        resultado4 = re.match(patronIdioma, idioma)
        resultado5 = re.match(patronProcedencia, procedencia)
        resultado7 = re.match(patronSiNo, dispElec)
        resultado8 = re.match(patronNumReal, precioElec)
        resultado9 = re.match(patronSiNo, dispFisico)
        resultado10 = re.match(patronNumReal, precioFisico)
        resultado11 = re.match(patronNumEntero, stockFisico)
        resultado12 = re.match(patron160, titulo)
        resultado13 = re.match(patron160, autor)
        resultado14 = re.match(patron80, procedencia)
    
    except Exception as e:
        print(e)

    print('         [VerificadorS] Ejecutando verificaciones de los datos...')
    if resultado1 and resultado2 and resultado3 and resultado4 and resultado5 and resultado7 and resultado8 and resultado9 and resultado10 and resultado11 and resultado12 and resultado13 and resultado14:
        print('         [VerificadorS] Sintaxis validada...')
        return True
    else:
        print('         [VerificadorS] Error: sintaxis de datos errónea...')
        return False











