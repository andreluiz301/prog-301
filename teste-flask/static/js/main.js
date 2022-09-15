$(function () {

    $.ajax({ 
        url: 'http://localhost:5000/listar_pessoas',
        method: 'GET',
        success: listar,
        error: function () {
            //alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar(pessoas) {
        console.log(pessoas);
        for (var i of pessoas.detalhes) {
            lin = '<tr>' +
                '<td>' + i.nome + '</td>' +
                '<td>' + i.email + '</td>' +
                '<td>' + i.telefone + '</td>' +
                '<td>' + i.senha + '</td>' +
                '</tr>';
            $('#tbody').append(lin);
        }
    }

    $("#bt").on("click", function(){
        namejdsfuis = $("#nome").val();
        email = $("#email").val();
        telefone = $("#telefone").val();
        senha = $("#senha").val();

        const data = JSON.stringify({
            nome:namejdsfuis,
            email:email,
            telefone: telefone,
            senha: senha
        });

        $.ajax({
            url: "http://localhost:5000/inserir_pessoas",
            method: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: data, // estes são os dados enviados
            success: function(resposta){
                console.log(resposta);
            },
            error: function(resposta){
                console.log(resposta);
            }
        });
        
    });

    $("#bt2").on("click", function(){
        id = $("#id").val();

        $.ajax({
            url: `http://localhost:5000/deletar_pessoa/${id}`,
            method: "DELETE",
            success: function(resposta){
                console.log(resposta);
            },
            error: function(resposta){
                console.log(resposta);
            }
        });
    });

    $("#bt3").on("click", function(){
        id = $("#id2").val();
        nome = $("#nome2").val();
        email = $("#email2").val();
        telefone = $("#telefone2").val();
        senha = $("#senha2").val();

        var data = JSON.stringify({
            nome: nome,
            email: email,
            telefone: telefone,
            senha: senha
        });

        $.ajax({
            url: `http://localhost:5000/update_pessoa/${id}`,
            method: "PUT",
            contentType: "application/json",
            dataType: "json",
            data: data,
            success: function(resposta){
                console.log(resposta);
            },
            error: function(resposta){
                console.log(resposta);
            }
        });

    });

});
