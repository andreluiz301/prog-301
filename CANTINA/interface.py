from banco import BancoDao
from risoles import Risoles
from nota import NotaFiscal


class Interface:

    def __init__(self):
        self.dao = BancoDao()
        self.nota = NotaFiscal()

    def inserir(self):
        try:
            cliente = input('Digite o nome do cliente que deseja inserir: ')
            qtde = int(input('Digite a quantidade de risoles desejada: '))
            refri = int(input('Digite a quantidade de refri desejada: '))
            money = float(input('Digite o valor recebido pelo cliente: '))
            if refri >= 0:
                total = (qtde * 2.5) + refri * 0.5
                troco = money - total
                if troco < 0:
                    status = 'Pendente'
                else:
                    status = 'Pago'
        except(ValueError, TypeError):
            print('Informação inválida!')
            return

        print('--------------------------------')
        print(f'TOTAL: {total} | TROCO: {troco}')
        print('--------------------------------')

        risoles = Risoles(cliente, qtde, refri, money, total, troco, status)
        self.dao.inserir_dados(risoles)

    def remover(self):
        cliente = input('Digite o nome do cliente que deseja remover: ')
        if self.dao.verificar_cliente(cliente) == False:
            print('Cliente não encontrado no banco de dados!')
            return
        
        self.dao.deletar_dados(cliente)

    def atualizar(self):
        cliente = input('Digite o nome do cliente que deseja atualizar: ')
        if self.dao.verificar_cliente(cliente) == False:
            print('Cliente não encontrado no banco de dados!')
            return
        try:
            novo_cliente = input('Novo nome do cliente: ')
            nova_qtde = int(input('Nova quantidade de risoles: '))
            novo_refri = int(input('Nova quantidade de refri: '))
            novo_money = float(input('Novo valor recebido: '))
            if novo_refri >= 0:
                novo_total = (nova_qtde * 2.5) + novo_refri * 0.5
                novo_troco = novo_money - novo_total
                if novo_troco < 0:
                    novo_status = 'Pendente'
                else:
                    novo_status = 'Pago'
        except(ValueError, TypeError):
            print('Informação inválida!')
            return

        print('--------------------------------')
        print(f'TOTAL: {novo_total} | TROCO: {novo_troco}')
        print('--------------------------------')

        risoles = Risoles(novo_cliente, nova_qtde, novo_refri, novo_money, novo_total, novo_troco, novo_status)
        self.dao.atualizar_dados(risoles, cliente)

    def buscar(self):
        cliente = input('Digite o nome do cliente que deseja buscar: ')
        if not cliente:
            print('Informe um cliente válido!')
        else:
            self.dao.buscar_dados(cliente)

    def exibir_menu(self):
        print('------------- MENU -------------')
        print('|                              |')
        print('|      1  -  Inserir           |')
        print('|      2  -  Remover           |')
        print('|      3  -  Atualizar         |')
        print('|      4  -  Listar            |')
        print('|      5  -  Buscar            |')
        print('|      6  -  Gerar Nota        |')
        print('|      7  -  Excluir Nota      |')
        print('|      0  -  Sair              |')
        print('|                              |')
        print('-------------RISOLES------------')

    def menu(self):
        #Este método serve para o usuário escolher o que quer fazer.
        sair = False
        while True:
            self.exibir_menu()
            try:
                n = int(input('\nO que deseja fazer: '))
                if n == 1:
                    self.inserir()
                elif n == 2:
                    self.remover()
                elif n == 3:
                    self.atualizar()
                elif n == 4:
                    self.dao.listar()
                elif n == 5:
                    self.buscar()
                elif n == 6:
                    self.nota.imprimir_nota()
                elif n == 7:
                    self.nota.deletar_nota()
                elif n == 0:
                    print('Saindo...')
                    sair = True
                    break
                else:
                    print('Insira uma opção válida')
            except(ValueError):
                print("Insira uma opção válida!")

if __name__ == '__main__':
    app = BancoDao()
    app.criar_tabela()
    inter = Interface()
    inter.menu()