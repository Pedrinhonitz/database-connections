import ibm_db


def conectar():
    conn = ibm_db.connect(
        "DRIVER={IBM DB2 ODBC Driver};"
        "HOSTNAME={SEU HOST};"
        "PORT={SUA PORTA};"
        "DATABASE={SEU DATABASE};"
        "UID={SEU USERNAME};"
        "PWD={SEU PASSWORD};"
    )

    return conn


def desconectar(conn):
    if conn:
        conn.close()