require "snowflake"


def conectar()
    conn = Snowflake::Connection.new(
        account: "SEU ACCOUNT",
        warehouse: "SEU WAREHOUSE",
        db: "SEU DATABASE",
        user: "SEU USER",
        password: "SEU PASSWORD",
    )

    conn.open

    return conn
end


def execute_query(conn, query)
    result = conn.execute(query)

    return result
end


def desconectar(conn)
    conn.close
end