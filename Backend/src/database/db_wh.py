from flask_sqlalchemy import SQLAlchemy
from .config_wh import *
import psycopg2

class DatabaseManager_wh:
    _instancia = None

    def __new__(self):
        if self._instancia is None:
            print(" [Backend] Creando instancia DatabaseManager".ljust(120, "."))
            self._instancia = super(DatabaseManager_wh, self).__new__(self)
            self._instancia.db = SQLAlchemy()
        print(" Obteniendo instancia de DatabaseManager ".center(120, "."))
        return self._instancia
    
    def getInstancia(self):
        return self._instancia

    def connection(self):
        db_config_wh = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }

        try:
            conn = psycopg2.connect(**db_config_wh)
            return conn
        except Exception as e:
            print(f" [Backend] Error de conexión con la base de datos: {e}".ljust(120, "."))
            return None