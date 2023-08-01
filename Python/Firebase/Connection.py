import pyrebase


def conectar():
    config = {
        "apiKey" : "SUA APIKEY",
        "authDomain" : "SEU DOMINIO",
        "databaseURL" : "SUA URL",
        "storageBucket" : "SEU BUCKET"
    }

    conn = pyrebase.initialize_app(config)

    db = conn.database()

    return db