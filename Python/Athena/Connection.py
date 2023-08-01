import boto3

def conectar():
    client = boto3.client('athena', region_name='SEU REGIAO')

    return client