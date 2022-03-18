class Risoles(object):

    def __init__(self, cliente:str, qtde:int, refri:int, money:float, total:float, troco:float, status:str) -> None:
        self.cliente = cliente
        self.qtde = qtde
        self.refri = refri
        self.money = money
        self.total = total
        self.troco = troco
        self.status = status