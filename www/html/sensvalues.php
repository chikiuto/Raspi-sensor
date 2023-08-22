<?php

$host = 'mysql5.7';
$db = 'raspi';
$charset = 'utf8';
$dsn = "mysql:host=$host; dbname=$db; charset=$charset";

$user = 'root';
$password = 'secret';

$pdo = new PDO($dsn, $user, $password);


switch ( $_SERVER['REQUEST_METHOD'] ) {
    case 'GET':
        $st = $pdo->query("SELECT * FROM sensorvalues");

        echo json_encode($st->fetchAll(PDO::FETCH_ASSOC));

        break;
        
    case 'POST':
        $in = json_decode(file_get_contents('php://input'), true);
        if (!isset($in['id']))
        {
            $st = $pdo->prepare("INSERT INTO sensorvalues(datetime,temp,hum,press,machine)
                                 VALUES(:datetime,:temp,:hum,:press,:machine)");
        }
        $st->execute($in);
        
        echo json_encode("normal end");
        
        break;
}

?>