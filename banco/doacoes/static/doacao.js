var URL_BASE = "https://127.0.0.1:8000/api/ongs/";

var buscar_dados = function(url){
    /* Busca os dados da Abong. */
    $('#ong_carregando').removeClass("display-none");
    $('#ongs_conteudo').html('');

    $.ajax({
        url: url,
        data: {},
        success: function(dados){
            var i;
            var dado;
            var html = '';

            for (i=0; i<dados.length; i++){
                dado = dados[i];
                html += '<div id="' + dado['pk'] + '" class="ong_box">';
                html +=     '<input type="checkbox" name="ongs_selecionadas" value="' + dado['pk'] + '">';
                html +=     '<img class="ong_imagem" src="' + dado['imagem'] + '">';
                html +=     '<p>';
                html +=         '<label>ONG: </label>'
                html +=         '<span class="ong_nome">' + dado['nome'] + '</span>';
                html +=     '</p>';
                html +=     '<p>';
                html +=         '<label>Sobre: </label>'
                html +=         '<span class="ong_descricao">' + dado['descricao'] + '</span>';
                html +=     '</p>';
                html +=     '<p>';
                html +=         '<label>Estado: </label>'
                html +=         '<span class="ong_estado">' + dado['estado'].toUpperCase() + '</span>';
                html +=     '</p>';
                html +=     '<p>';
                html +=         '<label>Cidade: </label>'
                html +=         '<span class="ong_cidade">' + dado['cidade_descricao'] + '</span>';
                html +=     '</p>';
                html +=     '<p>';
                html +=         '<label>Site: </label>'
                html +=         '<a class="ong_site" target="_blank" href="' + dado['site'] + '">' + dado['site'] + '</a>';
                html +=     '</p>';
                html +=     '<p>';
                html +=         '<label>Banco: </label>'
                html +=         '<span class="ong_banco">' + dado['banco'] + '</span>';
                html +=     '</p>';
                html +=     '<p>';
                html +=         '<label>Agência: </label>'
                html +=         '<span class="ong_agencia">' + dado['agencia'] + '</span>';
                html +=     '</p>';
                html +=     '<p>';
                html +=         '<label>Conta Corrente: </label>'
                html +=         '<span class="ong_conta">' + dado['conta'] + '</span>';
                html +=     '</p>';
                html +=     '<p>';
                html +=         '<label>Valor de doação: </label>'
                html +=         '<input class="ong_valor_doacao" type="number" name="valor_doacao_ong_' + dado['pk'] + '">'
                html +=     '</p>';
                html += '</div>'
            }
            $('#ong_carregando').addClass("display-none");

            if (html != ''){
                $('#ongs_conteudo').html(
                  "<p>Selecione as ONGs e informe os valores que deseja doar.</p>"
                  + html
                  + '<div class="clear"><button>Efetuar doação</button></div>'
                );
            }
            else {
                $('#ongs_conteudo').html("<p>Nenhum registro encontrado.</p>");
            }
        },
        error: function(){
            $('#ong_carregando').addClass("display-none");
            $('#ongs_conteudo').html('Serviço Temporariamente Indisponível.');
        }
    });
}

var aplicar_filtro = function(){
    var url = URL_BASE;
    var estado = $('#ong_filtro_select_estado').val();
    var cidade = $('#ong_filtro_select_cidade').val();
    var nome_ong = $('#ong_filtro_nome').val();

    if (estado != ""){
        url += estado + "/";
    }
    if (cidade != ""){
        url += cidade + "/";
    }
    if (nome_ong != ""){
        url += "?pesquisa=" + nome_ong;
    }
    buscar_dados(url);
}

var carregar_cidades = function(){
    var estado = $('#ong_filtro_select_estado').val();
    if (estado == ''){
        option = $('<option>', {
            val: '',
            text: '-------'
        });
        $('#ong_filtro_select_cidade').html(option);
        $('#ong_filtro_select_cidade').addClass('not-active');
    }
    else {
        $('#ong_filtro_select_cidade').html('');
        $('#ong_filtro_select_cidade').addClass('not-active');

        $.ajax({
            url: "https://127.0.0.1:8000/api/choices_estado/" + estado + "/",
            data: {},
            success: function(dados){
                var i;
                var dados;
                var option;

                option = $('<option>', {
                    val: '',
                    text: '-------'
                });
                $('#ong_filtro_select_cidade').append(option);

                for (i=0; i<dados.length; i++){
                    dado = dados[i];
                    option = $('<option>', {
                        val: dado[0],
                        text: dado[1]
                    });
                    $('#ong_filtro_select_cidade').append(option);
                }
                $('#ong_filtro_select_cidade').removeClass('not-active');
            },
        })
    }
}

$( window ).load(function(){
    $('#ong_botao_filtrar').click(aplicar_filtro);
    $('#ong_filtro_select_estado').change(carregar_cidades);
    buscar_dados(URL_BASE);
});
