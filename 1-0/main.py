from funcoes.Comandos import *
from funcoes.Modulo import limpar_terminal, pausar_terminal


def main():
    while not sair:
        menu_linguagens()
        menu_comandos()


if __name__ == "__main__":
    main()
