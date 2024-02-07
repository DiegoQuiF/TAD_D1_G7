from .iEncriptador import IEncriptador
from .encriptador import Encriptador
from cryptography.fernet import Fernet

class Proxy(IEncriptador):
    def encriptar(self, contra):
        try:
            # Previa encriptación
            clave = cargar_clave()
            cifrador = Fernet(clave)
            encriptador = Encriptador()
            contra = contra.encode()
            
            #Encriptación
            clave_encriptada = encriptador.encriptar(contra, cifrador)
        except Exception as error:
            print(error)
        
        # Post encriptación
        return clave_encriptada.decode()
    

    def desencriptar(self, contra):
        # Previa desencriptación
        clave = cargar_clave()
        cifrador = Fernet(clave)
        encriptador = Encriptador()

        # Desencriptación
        clave_desencriptada = encriptador.desencriptar(contra, cifrador)

        #Post desencriptación
        return clave_desencriptada.decode()


# Genera una nueva clave y se guarda para utilizarla posteriormente
def generar_y_guardar_clave():
    clave = Fernet.generate_key()
    with open("clave_secreta.key", "wb") as archivo_clave:
        archivo_clave.write(clave)


# Carga la clave desde el archivo
def cargar_clave():
    return open("src/auxiliar/clave_secreta.key", "rb").read()
    