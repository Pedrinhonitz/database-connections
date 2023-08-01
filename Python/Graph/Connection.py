import graphdb


def conectar():
    conn = graphdb.Client("graphdb://[SEU USERNAME]:[SEU PASSWORD]@[SEU HOST]:[SUA PORTA]/[SEU DATABASE]")

    return conn


def desconectar(conn):
    if conn:
        conn.close()
