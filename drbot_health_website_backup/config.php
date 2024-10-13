<?php 
// Database connection
$servername = "localhost";
$username = "drbot_health_user";
$password = "drbot_health@12345";
$database = "drbot_health_final";
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>