import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        pass

    def criar_conexao(self, database) -> sqlite3.Connection | None:
        try:
            conn = sqlite3.connect(f'E:\\Programacao\\Projetos\\Dicionario_de_Comandos\\1-0\\Databases\\{database}')
            return conn
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def executar(self, conn: sqlite3.Connection, comando: str, dados: tuple | None=None) -> None:
        try:
            cursor = conn.cursor()
            if dados:
                cursor.execute(comando, dados)
            else:
                cursor.execute(comando)
            conn.commit()
        except Error as e:
            print(e)

    def comandos(self, conn: sqlite3.Connection):
        if conn is None:
            print("Erro: Conexão com o banco de dados não estabelecida.")
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comandos;")
            return cursor.fetchall()
        except Error as e:
            print(e)
            return []
