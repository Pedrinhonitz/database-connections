import socket
import couchdb


def conectar():
    user = f'SEU USER'
    password = f'SEU PASSWORD'
    host = f'SEU HOST'
    database = f"SEU DATABASE"
    port = f"PORTA"
    conn = couchdb.Server(f"http://{user}:{password}@{host}:{port}")

    if database in conn:
        db = conn[database]

        return db
    else:
        try:
            db = conn.create(database)
            return db
        except socket.gaierror as e:
            print(f"ERROR: {e}")
        except couchdb.http.Unauthorized as er:
            print(f"ERROR: {er}")
        except ConnectionRefusedError as err:
            print(f"ERROR: {err}")