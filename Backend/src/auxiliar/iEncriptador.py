from abc import ABC, abstractmethod

class IEncriptador():
    @abstractmethod
    def encriptar(self, contra):
        pass

    @abstractmethod
    def desencriptar(self, contra):
        pass