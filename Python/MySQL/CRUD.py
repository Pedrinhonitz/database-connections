import MySQLdb
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
    try:
        conn = MySQLdb.connect(
            db='SEU DATABASE',
            host='SEU HOST',
            user='SEU USER',
            passwd='SEU PASSWORD'
        )
        
        return conn
    except MySQLdb.Error as e:
        print(f"{RED} {' → ERRO: {e} ':^40} {RESET}")
        divideLine()


#---Desconectando-do-Banco-de-Dados----
def desconectar(conn):
    if conn:
        conn.close()


#---Listando-Tabela-do-Banco-de-Dados
def listar(query, type_return=0):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(query)
    resultados = cursor.fetchall()

    if len(resultados) > 0:
        if type_return == 0:
            df = pd.DataFrame(resultados)
            print(df)
            divideLine()
        elif type_return ==1:
            print(f"{PURPLE} {' → LISTANDO PRODUTOS ':^40} {RESET}")
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

    desconectar(conn)

#---Inserindo-Dados-no-Banco
def inserir(query):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    if cursor.rowcount >= 1:
        print(f"{GREEN} {' → INSERIDO COM SUCESSO!':^40} {RESET}")
        divideLine()
    else:
        print(f"{RED} {' → FALHA AO INSERIR! ':^40} {RESET}")
        divideLine()

    desconectar(conn)
    

#---Atualizando-Dados-no-Banco
def atualizar(query):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    if cursor.rowcount >= 1:
        print(f"{GREEN} {' → ATUALIZADO COM SUCESSO!':^40} {RESET}")
        divideLine()
    else:
        print(f"{RED} {' → FALHA AO ATUALIZAR! ':^40} {RESET}")
        divideLine()

    desconectar(conn)


#---Deltando-Dados-no-Banco
def deletar(query):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    if cursor.rowcount >= 1:
        print(f"{GREEN} {' → DELETADO COM SUCESSO!':^40} {RESET}")
        divideLine()
    else:
        print(f"{RED} {' → FALHA AO DELETAR! ':^40} {RESET}")
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
        print(f"{PURPLE} {' → DIGITE SUA CONSULTA SQL ':^40} {RESET}")
        query = str(input(f"{GREEN}→ {RESET}"))
        divideLine()

        listar(query)
    elif menu_choice == '1':
        print(f"{PURPLE} {' → DIGITE SUA CONSULTA SQL ':^40} {RESET}")
        query = str(input(f"{GREEN}→ {RESET}"))
        divideLine()

        inserir(query)
    elif menu_choice == '2':
        print(f"{PURPLE} {' → DIGITE SUA CONSULTA SQL ':^40} {RESET}")
        query = str(input(f"{GREEN}→ {RESET}"))
        divideLine()

        atualizar(query)
    elif menu_choice == '3':
        print(f"{PURPLE} {' → DIGITE SUA CONSULTA SQL ':^40} {RESET}")
        query = str(input(f"{GREEN}→ {RESET}"))
        divideLine()

        deletar(query)
    else:
        print(f"{RED} {' → OPÇÃO INVALIDA! ':^40} {RESET}")
        divideLine()


#---Main-do-Sistema----
while True:
    menu()