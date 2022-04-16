from config import *


class Casa (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formato = db.Column(db.String(254))

    quartos = db.relationship("Quarto", backref="casa")

    def __str__(self):
        c = f'Casa | Id: {self.id}, Formato: {self.formato}'
        print()
        return c
    
        
class Quarto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    dimensoes = db.Column(db.String(254))

    casa_id = db.Column(db.Integer, db.ForeignKey(Casa.id), 
                          nullable=False)
    #casa = db.relationship("Casa")

    mobilias = db.relationship("Mobilia", backref="quarto")

    def __str__(self):
        s = f'Quarto | Nome: {self.nome}, Dim.: {self.dimensoes}'
        s += f'\nNa casa: {str(self.casa)}'
        print()
        return s


class Mobilia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    funcao = db.Column(db.String(254))
    material = db.Column(db.String(254))
    
    quarto_id = db.Column(db.Integer, db.ForeignKey(Quarto.id), nullable=True)

    tvs = db.relationship("Tv", backref="mobilia")

    def __str__(self) -> str:
        a = f'Mobilia | Nome: {self.nome}, Função: {self.funcao}, Material: {self.material}. '
        a += f'\nNo quarto: {str(self.quarto)}'
        return a


class Tv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(254))
    modelo = db.Column(db.String(254))
    tamanho = db.Column(db.Integer)

    mobilia_id = db.Column(db.Integer, db.ForeignKey(Mobilia.id), nullable=True)

    def __str__(self) -> str:
        a = f'Tv | Marca: {self.marca}, Modelo: {self.modelo}, Tamanho: {self.tamanho}p.'
        return a


if __name__ == "__main__": # teste das classes
    
    if os.path.exists(arquivobd): # se houver o arquivo...
        os.remove(arquivobd) # ...apagar!

    db.create_all() # criar tabelas

    print("TESTE CRIANDO DADOS")

    c1 = Casa(formato="Germânica") # cria uma casa

    # persiste para criar o id
    db.session.add(c1)
    db.session.commit()

    print(c1) # exibir atributos da casa

    q1 = Quarto(nome="Sala", dimensoes="6x5 metros", casa=c1)
    q2 = Quarto(nome="Banheiro", dimensoes="3x4 metros", casa=c1)
    
    db.session.add(q1)
    db.session.add(q2)
    db.session.commit()

    print(q1, q2)

    m1 = Mobilia(nome="Armário", funcao="Guardar", material="Madeira", quarto=q1)

    db.session.add(m1)
    db.session.commit()

    print(m1)

    tv1 = Tv(marca="Samsung", modelo="k11", tamanho=43)
    print(tv1)

    print('')
    print("TESTE COM TODOS OS DADOS")
    print(c1) # casa
    # quartos da casa, sem lista reversa
    for q in db.session.query(Mobilia).filter().all():
        print(q)
    
    print('\nLISTA REVERSA:', end="")
    for q in c1.quartos and q1.mobilias:
        print(q)