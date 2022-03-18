import sqlite3, os
from risoles import Risoles


class BancoDao:

    def __init__(self):
        self.con = None

    def conectar(self):
        if self.con is None:
            self.con = sqlite3.connect('risoles.db')
            self.cur = self.con.cursor()

    def desconectar(self):
        if self.con is not None:
            self.con.close()
            self.con = None

    def criar_tabela(self):
        self.conectar()
        self.cur.execute("""
                            CREATE TABLE IF NOT EXISTS risoles(
                                idCliente integer PRIMARY KEY AUTOINCREMENT,
                                cliente text NOT NULL,
                                qtde integer,
                                refri integer,
                                money real,
                                total real,
                                troco real,
                                status text NOT NULL
                            );
        """)
        self.desconectar()

    def inserir_dados(self, risoles:Risoles):
        self.conectar()
        risoles = (risoles.cliente, risoles.qtde, risoles.refri, risoles.money, risoles.total, risoles.troco, risoles.status)
        self.cur.execute("""
                            INSERT INTO risoles(cliente, qtde, refri, money, total, troco, status)
                            VALUES(?, ?, ?, ?, ?, ?, ?)""", risoles)
        self.con.commit()
        print('Venda inserida com sucesso!')
        self.desconectar()

    def deletar_dados(self, cliente:str):
        self.conectar()
        self.cur.execute('DELETE FROM risoles WHERE cliente = ?', (cliente,))
        self.con.commit()
        print('Venda deletada com sucesso!')
        self.desconectar()

    def listar(self):
        self.conectar()
        if self.verificar_quantidade() == False:
            print('A lista está vazia!')
        else:
            lista = self.con.execute('SELECT * FROM risoles').fetchall()
            print('Lista de vendas:')
            for i in lista:
                print('--------------------------------------------------------------------------------------------------------------------')
                print(f'ID: {i[0]} | Cliente: {i[1]} | Quantidade: {i[2]} | Refri: {i[3]} | Recebido: {i[4]} | Total: {i[5]} | Troco: {i[6]} | Status: {i[7]}')
                print('--------------------------------------------------------------------------------------------------------------------')
        self.desconectar()

    def atualizar_dados(self, risoles:Risoles, cliente:str):
        self.conectar()
        risoles = (risoles.cliente, risoles.qtde, risoles.refri, risoles.money, risoles.total, risoles.troco, risoles.status, cliente)
        self.con.execute('UPDATE risoles SET cliente = ?, qtde = ?, refri = ?, money = ?, total = ?, troco = ?, status = ? \
                        WHERE cliente = ?', risoles)
        self.con.commit()
        print('Venda atualizada com sucesso!')
        self.desconectar()

    def buscar_dados(self, risoles:str):
        self.conectar()
        if self.verificar_cliente(risoles) == False:
            print('Cliente não encontrado!')
        else:
            buscar = self.con.execute('SELECT * FROM risoles WHERE cliente LIKE ?', ('%'+risoles+'%',)).fetchall()
            for i in buscar:
                print('--------------------------------------------------------------------------------------------------------------------')
                print(f'Venda: {i[0]} | Cliente: {i[1]} | Quantidade: {i[2]} | Refri: {i[3]} | Recebido: {i[4]} | Total: {i[5]} | Troco: {i[6]} | Status: {i[7]}')
                print('--------------------------------------------------------------------------------------------------------------------')

    def verificar_quantidade(self):
        self.conectar()
        lista = self.con.execute('SELECT * FROM risoles').fetchall()
        if len(lista) == 0:
            return False
        else:
            return True

    def verificar_cliente(self, risoles:str):
        self.conectar()
        lista = self.con.execute('SELECT * FROM risoles WHERE cliente = ?', (risoles,)).fetchall()
        if len(lista) == 0:
            return False

if __name__ == '__main__':
    app = BancoDao()
    app.listar()