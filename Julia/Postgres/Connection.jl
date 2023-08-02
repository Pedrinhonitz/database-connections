using JuliaDB


function conectar()
    conn = JuliaDB.connect("postgresql://SEU USERNAME:SEU PASSWORD@SEU HOST:5432/SEU DATABASE")

    return conn
end


function desconectar(conn)
    conn |> JuliaDB.close()
end