<?php
include('../connection/conn.php');
if ($_POST['operacao'] == 'create') {
    if (empty($_POST['Cliente']) || empty($_POST['Produto']) || empty($_POST['Quantidade']) || empty($_POST['Categoria'])) {
        $result = array(
            'type' => 'error',
            'message' => 'Existe(m) campo(s) obrigatório(s) não preenchido(s).'
        );
        echo json_encode($result);
    } else {
        try {
            $sql = "INSERT INTO produtos.vendas(Cliente, Produto, Quantidade, Categoria) VALUES (?, ?, ?, ?)";
            $stmt = $pdo->prepare($sql);
            $stmt->execute([
                $_POST['Cliente'],
                $_POST['Produto'],
                $_POST['Quantidade'],
                $_POST['Categoria']
            ]);
            $result = array(
                'type' => 'success',
                'message' => 'Registro cadastrado com sucesso'
            );
            echo json_encode($result);
        } catch (PDOException $e) {
            $result = array(
                'type' => 'error',
                'message' => 'Erro: ' . $e->getMessage()
            );
            echo json_encode($result);
        }
    }
}





?>