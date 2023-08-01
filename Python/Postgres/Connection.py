import psycopg2


def conectar():
    try:
        conn = psycopg2.connect(
            db='SEU DATABASE',
            host='SEU HOST',
            user='SEU USER',
            passwd='SEU PASSWORD',
            port='PORTA'
        )
        
        return conn
    except psycopg2.Error as e:
        print(f"ERROR: {e}")


def desconectar(conn):
    if conn:
        conn.close()