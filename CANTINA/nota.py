from banco import BancoDao
import os, time, sqlite3


class NotaFiscal:

    def __init__(self):
        self.dao = BancoDao()
        self.con = sqlite3.connect('risoles.db')
        self.cur = self.con.cursor()

    def imprimir_nota(self):
        self.dao.conectar()
        if self.dao.verificar_quantidade() == False:
            print('A lista está vazia!')
        else:
            lista = self.cur.execute('SELECT * FROM risoles').fetchall()
            print('Gerando arquivo...\n')
            arq = open('nota_risoles.txt', 'a')
            arq.write(f'VENDAS DA CANTINA DO DIA 19/02/2022\n\n')
            for i in lista:
                arq.write(f'---------------------------------------------------------------------------------------------------------------------------\n')
                arq.write(f'ID: {i[0]} | Cliente: {i[1]} | Quantidade: {i[2]} | Refri: {i[3]} | Recebido: {i[4]} | Total: {i[5]} | Troco: {i[6]} | Status: {i[7]}\n')
            arq.write(f'===========================================================================================================================\n')
            arq.write(f'\nGerado em {time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())}\n\n')
        self.dao.desconectar()

    def deletar_nota(self):
        self.dao.conectar()
        if self.dao.verificar_quantidade() == False:
            print('A lista está vazia! Arquivo inexistente.')
        else:
            try:
                a = input('Deletar nota? (Digite "s" para "Sim" ou "n" para "Não") -> ')
                if a == 's':
                    os.remove('nota_risoles.txt')
                    print('Deletando nota...\n')
                elif a == 'n':
                    print('Você optou por não deletar a nota.')
                    pass
                else:
                    print('Opção inválida!')
            except(FileNotFoundError):
                print('Arquivo inexistente!\n')
                return
            except(TypeError, NameError):
                print('Opção inválida!')
        self.dao.desconectar()
