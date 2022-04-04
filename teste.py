from abacate import *

class Pessoa(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    tipo = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity':'pessoa',
        'polymorphic_on':'tipo'
    }

    def __str__(self):
        pass

class Vendedor(Pessoa):

    id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), primary_key=True)
    comissao = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity':'vendedor'
    }

    def __str__(self):
        pass

class Motorista(Pessoa):

    id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), primary_key=True)
    cnh = db.Column(db.String(254))

    __mapper_args__ = {
        'polymorphic_identity':'motorista'
    }

    def __str__(self):
        pass

pedro = Vendedor(nome="Pedro", email="pe@gmail.com", comissao=10)
db.session.add(pedro)
db.session.commit()

teresa = Motorista(nome="Teresa", cnh="1234-5")
db.session.add(teresa)
db.session.commit()