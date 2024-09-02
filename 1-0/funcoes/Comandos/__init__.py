from funcoes.Database import Database
from funcoes.Modulo import limpar_terminal, pausar_terminal
from funcoes.Linguagens import *

db = Database()
conexoes = []
for linguagem in linguagens:
    conexoes.append(db.criar_conexao(f"{linguagem.lower()}.db"))

con = None
sair = False


def procurarPorComando():
    limpar_terminal()
    comando = input("Digite o comando: ")
    comandos = db.comandos(con)
    for cmd in comandos:
        if cmd[0].lower() == comando.lower():
            limpar_terminal()
            print(f"\nA Descricao do Comando {comando.lower()}:\n")
            print(cmd[1], "\n")
            pausar_terminal()
            return
    limpar_terminal()
    print(f"\nComando {comando.lower()} nao encontrado\n")
    pausar_terminal()
    return

def procurar_comando() -> None:
    procurarPorComando()

def adicionar_comando() -> None:
    limpar_terminal()
    comando = input("Digite o comando: ")
    descricao = input("Digite a descricao do comando: ")
    db.executar(con, "INSERT INTO comandos (T_COMANDO, T_DESCRICAO) VALUES (?,?)", (comando, descricao))
    print("\nComando Adicionado\n")
    pausar_terminal()

def listar_comandos() -> None:
    limpar_terminal()
    comandos = db.comandos(con)
    lim = 5
    cont = 0
    for cmd in comandos:
        print(f"\nComando: {cmd[0].lower()}")
        print(f"Descricao: {cmd[1]}\n")
        cont += 1
        if cont == lim:
            cont = 0
            pausar_terminal()
            limpar_terminal()
    pausar_terminal()

def alterarADescricaoDoComando() -> None:
    limpar_terminal()
    comando = input("Digite o comando: ")
    comandos = db.comandos(con)
    for cmd in comandos:
        if cmd[0].lower() == comando.lower():
            novo_descricao = input("Digite a nova descricao do comando: ")
            db.executar(con, "UPDATE comandos SET T_DESCRICAO =? WHERE T_COMANDO =?", (novo_descricao, comando))
            print("\nDescricao do Comando Alterada\n")
            pausar_terminal()
        else:
            limpar_terminal()
            print(f"\nComando {comando.lower()} nao encontrado\n")
            pausar_terminal()

def traduzir_comando(comando: int) -> None:
    global sair
    match comando:
        case 1:
            procurar_comando()
        case 2:
            adicionar_comando()
        case 3:
            alterarADescricaoDoComando()
        case 4:
            listar_comandos()

def perguntarDescisaoComando() -> None:
    try:
        opcao = int(input("Digite a opcao: "))
        if opcao < 0 or opcao > 4:
            raise ValueError
        traduzir_comando(opcao)
    except:
        print("Digite um número")
        return perguntarDescisaoComando()

def menu_linguagens():
    global con, sair
    limpar_terminal()
    print("Bem vindo ao Dicionario de Comandos\n")
    print("Linguagens Disponíveis: ")
    for i, linguagem in enumerate(linguagens):
        print(f"{i+1} - {linguagem}")
        
    descisao = perguntarDescisaoLinguagem()

    con = conexoes[traduzir_linguagem(descisao)]

def menu_comandos():
    limpar_terminal()
    print("Bem vindo ao Dicionario de Comandos\n")
    print("1 - Procurar Comando")
    print("2 - Adicionar Comando")
    print("3 - Mudar Descricao de um Comando")
    print("4 - Listar os comandos")
    perguntarDescisaoComando()
