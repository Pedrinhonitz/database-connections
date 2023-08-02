using Athena


function conectar()
    conn = Athena.connect("SEU ACESS KEY", "SEU SECRET ACESSO KEY", "SUA REGIÃO")

    return conn
end


function get_table(conn)
    table = conn |> Athena.get_table("SEU DATABASE", "SUA TABELA")

    return table
end



function desconectar(conn)
    conn |> Athena.close()
end