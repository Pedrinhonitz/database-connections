import mariadb


def conectar():
    conn = mariadb.connect(
        host='SEU HOST',
        port=3306,
        user='SEU USER',
        password='SEU PASSWORD',
        database='SEU DATABASE',
    )

    return conn


def desconectar(conn):
    if conn:
        conn.close()