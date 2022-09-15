from config import *

class Pessoa(db.Model): #Tabela Pessoa

    id = db.Column(db.Integer, primary_key = True) #Campo id da tabela Pessoa
    nome = db.Column(db.String(254)) #Campo nome da tabela Pessoa
    email = db.Column(db.String(254)) #Campo email da tabela Pessoa
    telefone = db.Column(db.String(254)) #Campo telefone da tabela Pessoa
    senha = db.Column(db.String(254)) #Campo senha da tabela Pessoa

    def __str__(self) -> str: #Função que retorna uma string
        return f"{self.id}, {self.nome}, {self.email}, {self.telefone}" 

    def json(self): #Função retorna os dados em json
        return {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "senha": self.senha
        }


if __name__ == "__main__":
    db.create_all() #Cria todas as tabelas

    user = Pessoa(nome = "Nikolas", email = "nikolas@nikolas.com", telefone = "999999999", senha = "123") #Objeto de teste

    db.session.add(user) #Insere o objeto 'user' no banco de dados
    db.session.commit() #Confirma a inserção do objeto