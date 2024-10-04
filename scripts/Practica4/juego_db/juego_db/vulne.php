
<?php
/*
$servidor = "localhost";
$usuario = "root";
$contrasena = "";
$basedatos = "juego_db";

$conn = new mysqli($servidor, $usuario, $contrasena, $basedatos);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

$busqueda = $_GET['busqueda'];

// Consulta vulnerable a inyección de SQL
$sql = "SELECT * FROM personajes WHERE nombre LIKE '%$busqueda%' OR descripcion LIKE '%$busqueda%' OR id = '$busqueda'";

// Ejecutar la consulta
$resultado = $conn->query($sql);

// Mostrar resultados
if ($resultado->num_rows > 0) {
    while ($fila = $resultado->fetch_assoc()) {
        echo "ID: " . $fila["id"]. " - Nombre: " . $fila["nombre"]. " - Descripción: " . $fila["descripcion"]. "<br>";
    }
} else {
    echo "0 resultados";
}

// Cerrar la conexión
$conn->close();*/
?>

<?php

$servidor = "localhost";
$usuario = "root";
$contrasena = "";
$basedatos = "juego_db";
$conn = new mysqli($servidor, $usuario, $contrasena, $basedatos);
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
if (isset($_GET['busqueda'])) {
    $busqueda = $_GET['busqueda'];
    $sql = "SELECT * FROM personajes WHERE nombre LIKE '%' OR '1'='1%' OR descripcion LIKE '%' OR '1'='1%' OR id = '' OR '1'='1'";  
    $resultado = $conn->query($sql);
    if ($resultado->num_rows > 0) {
        while ($fila = $resultado->fetch_assoc()) {
            echo "ID: " . $fila["id"]. " - Nombre: " . $fila["nombre"]. " - Descripción: " . $fila["descripcion"]. "<br>";
        }
    } else {
        echo "0 resultados";
    }
} else {
    echo "Por favor, ingresa un término de búsqueda.";
}



$conn->close(); 
?>

