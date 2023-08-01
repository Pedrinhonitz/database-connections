import pyodbc


def conectar():
    conn = pyodbc.connect(
        "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        "DBQ={SEU DATABASE PATH};"
        "UID={SEU USER};"
        "PWD={SEU PASSWORD};"
    )

    return conn


def desconectar(conn):
    if conn:
        conn.close()