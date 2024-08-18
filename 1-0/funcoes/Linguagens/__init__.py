from funcoes.Modulo import limpar_terminal, pausar_terminal
from funcoes.Database import Database

linguagens = ["Javascript", "Python", "Linux", "C++", "SQL"]
db = Database()

def perguntarDescisaoLinguagem() -> int:
    while True:
        try:
            descisao = int(input("Digite a Linguagem escolhida: "))
            if 1 <= descisao <= len(linguagens):
                return descisao
            else:
                print("Escolha uma opcao válida entre 1 e", len(linguagens))
        except ValueError:
            print("Digite um número válido.")

def traduzir_linguagem(linguagem: int) -> int:
    return linguagem - 1
