import snowflake.connector


def conectar():
    conn = snowflake.connector.connect(
        user='SEU USER',
        password='SEU PASSWORD',
        account='SUA ACCOUNT',
        warehouse='SEU WAREHOUSE',
        schema='SEU SCHEMA',
    )

    return conn


def desconectar(conn):
    if conn:
        conn.close()