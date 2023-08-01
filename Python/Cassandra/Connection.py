import cassandra


def conectar():
    conn = cassandra.Session(
        host='SEU HOST',
        port=9042,
        keyspace='SEU KEYSPACE',
        username='SEU USERNAME',
        password='SEU PASSWORD',
    )

    return conn


def desconectar(conn):
    if conn:
        conn.close()