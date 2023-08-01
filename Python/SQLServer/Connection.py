import pyodbc


def connectar():
    conn = pyodbc.connect(
        "DRIVER={SQL Server Native Client 11.0};"
        "SERVER={SEU SERVER NAME};"
        "DATABASE={SEU DATABASE};"
        "UID={SEU USERNAME};"
        "PWD={SEU PASSWORD};"
    )

    return conn


def desconectar(conn):
    if conn:
        conn.close()