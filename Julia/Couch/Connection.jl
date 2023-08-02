using CouchDB


function conectar()
    conn = CouchDB.connect("SEU HOST", 5984)

    return conn
end


function get_database(conn)
    db = conn |> CouchDB.get_database("SEU DATABASE")

    return db
end


function desconectar(conn)
    conn |> CouchDB.close()
end