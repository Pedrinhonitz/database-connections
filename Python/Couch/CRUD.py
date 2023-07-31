import socket
import couchdb
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


#---Conexão-com-o-Bando-de-Dados----
def conectar():
    user = f'SEU USER'
    password = f'SEU PASSWORD'
    host = f'SEU HOST'
    database = f"SEU DATABASE"
    conn = couchdb.Server(f"http://{user}:{password}@{host}:5984")

    if database in conn:
        db = conn[database]

        return db
    else:
        try:
            db = conn.create(database)
            return db
        except socket.gaierror as e:
            print(f"{RED} {' → ERRO: {e} ':^40} {RESET}")
            divideLine()
        except couchdb.http.Unauthorized as er:
            print(f"{RED} {' → ERRO: {er} ':^40} {RESET}")
            divideLine()
        except ConnectionRefusedError as err:
            print(f"{RED} {' → ERRO: {err} ':^40} {RESET}")
            divideLine()


#---Desconectando-do-Banco-de-Dados----
def desconectar(db):
    pass


#---Listando-Tabela-do-Banco-de-Dados----
def listar(type_return=0):
    db = conectar()

    if db:
        if db.info()['doc_count'] > 0:
            if type_return == 0:
                for doc in db:
                    df = pd.DataFrame(db[doc])
                    print(df)
                    divideLine()
            elif type_return ==1:
                print(f"{PURPLE} {' → LISTANDO ':^40} {RESET}")
                divideLine()

                for doc in db:

                    id = f"{db[doc][id]}"
                    nome = f"{db[doc][nome]}"
                    email = f"{db[doc][email]}"
                    senha = f"{db[doc][senha]}"

                    print(f"{GREEN} {' → ID: {id}':^40} {RESET}")
                    divideLine()

                    print(f"{GREEN} {' → NOME: {nome}':^40} {RESET}")
                    divideLine()

                    print(f"{GREEN} {' → EMAIL: {email}':^40} {RESET}")
                    divideLine()

                    print(f"{GREEN} {' → SENHA: {senha}':^40} {RESET}")
                    divideLine()
            else:
                print(f"{RED} {' → TIPO DE RETORNO NÃO ENCONTRADO! ':^40} {RESET}")
                divideLine()
        else:
            print(f"{RED} {' → ERRO AO CONECTAR COM O SERVIDOR! ':^40} {RESET}")
            divideLine()


#---Inserindo-Dados-no-Banco
def inserir(seu_json):
    db = conectar()

    if db:
        res = db.save(seu_json)

        if res:
            print(f"{GREEN} {' → INSERIDO COM SUCESSO!':^40} {RESET}")
            divideLine()
        else:
            print(f"{RED} {' → FALHA AO INSERIR! ':^40} {RESET}")
            divideLine()
    else:
        print(f"{RED} {' → ERRO AO CONECTAR COM O SERVIDOR! ':^40} {RESET}")
        divideLine()

    
#---Atualizando-Dados-no-Banco
def atualizar(chave, seu_json):
    db = conectar()
    
    if db:
        try:
            doc = db[chave]

            db[doc.id] = doc
            print(f"{GREEN} {' → ATUALIZADO COM SUCESSO!':^40} {RESET}")
            divideLine()
        except couchdb.http.ResourceNotFound as e
            print(f"{RED} {' → FALHA AO ATUALIZAR! ':^40} {RESET}")
            divideLine()
    else:
        print(f"{RED} {' → ERRO AO CONECTAR COM O SERVIDOR! ':^40} {RESET}")
        divideLine()


#---Deltando-Dados-no-Banco
def deletar(chave):
    db = conectar()
   
    if db:
        try:
            db.delete(db[chave])
        except couchdb.http.ResourceNotFound as e
            print(f"{RED} {' → FALHA AO ATUALIZAR! ':^40} {RESET}")
            divideLine()
    else:
        print(f"{RED} {' → ERRO AO CONECTAR COM O SERVIDOR! ':^40} {RESET}")
        divideLine()


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
        print(f"{PURPLE} {' → DIGITE A CHAVE ':^40} {RESET}")
        chave = str(input(f"{GREEN}→ {RESET}"))
        divideLine()    

        print(f"{PURPLE} {' → DIGITE SEU JSON ':^40} {RESET}")
        seu_json = str(input(f"{GREEN}→ {RESET}"))
        divideLine()

        atualizar(chave, seu_json)
    elif menu_choice == '3':
        print(f"{PURPLE} {' → DIGITE A CHAVE ':^40} {RESET}")
        chave = str(input(f"{GREEN}→ {RESET}"))
        divideLine()

        deletar(chave)
    else:
        print(f"{RED} {' → OPÇÃO INVALIDA! ':^40} {RESET}")
        divideLine()


#---Main-do-Sistema----
while True:
    menu()