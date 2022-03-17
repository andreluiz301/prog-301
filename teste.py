class Pessoa(object):

    def __init__(self, nome='', email='', telefone='', celular=None):

        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.celular = celular

    def __str__(self) -> str:
        return f'NOME: {self.nome} | EMAIL: {self.email} | FONE: {self.telefone} | {self.celular}'

    
class Celular(object):

    def __init__(self, numero, marca, modelo):

        self.numero = numero
        self.marca = marca
        self.modelo = modelo

    def __str__(self) -> str:
        return f'CELULAR: {self.numero} | MARCA: {self.marca} | MODELO: {self.modelo}'

    
if __name__ == "__main__":

    c1 = Celular('47992591759', 'Motorola', 'G6+')
    p1 = Pessoa('André', 'andrelbarcelo@gmail.com', '473394-4176', c1)
    
    print(p1)