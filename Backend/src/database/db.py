from flask_sqlalchemy import SQLAlchemy
from .config import *
import psycopg2


db = SQLAlchemy()

def connection():
    
    db_config = {
        'dbname': dbname,
        'user': user,
        'password': password,
        'host': host,
        'port': port
    }

    try:
        conn = psycopg2.connect(**db_config)
        print('[Backend] Conexión con la base de datos exitosa'.ljust(120, '.'))
        return conn
    
    except Exception as e:
        print('[Backend] No se pudo establecer conexión con la base de datos'.ljust(120, '.'))
        return None