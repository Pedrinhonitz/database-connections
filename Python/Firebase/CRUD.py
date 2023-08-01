import pyrebase
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

SUA_TABELA = f""


#---Conexão-com-o-Bando-de-Dados----
def conectar():
    config = {
        "apiKey" : "SUA APIKEY",
        "authDomain" : "SEU DOMINIO",
        "databaseURL" : "SUA URL",
        "storageBucket" : "SEU BUCKET"
    }

    conn = pyrebase.initialize_app(config)

    db = conn.database()

    return db


#---Desconectando-do-Banco-de-Dados----
def desconectar():
    pass


#---Listando-Tabela-do-Banco-de-Dados----
def listar(type_return=0):
    db = conectar()

    resultados = db.child(SUA_TABELA).get()

    if resultados.val():
        if type_return == 0:
            for resultado in resultados.each():
                df = pd.DataFrame(resultado)
                print(df)
                divideLine()
        elif type_return ==1:
            print(f"{PURPLE} {' → LISTANDO ':^40} {RESET}")
            divideLine()

            for resultado in resultados.each():
                id = f"{resultado.key()}"
                nome = f"{resultado.val()['nome']}"
                email = f"{resultado.val()['email']}"
                senha = f"{resultado.val()['senha']}"

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
        print(f"{RED} {' → NÃO FOI ENCONTRADO NENHUM RESULTADO! ':^40} {RESET}")
        divideLine()


#---Inserindo-Dados-no-Banco
def inserir(seu_json):
    db = conectar()

    res = db.child(SUA_TABELA).push(seu_json)

    if 'name' in res:
        print(f"{GREEN} {' → INSERIDO COM SUCESSO!':^40} {RESET}")
        divideLine()
    else:
        print(f"{RED} {' → FALHA AO INSERIR! ':^40} {RESET}")
        divideLine()


#---Atualizando-Dados-no-Banco
def atualizar(chave, seu_json):
    db = conectar()

    res = db.child(SUA_TABELA).child(chave).get()

    if res.val():
        db.child(SUA_TABELA).child(chave).update(seu_json)
        print(f"{GREEN} {' → ATUALIZADO COM SUCESSO!':^40} {RESET}")
        divideLine()
    else:
        print(f"{RED} {' → FALHA AO ATUALIZAR! ':^40} {RESET}")
        divideLine()


#---Deltando-Dados-no-Banco
def deletar(chave):
    db = conectar()

    res = db.child(SUA_TABELA).child(chave).get()

    if res.val():
        db.child(SUA_TABELA).child(chave).remove()
        print(f"{GREEN} {' → DELETADO COM SUCESSO!':^40} {RESET}")
        divideLine()
    else:
        print(f"{RED} {' → FALHA AO DELETAR! ':^40} {RESET}")
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