from config import *

class Pessoa(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    tipo = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity':'pessoa',
        'polymorphic_on':tipo
    }

    def __str__(self):
        return f'ID: {self.id} | Nome: {self.nome} | Tipo: {self.tipo} | Email: {self.email} | Fone: {self.telefone}'

class Vendedor(Pessoa):

    id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), primary_key=True)
    comissao = db.Column(db.Float)

    __mapper_args__ = {
        'polymorphic_identity':'Vendedor'
    }

    def __str__(self):
        return f'{super().__str__()} | Comissão: {str(self.comissao)}'

class Motorista(Pessoa):

    id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), primary_key=True)
    cnh = db.Column(db.String(254))

    __mapper_args__ = {
        'polymorphic_identity':'Motorista'
    }

    def __str__(self):
        return f'{super().__str__()} | CNH: {self.cnh}'


if os.path.exists(arquivobd): # se houver o arquivo...
        os.remove(arquivobd) # ...apagar!

db.create_all() # criar tabelas

pedro = Vendedor(nome="Pedro", email="pe@gmail.com", telefone="(47)3394-4176", comissao=10)
db.session.add(pedro)
db.session.commit()

print(pedro)

teresa = Motorista(nome="Teresa", email="tete@gmail.com", telefone="(47)3396-0877", cnh="1234-5")
db.session.add(teresa)
db.session.commit()

print(teresa)