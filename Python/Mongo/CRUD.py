from pymongo import MongoClient, errors
from bson.objectid import ObjectId
import pandas as pd

#---Cores-do-Sistema----
RED   = "\033[1;31m"  
PURPLE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
GREY = "\033[1;90m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
YELLOW = "\033[1;33m"
REVERSE = "\033[;7m"

SEU_DATABASE = f""
SUA_TABELA = f""

#---Conexão-com-o-Bando-de-Dados----
def conectar():
    conn = MongoClient('SEU HOST', 27017)
    
    return conn
    

#---Desconectando-do-Banco-de-Dados----
def desconectar(conn):
    if conn:
        conn.close()


#---Listando-Tabela-do-Banco-de-Dados----
def listar(type_return=0):
    conn = conectar()
    db = conn.SEU_DATABASE

    try:
        if db.SUA_TABELA.count_documents({}) > 0:
            resultados = db.SUA_TABELA.find()
            if type_return == 0:
                df = pd.DataFrame(resultados)
                print(df)
                divideLine()
            elif type_return ==1:
                print(f"{PURPLE} {' → LISTANDO ':^40} {RESET}")
                divideLine()

                for resultado in resultados:
                    print(f"{GREEN} {' → ID: {resultado[0]}':^40} {RESET}")
                    divideLine()

                    print(f"{GREEN} {' → NOME: {resultado[1]}':^40} {RESET}")
                    divideLine()

                    print(f"{GREEN} {' → EMAIL: {resultado[2]}':^40} {RESET}")
                    divideLine()

                    print(f"{GREEN} {' → SENHA: {resultado[3]}':^40} {RESET}")
                    divideLine()
            else:
                print(f"{RED} {' → TIPO DE RETORNO NÃO ENCONTRADO! ':^40} {RESET}")
                divideLine()
        else:
            print(f"{RED} {' → NÃO FOI ENCONTRADO NENHUM RESULTADO! ':^40} {RESET}")
            divideLine()
    except errors.PyMongoError as e:
        print(f"{RED} {' → ERRO: {e} ':^40} {RESET}")
        divideLine()

    desconectar(conn)

#---Inserindo-Dados-no-Banco
def inserir(seu_json):
    conn = conectar()
    db = conn.SEU_DATABASE

    try:
        db.SUA_TABELA.insert_one(seu_json)
        print(f"{GREEN} {' → INSERIDO COM SUCESSO! ':^40} {RESET}")
        divideLine()
    except errors.PyMongoErros as e:
        print(f"{RED} {' → ERRO: {e} ':^40} {RESET}")
        divideLine()

    desconectar(conn)
    

#---Atualizando-Dados-no-Banco
def atualizar(seu_json):
    conn = conectar()
    db = conn.SEU_DATABASE

    try:
        if db.SUA_TABELA.count_documents({}) > 0:
            res = db.SUA_TABELA.update_one(seu_json)

            if res.modified_count == 1:
                print(f"{GREEN} {' → ATUALIZADO COM SUCESSO! ':^40} {RESET}")
                divideLine()
            else:
                print(f"{RED} {' → FALHA AO ATUALIZAR! ':^40} {RESET}")
                divideLine()
        else:
            print(f"{RED} {' → NENHUMA LINHA ENCONTRADA! ':^40} {RESET}")
            divideLine()
    except errors.PyMongoErros as e:
        print(f"{RED} {' → ERRO: {e} ':^40} {RESET}")
        divideLine()

    desconectar(conn)


#---Deltando-Dados-no-Banco
def deletar(seu_json):
    conn = conectar()
    db = conn.SEU_DATABASE

    try:
        if db.SUA_TABELA.count_documents({}) > 0:
            res = db.SUA_TABELA.delete_one(seu_json)

            if res.deleted_count == 1:
                print(f"{GREEN} {' → DELETADO COM SUCESSO! ':^40} {RESET}")
                divideLine()
            else:
                print(f"{RED} {' → FALHA AO DELETAR! ':^40} {RESET}")
                divideLine()
        else:
            print(f"{RED} {' → NENHUMA LINHA ENCONTRADA! ':^40} {RESET}")
            divideLine()
    except errors.PyMongoErros as e:
        print(f"{RED} {' → ERRO: {e} ':^40} {RESET}")
        divideLine()

    desconectar(conn)


#---Quebra-de-Linha----
def divideLine():
    print(f"{BOLD}-{RESET}" * 40)


#---Menu-do-Sistema----
def menu():
    divideLine()
    print(f"{PURPLE} {' → LISTAR (0)':^40} {RESET}")
    divideLine()

    print(f"{PURPLE} {' → INSERIR (1)':^40} {RESET}")
    divideLine()

    print(f"{PURPLE} {' → ATUALIZAR (2)':^40} {RESET}") 
    divideLine()

    print(f"{PURPLE} {' → DELETAR (3)':^40} {RESET}")
    divideLine()

    print(f"{PURPLE} {' → QUAL ABA DESEJA ACESSAR? ':^40} {RESET}")
    menu_choice = str(input(f"{GREEN}→ {RESET}"))
    divideLine()

    if menu_choice == '0':
        listar()
    elif menu_choice == '1':
        print(f"{PURPLE} {' → DIGITE SEU JSON ':^40} {RESET}")
        seu_json = str(input(f"{GREEN}→ {RESET}"))
        divideLine()

        inserir(seu_json)
    elif menu_choice == '2':
        print(f"{PURPLE} {' → DIGITE SEU JSON ':^40} {RESET}")
        seu_json = str(input(f"{GREEN}→ {RESET}"))
        divideLine()

        atualizar(seu_json)
    elif menu_choice == '3':
        print(f"{PURPLE} {' → DIGITE SEU JSON ':^40} {RESET}")
        seu_json = str(input(f"{GREEN}→ {RESET}"))
        divideLine()

        deletar(seu_json)
    else:
        print(f"{RED} {' → OPÇÃO INVALIDA! ':^40} {RESET}")
        divideLine()


#---Main-do-Sistema----
while True:
    menu()