using Mongo


function conectar()
    conn = Mongo.connect("SEU HOST", 27017)

    return conn
end


function get_collection(conn)
    collection = conn |> Mongo.get_collection("SUA COLEÇÃO")
    
    return collection
end


function desconectar(conn)
    conn |> Mongo.close()
end