import streamdb


def conectar():
    conn = streamdb.Client("streamdb://[SEU USER]:[SEU PASSWORD]@[SEU HOST]:[SUA PORTA]/[SEU DATABASE]")

    return conn


def desconectar(conn):
    if conn:
        conn.close()