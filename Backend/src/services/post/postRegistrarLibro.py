import re
from src.database.db import connection

def postRegistrarLibro(titulo, autor, hoy, idioma, procedencia, fechaO, electronico, precioE, fisico, precioF, sotckF, idColeccion):
    print('      [Registro] Verificando sintaxis de datos ingresados...')
    if verificarDatos(titulo, autor, hoy, idioma, procedencia, fechaO, electronico, precioE, fisico, precioF, sotckF):
        try:
            print('      [Registro] Realizando conexión con la base de datos...')
            conn = connection()
            print('      [Registro] Ejecutando inserción de nuevo material bibliografico...')
            print('      [Registro] Inserción de material bibliografico...')
            
            inst =  '''
                    WITH nuevo_libro AS (
                        INSERT INTO materialBibliografico(nombreMaterial, autorMaterial, fechaPubMaterial, idiomaMaterial,
                            procedenciaMaterial, fechaPubOrigMaterial, electronicoMaterial, precioEMaterial,
                            fisicoMaterial, precioFMaterial, stockMaterial)
                        VALUES(%(titulo)s, %(autor)s, TO_DATE(%(hoy)s, 'DD/MM/YYYY'), %(idioma)s, %(procedencia)s,
                            TO_DATE(%(fechaO)s, 'DD/MM/YYYY'), %(electronico)s, %(precioE)s, %(fisico)s, %(precioF)s, %(stockF)s)
                        RETURNING idMaterial
                    )
                    INSERT INTO coleccionMaterial(idColeccion, idMaterial)
                        SELECT %(idColeccion)s, idMaterial FROM nuevo_libro;
                    '''
            with conn.cursor() as cursor:
                cursor.execute(inst, {'titulo': titulo, 'autor': autor, 'hoy': hoy, 'idioma': idioma, 'procedencia':procedencia,
                                      'fechaO': fechaO, 'electronico':electronico, 'precioE':precioE, 'fisico':fisico,
                                      'precioF':precioF, 'stockF':sotckF, 'idColeccion':idColeccion})
                conn.commit()
            print('      [Registro] Inserción ejecutada correctamente...')
            return True
        except Exception as e:
            print('      [Registro] Error de lógica interna:', e)
            return False
    else:
        print('      [Registro] Error: verificador de sintaxis...')
        return False

def verificarDatos(titulo, autor, hoy, idioma, procedencia, fechaO, electronico, precioE, fisico, precioF, stockF):
    # Patrones de coincidencias
    #patronTitulo = r'^[A-Za-z]([A-Za-z]|\s|\d|\-|\_|[0-9])*$'
    patronTitulo = r'^.*$'
    #patronAutor = r'^[A-Za-z]([A-Za-z]|\s|\d|[0-9])*$'
    patronAutor = r'^[A-Za-zñÑáéíóúÁÉÍÓÚüÜ\s,]+$'
    patronFechas = r'^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/\d{4}$'
    patronIdioma = r'^(Espanol|Ingles|Portugues)$'
    #patronProcedencia = r'^[A-Za-z]([A-Za-z]|\s|\d|[0-9])*$'
    patronProcedencia = r'^[A-Za-zñÑáéíóúÁÉÍÓÚüÜ\s,]+$'
    patronSiNo = r'^(Si|No)$'
    patronNumReal = r'^\d+\.\d+$'
    patronNumEntero = r'^\d+$'
    patron100 = r'^.{0,99}$'
    patron120 = r'^.{0,119}$'

    # Resultado de las comprobaciones
    resultado1 = re.match(patronTitulo, titulo)
    resultado2 = re.match(patronAutor, autor)
    resultado3 = re.match(patronFechas, hoy)
    resultado4 = re.match(patronIdioma, idioma)
    resultado5 = re.match(patronProcedencia, procedencia)
    resultado6 = re.match(patronFechas, fechaO)
    resultado7 = re.match(patronSiNo, electronico)
    resultado8 = re.match(patronNumReal, precioE)
    resultado9 = re.match(patronSiNo, fisico)
    resultado10 = re.match(patronNumReal, precioF)
    resultado11 = re.match(patronNumEntero, stockF)
    resultado12 = re.match(patron100, titulo)
    resultado13 = re.match(patron120, autor)
    resultado14 = re.match(patron100, procedencia)

    print('         [VerificadorS] Ejecutando verificaciones de los datos...')
    if resultado1 and resultado2 and resultado3 and resultado4 and resultado5 and resultado6 and resultado7 and resultado8 and resultado9 and resultado10 and resultado11 and resultado12 and resultado13 and resultado14:
        print('         [VerificadorS] Sintaxis validada...')
        return True
    else:
        print('         [VerificadorS] Error: sintaxis de datos errónea...')
        return False











