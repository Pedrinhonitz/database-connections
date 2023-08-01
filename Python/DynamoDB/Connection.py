import boto3

def conectar():
    client = boto3.client('dynamodb', region_name='SEU REGIAO')

    return client