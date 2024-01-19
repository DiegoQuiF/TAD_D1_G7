from flask_sqlalchemy import SQLAlchemy
from config import dbname, host, password, port, user
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
        return conn
    
    except Exception as e:
        print('          -> Error:', e)
        return None