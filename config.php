//<?php 
$servername = "tcp:drbotserver.database.windows.net,1433"; // Update with your Azure SQL Server name
$username = "drbot"; // Include the server name in the username
$password = "AquaMan40!@";
$database = "drbothealthdb";

// Connection options
$connectionOptions = array(
    "Database" => $database,
    "Uid" => $username,
    "PWD" => $password,
    "CharacterSet" => "UTF-8"
);

// Establish the connection
$conn = sqlsrv_connect($servername, $connectionOptions);

// Check connection
if ($conn === false) {
    die(print_r(sqlsrv_errors(), true)); // Print SQLSRV errors
}
?>