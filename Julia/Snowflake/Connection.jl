using Snowflake


function conectar()
    conn = SnowflakeConnection(
        account = "SEU ACCOUNT",
        warehouse = "SEU WAREHOUSE",
        db = "SEU DATABASE",
        user = "SEU USER",
        password = "SEU PASSWORD",
    )

    conn.open()

    return conn
end


function execute_query(conn, query)
    result = conn.execute(query)

    return result
end


function desconectar(conn)
    conn.close()
end