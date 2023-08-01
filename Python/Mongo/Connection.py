from pymongo import MongoClient


def conectar():
    conn = MongoClient('SEU HOST', 27017)
    
    return conn
    

def desconectar(conn):
    if conn:
        conn.close()