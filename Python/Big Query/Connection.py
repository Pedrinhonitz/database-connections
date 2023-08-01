from google.cloud import bigquery


def conectar():
    client = bigquery.Client()

    return client