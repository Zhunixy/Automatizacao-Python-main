$(document).ready(function () {

    $('.btn-save').click(function (e) {
        e.preventDefault();
        let dados = $('#form-produto').serialize();
        dados += `&operacao=${$('.btn-save').attr('data-operation')}`;
        $.ajax({
            type: 'POST',
            dataType: 'JSON',
            async: true,
            data: dados,
            url: 'php/formulario.php',
            success: function (response) {
                if (response.type === 'success') {
                    alert("Novo registro inserido com sucesso!");
                    $('body').load('index.html');
                } else {
                    alert("Erro: " + response.message);
                }
            }
        });
    });
    
})