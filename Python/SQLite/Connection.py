import sqlite3


def conectar():
    try:
        conn = sqlite3.connect('SEU ARQUIVO .DB')
        
        return conn
    except sqlite3.Error as e:
        print(f"ERROR: {e}")



def desconectar(conn):
    if conn:
        conn.close()