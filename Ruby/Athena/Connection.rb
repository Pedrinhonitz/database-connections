require "aws-sdk-athena"


def conectar()
    client = Aws::Athena::Client.new

    # Configure as credenciais
    client.configure do |config|
    config.access_key_id = "SEU ACCESS KEY ID"
    config.secret_access_key = "SEU SECRET ACCESS KEY"
    config.region = "SUA REGIÃO"
    end

    return client
end


def execute_query(client, query)
    result = client.query(query_string: query)

    return result
end