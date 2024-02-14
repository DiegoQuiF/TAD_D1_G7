from flask_sqlalchemy import SQLAlchemy
from .config import *
import psycopg2

class DatabaseManager:
    _instancia = None

    def __new__(self):
        if self._instancia is None:
            print(" [Backend] Creando instancia DatabaseManager".ljust(120, "."))
            self._instancia = super(DatabaseManager, self).__new__(self)
            self._instancia.db = SQLAlchemy()
        print(" Obteniendo instancia de DatabaseManager ".center(120, "."))
        return self._instancia
    
    def getInstancia(self):
        return self._instancia

    def connection(self):
        db_config = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }

        try:
            conn = psycopg2.connect(**db_config)
            return conn
        except Exception as e:
            print(f" [Backend] Error de conexión con la base de datos: {e}".ljust(120, "."))
            return None