using MySQL


function conectar()
    conn = MySQL.connect("SEU HOST", "SEU USERNAME", "SEU PASSWORD", "SEU DATABASE")

    return conn
end


function desconectar(conn)
    conn |> MySQL.close()
end