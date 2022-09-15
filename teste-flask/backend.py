from config import *
from modelo import Pessoa


@app.route("/") #Esta rota renderiza o arquivo 'index.html' no navegador
def padrao(): #Função da rota
    return render_template("index.html")

@app.route("/listar_pessoas", methods = ["GET"]) #Esta rota retorna as pessoas do banco de dados
def listar_pessoas(): #Função da rota
    try: #Se não houver erros com o backend, será retornada a lista de pessoas
        lista = [x.json() for x in db.session.query(Pessoa).all()]
        resposta = jsonify({"reposta": "ok", "detalhes": lista})
    except Exception as e: #Se houver erros com o backend, será exibida uma mensagem de erro
        resposta = jsonify({"reposta": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Controll-Allow-Origin", "*") #Permite o tráfego de dados de dispostivos fora do escopo local
    return resposta


@app.route("/inserir_pessoas", methods=["POST"]) #Esta rota insere registros no banco de dados obtidos no navegador
def inserir_pessoas(): #Função da rota
    try: #Pega os dados inseridos pelo usuário e mando para o bancdo de dados
        dados = request.get_json() #Pega os dados da requisição do usuário
        pessoa = Pessoa(nome = dados["nome"], #Cria o objeto a ser inserido no banco de dados
                email = dados["email"],
                telefone = dados["telefone"],
                senha = dados["senha"]
        )
        db.session.add(pessoa) #Insere o objeto 'pessoa' no banco de dados
        db.session.commit() #Confirma a inserção do objeto 'pessoa' no banco de dados
        resposta = jsonify({"resultado": "ok", "detalhes": "pessoa incluida"}) #Exibe uma mensagem de confirmação
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    
    resposta.headers.add("Access-Controll-Allow-Origin", "*")
    return resposta        

@app.route("/deletar_pessoa/<id>", methods=["DELETE"]) #Esta rota deleta registros do banco de dados
def deletar_pessoa(id): #Função da rota
    try: #Seleciona uma pessoa do banco de acordo com o id requisitado pelo usuário e deleta o registro selecionado
        pessoa = db.session.query(Pessoa).filter_by(id = id).first() #Percorre a lista de pessoas e seleciona a pessoa de acordo com o id requisitado pelo usuário
        if pessoa is None: #Se não existir o id requisitado será exibida uma mensagem de erro
            raise Exception("O FUDIDO EM QUESTAO NAO EXISTE")
        db.session.delete(pessoa) #Deleta o registro do banco de dados
        db.session.commit() #Confirma o deletamento
        resposta = jsonify({"resultado": "ok", "detalhes": "o otário foi deletado"}) #Exibe uma mensagem de confirmação

    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    
    resposta.headers.add("Access-Controll-Allow-Origin", "*")
    return resposta   

@app.route("/update_pessoa/<id>", methods=["PUT"]) #Esta rota atualiza um registro do banco de dados
def update_pessoa(id): #Função da rota
    try: #Seleciona um resgistro do banco de acordo com o id requisitado pelo usuário e atualiza as informações do registro
        dados = request.get_json(force=True) #Pega os dados da requisição do usuário
        Pessoa.query.filter_by(id = id).update({ #Seleciona o registro do banco de dados e atualiza as informações do registro
            "nome": dados["nome"],
            "email": dados["email"],
            "telefone": dados["telefone"],
            "senha": dados["senha"]
        })
        db.session.commit() #Confirma a atualização do registro
        resposta = jsonify({"resultado": "ok", "detalhes": "o otário foi atualizado"}) #Exibe uma mensagem de confirmação
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Controll-Allow-Origin", "*")
    return resposta   

app.run(debug=True) #Roda o backend