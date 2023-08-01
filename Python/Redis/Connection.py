import redis


def conectar():
    conn = redis.Redis(host='SEU HOST', port=6379)
    
    return conn
    

def desconectar(conn):
    conn.connection_pool.disconnect()