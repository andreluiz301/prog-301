import sqlite3


class BancoDao(object):

    def __init__(self) -> None:
        self.con = None

    def conectar(self):
        if self.con is None:
            self.con = sqlite3.connect('pessoa.db')
            self.cur = self.con.cursor()

    def desconectar(self):
        if self.con is not None:
            self.con.close()
            self.con = None

    def criar_tabela(self):
        self.conectar()
        self.cur.execute("""
                            CREATE TABLE IF NOT EXISTS pessoa(
                                idPessoa integer PRIMARY KEY AUTOINCREMENT,
                                nome text NOT NULL,
                                idade integer NOT NULL
                            );
        """)
        self.con.commit()
        self.desconectar()