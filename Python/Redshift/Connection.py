import pyodbc


def conectar():

    conn = pyodbc.connect(
        "DRIVER={Amazon Redshift ODBC Driver};"
        "HOSTNAME={redshift_endpoint};"
        "PORT={port};"
        "DATABASE={database};"
        "UID={username};"
        "PWD={password};"
    )
    
    return conn


def desconectar(conn):
    if conn:
        conn.close()