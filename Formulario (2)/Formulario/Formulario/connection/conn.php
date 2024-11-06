<?php
$hostname="localhost";
$dbname="produtos";
$username="root";
$password="";

try{
    $pdo=new PDO('mysql:host='.$hostname.';dbname='.$dbname, $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $resultc = array(
        'type'=>'sucesso',
        'mensagem'=>'conexao efetujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjada com sucesso!'
    );



}catch(PDOException $e){
    $resultc= array(
        'type'=>'error',
        'mensagem'=>'ERR: '.$e->getMessage()
    );

}
?>