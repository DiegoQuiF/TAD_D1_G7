from .iEncriptador import IEncriptador
from cryptography.fernet import Fernet

class Encriptador(IEncriptador):
    def encriptar(self, contra, cifrador):
        contra_encriptada = cifrador.encrypt(contra)
        return contra_encriptada

    def desencriptar(self, contra, cifrador):
        contrasena = cifrador.decrypt(contra)
        return contrasena