using BigQuery


function conectar()
    conn = BigQuery.connect("SEU PROJECT ID", "SEU DATASET ID", "SEU TABLE ID")

    return conn
end


function get_table(conn)
    table = conn |> BigQuery.get_table("SEU PROJECT ID", "SEU DATASET ID", "SEU TABLE ID")

    return table
end


function execute_query(conn, query)
    result = conn |> BigQuery.query(query)

    return result
end


function desconectar(conn)
    conn |> BigQuery.close()
end