import cx_Oracle


def conectar():
    conn = cx_Oracle.connect(
        user='SEU USERNAME',
        password='SEU PASSWORD',
        dsn='//host:port/service',
    )

    return conn


def desconectar(conn):
    if conn:
        conn.close()