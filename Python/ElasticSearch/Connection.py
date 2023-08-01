import elasticsearch


def conectar():
    conn = elasticsearch.Elasticsearch([
        "SEU HOST:9200"
    ])

    return conn