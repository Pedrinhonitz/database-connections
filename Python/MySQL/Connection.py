import MySQLdb


def conectar():
    try:
        conn = MySQLdb.connect(
            db='SEU DATABASE',
            host='SEU HOST',
            user='SEU USER',
            passwd='SEU PASSWORD',
            port='PORTA'
        )
        
        return conn
    except MySQLdb.Error as e:
        print(f"ERROR: {e}")


def desconectar(conn):
    if conn:
        conn.close()