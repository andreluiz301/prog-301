import sqlite3


class Pessoa(object):

    def __init__(self, nome:str, idade:int, email:str) -> None:

        self.nome = nome
        self.idade = idade
        self.email = email


class BancoDao(object):

    def __init__(self) -> None:
        self.con = None

    def conectar(self):
        if self.con is None:
            self.con = sqlite3.connect('teste.db')
            self.cur = self.con.cursor()

    def desconectar(self):
        if self.con is not None:
            self.con.close()
            self.con = None

    def criar_tabela(self):
        self.conectar()
        self.cur.execute("""
                        CREATE TABLE IF NOT EXISTS cliente(
                            idCliente integer PRIMARY KEY AUTOINCREMENT,
                            nome text,
                            idade integer,
                            email text UNIQUE NOT NULL
                        );
        """)
        self.con.commit()
        self.con.close()